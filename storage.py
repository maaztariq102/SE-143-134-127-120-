"""Settings, JSON data storage and shared helpers for the library app."""

import json
import os
from datetime import date

# Settings
DATA_FILE = "library_data.json"
LOAN_DAYS = 14
MAX_LOANS = 3
FINE_PER_DAY = 10


def sample_data():
    """Return a fresh copy of the starter books, members and loans."""
    return {
        "next_id": 6,
        "books": [
            {"id": "B1", "title": "Clean Code", "author": "Robert C. Martin", "isbn": "9780132350884", "category": "Programming", "copies": 3},
            {"id": "B2", "title": "Introduction to Algorithms", "author": "Cormen et al.", "isbn": "9780262046305", "category": "Algorithms", "copies": 2},
            {"id": "B3", "title": "Software Engineering", "author": "Ian Sommerville", "isbn": "9780133943030", "category": "Software Engineering", "copies": 4},
        ],
        "members": [
            {"id": "M4", "name": "Ayesha Khan", "email": "ayesha@example.com", "phone": "0300-1234567"},
            {"id": "M5", "name": "Bilal Ahmed", "email": "bilal@example.com", "phone": ""},
        ],
        "loans": [],
    }


def load_data(path=None):
    """Load data from JSON, or return starter data if it is missing/unreadable."""
    path = path or DATA_FILE
    if not os.path.exists(path):
        return sample_data()
    try:
        with open(path, encoding="utf-8") as data_file:
            return json.load(data_file)
    except (json.JSONDecodeError, OSError):
        print("Warning: data file could not be read; starting with sample data.")
        return sample_data()


def save_data(db, path=None):
    """Persist the database as readable JSON."""
    with open(path or DATA_FILE, "w", encoding="utf-8") as data_file:
        json.dump(db, data_file, indent=2)


def new_id(db, prefix):
    result = f"{prefix}{db['next_id']}"
    db["next_id"] += 1
    return result


def find_book(db, book_id):
    return next((book for book in db["books"] if book["id"] == book_id.upper()), None)


def find_member(db, member_id):
    return next((member for member in db["members"] if member["id"] == member_id.upper()), None)


def active_loans(db):
    return [loan for loan in db["loans"] if loan["return_date"] is None]


def copies_on_loan(db, book_id):
    return sum(1 for loan in active_loans(db) if loan["book_id"] == book_id)


def available_copies(db, book):
    return book["copies"] - copies_on_loan(db, book["id"])


def today():
    return date.today()


def ask(prompt, required=True):
    while True:
        value = input(f"{prompt}: ").strip()
        if value or not required:
            return value
        print(" This field is required.")


def ask_int(prompt, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt}{suffix}: ").strip()
        if not raw and default is not None:
            return default
        if raw.isdigit():
            return int(raw)
        print(" Please enter a whole number.")


def confirm(prompt):
    return input(f"{prompt} (y/n): ").strip().lower() == "y"


def print_table(headers, rows):
    """Print rows in a simple text table."""
    if not rows:
        print(" (nothing to show)")
        return
    widths = [max(len(str(value)) for value in column) for column in zip(headers, *rows)]
    line = " ".join(header.ljust(width) for header, width in zip(headers, widths))
    print(line)
    print("-" * len(line))
    for row in rows:
        print(" ".join(str(value).ljust(width) for value, width in zip(row, widths)))
