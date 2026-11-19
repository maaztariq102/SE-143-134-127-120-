"""Dashboard and sample-data reset features."""

from loans import is_overdue
from storage import active_loans, confirm, sample_data, save_data


def stats(db):
    loans = active_loans(db)
    return {
        "Book titles": len(db["books"]),
        "Total copies": sum(book["copies"] for book in db["books"]),
        "Members": len(db["members"]),
        "Books on loan": len(loans),
        "Overdue loans": sum(1 for loan in loans if is_overdue(loan)),
    }


def ui_dashboard(db):
    print("\n--- Dashboard ---")
    for label, value in stats(db).items():
        print(f" {label:<15} {value}")
    from loans import loan_rows, LOAN_HEADERS
    overdue = [loan for loan in active_loans(db) if is_overdue(loan)]
    print("\n--- Overdue loans ---")
    from storage import print_table
    print_table(LOAN_HEADERS, loan_rows(db, overdue))


def ui_reset(db):
    if confirm("Delete all data and restore the sample data?"):
        db.clear()
        db.update(sample_data())
        save_data(db)
        print("Sample data restored.")
