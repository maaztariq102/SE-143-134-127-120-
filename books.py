"""Book catalog features: add, list, edit, delete and search."""

import re

from storage import (
    ask,
    ask_int,
    available_copies,
    confirm,
    copies_on_loan,
    find_book,
    new_id,
    print_table,
    save_data,
)


def clean_isbn(isbn):
    return re.sub(r"[-\s]", "", isbn)


def validate_book(db, title, author, isbn, copies, book_id=None):
    """Return a normalized ISBN, or raise ValueError for invalid book data."""
    if not title or not author or not isbn:
        raise ValueError("Title, author and ISBN are required.")
    isbn = clean_isbn(isbn)
    if not re.fullmatch(r"\d{10}|\d{13}", isbn):
        raise ValueError("ISBN must be 10 or 13 digits.")
    if copies < 1:
        raise ValueError("Copies must be at least 1.")
    for book in db["books"]:
        if book["isbn"] == isbn and book["id"] != book_id:
            raise ValueError(f'A book with ISBN {isbn} already exists: "{book["title"]}".')
    return isbn


def add_book(db, title, author, isbn, category, copies):
    isbn = validate_book(db, title, author, isbn, copies)
    book = {
        "id": new_id(db, "B"), "title": title, "author": author,
        "isbn": isbn, "category": category, "copies": copies,
    }
    db["books"].append(book)
    save_data(db)
    return book


def ui_add_book(db):
    print("\n--- Add a book ---")
    title = ask("Title")
    author = ask("Author")
    isbn = ask("ISBN (10 or 13 digits)")
    category = ask("Category", required=False)
    copies = ask_int("Copies", default=1)
    try:
        book = add_book(db, title, author, isbn, category, copies)
        print(f'Added "{book["title"]}" with ID {book["id"]}.')
    except ValueError as error:
        print(f"Error: {error}")


BOOK_HEADERS = ["ID", "Title", "Author", "ISBN", "Category", "Available / Total"]


def book_rows(db, books):
    return [
        [book["id"], book["title"], book["author"], book["isbn"],
         book["category"] or "-", f'{available_copies(db, book)} / {book["copies"]}']
        for book in books
    ]


def ui_list_books(db):
    print("\n--- All books ---")
    books = sorted(db["books"], key=lambda book: book["title"].lower())
    print_table(BOOK_HEADERS, book_rows(db, books))


def edit_book(db, book_id, title, author, isbn, category, copies):
    book = find_book(db, book_id)
    if book is None:
        raise ValueError(f"No book with ID {book_id}.")
    isbn = validate_book(db, title, author, isbn, copies, book_id=book["id"])
    on_loan = copies_on_loan(db, book["id"])
    if copies < on_loan:
        raise ValueError(f"Cannot set copies below {on_loan}; that many are on loan.")
    book.update(title=title, author=author, isbn=isbn, category=category, copies=copies)
    save_data(db)
    return book


def delete_book(db, book_id):
    book = find_book(db, book_id)
    if book is None:
        raise ValueError(f"No book with ID {book_id}.")
    if copies_on_loan(db, book["id"]) > 0:
        raise ValueError(f'"{book["title"]}" has copies on loan and cannot be deleted.')
    db["books"].remove(book)
    save_data(db)
    return book


def ui_edit_book(db):
    print("\n--- Edit a book (press Enter to keep the current value) ---")
    book = find_book(db, ask("Book ID"))
    if book is None:
        print("Error: no book with that ID.")
        return
    title = ask(f'Title [{book["title"]}]', required=False) or book["title"]
    author = ask(f'Author [{book["author"]}]', required=False) or book["author"]
    isbn = ask(f'ISBN [{book["isbn"]}]', required=False) or book["isbn"]
    category = ask(f'Category [{book["category"]}]', required=False) or book["category"]
    copies = ask_int("Copies", default=book["copies"])
    try:
        edit_book(db, book["id"], title, author, isbn, category, copies)
        print(f'"{title}" updated.')
    except ValueError as error:
        print(f"Error: {error}")


def ui_delete_book(db):
    print("\n--- Delete a book ---")
    book = find_book(db, ask("Book ID"))
    if book is None:
        print("Error: no book with that ID.")
        return
    if not confirm(f'Delete "{book["title"]}"?'):
        print("Cancelled.")
        return
    try:
        delete_book(db, book["id"])
        print(f'"{book["title"]}" deleted.')
    except ValueError as error:
        print(f"Error: {error}")


def search_books(db, query):
    query = query.lower()
    found = [
        book for book in db["books"]
        if query in f'{book["title"]} {book["author"]} {book["isbn"]} {book["category"]}'.lower()
    ]
    return sorted(found, key=lambda book: book["title"].lower())


def ui_search_books(db):
    print("\n--- Search books ---")
    results = search_books(db, ask("Title, author, ISBN or category"))
    if not results:
        print("No books found.")
        return
    print_table(BOOK_HEADERS, book_rows(db, results))
