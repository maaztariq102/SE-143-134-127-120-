"""Unit tests for library stories. Run with: python -m unittest -v"""

import os
import tempfile
import unittest
from datetime import date

import storage
from storage import sample_data


class LibraryTestCase(unittest.TestCase):
    """Use a temporary data file so tests never touch real application data."""

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()
        storage.DATA_FILE = self.tmp.name
        self.db = sample_data()

    def tearDown(self):
        os.remove(self.tmp.name)


class TestBooks(LibraryTestCase):
    def test_add_book_normalizes_isbn(self):
        from books import add_book
        book = add_book(self.db, "Python Crash Course", "Eric Matthes", "978-1-59327-603-4", "Programming", 2)
        self.assertEqual(book["isbn"], "9781593276034")
        self.assertIn(book, self.db["books"])

    def test_invalid_and_duplicate_isbn_rejected(self):
        from books import add_book
        with self.assertRaises(ValueError):
            add_book(self.db, "X", "Y", "123", "", 1)
        with self.assertRaises(ValueError):
            add_book(self.db, "X", "Y", "9780132350884", "", 1)

    def test_listing_shows_books_sorted_by_title(self):
        from books import book_rows
        rows = book_rows(self.db, sorted(self.db["books"], key=lambda book: book["title"].lower()))
        self.assertEqual([row[1] for row in rows], ["Clean Code", "Introduction to Algorithms", "Software Engineering"])
        self.assertEqual(rows[0][-1], "3 / 3")

    def test_search_is_case_insensitive(self):
        from books import search_books
        self.assertEqual([book["id"] for book in search_books(self.db, "sommerville")], ["B3"])
        self.assertEqual(search_books(self.db, "no such book"), [])

    def test_cannot_delete_book_on_loan(self):
        from books import delete_book
        from loans import issue_book
        issue_book(self.db, "M4", "B1")
        with self.assertRaises(ValueError):
            delete_book(self.db, "B1")

    def test_cannot_reduce_copies_below_loans(self):
        from books import edit_book
        from loans import issue_book
        issue_book(self.db, "M4", "B1")
        with self.assertRaises(ValueError):
            edit_book(self.db, "B1", "Clean Code", "Robert C. Martin", "9780132350884", "Programming", 0)


class TestMembers(LibraryTestCase):
    def test_add_member_and_reject_duplicate_email(self):
        from members import add_member
        add_member(self.db, "Sara Ali", "sara@example.com")
        with self.assertRaises(ValueError):
            add_member(self.db, "Sara Two", "SARA@example.com")

    def test_cannot_remove_member_with_loan(self):
        from loans import issue_book
        from members import remove_member
        issue_book(self.db, "M5", "B2")
        with self.assertRaises(ValueError):
            remove_member(self.db, "M5")


class TestLoans(LibraryTestCase):
    def test_issue_sets_due_date_and_reduces_available_copies(self):
        from loans import issue_book
        loan = issue_book(self.db, "M4", "B2", on_date=date(2026, 11, 1))
        self.assertEqual(loan["due_date"], "2026-11-15")
        self.assertEqual(storage.available_copies(self.db, storage.find_book(self.db, "B2")), 1)

    def test_loan_limit(self):
        from loans import issue_book
        for book_id in ["B1", "B2", "B3"]:
            issue_book(self.db, "M4", book_id)
        self.db["books"].append({"id": "B9", "title": "T", "author": "A", "isbn": "1234567890", "category": "", "copies": 1})
        with self.assertRaises(ValueError):
            issue_book(self.db, "M4", "B9")

    def test_late_return_fine(self):
        from loans import issue_book, return_book
        loan = issue_book(self.db, "M4", "B1", on_date=date(2026, 11, 1))
        self.assertEqual(return_book(self.db, loan["id"], on_date=date(2026, 11, 20)), 50)

    def test_overdue_status_and_fine(self):
        from loans import fine_for, is_overdue, issue_book
        loan = issue_book(self.db, "M4", "B1", on_date=date(2026, 11, 1))
        self.assertTrue(is_overdue(loan, date(2026, 11, 20)))
        self.assertEqual(fine_for(loan, date(2026, 11, 20)), 50)


class TestDashboard(LibraryTestCase):
    def test_dashboard_counts(self):
        from dashboard import stats
        self.assertEqual(stats(self.db)["Book titles"], 3)
        self.assertEqual(stats(self.db)["Members"], 2)
        self.assertEqual(stats(self.db)["Books on loan"], 0)


if __name__ == "__main__":
    unittest.main()
