# Library Management System

A simple, offline Library Management System built in Python as a two-sprint Scrum lab using GitHub Projects.

## Product vision

A simple system that lets our department library keep track of its books, its members and who has borrowed what.

## Team and roles

| Role | Name | GitHub username |
| --- | --- | --- |
| Product Owner (PO) | Maaz | @MaazTariq102 |
| Scrum Master (SM) | Ali | @Ali |
| Developer | Ali | @Ali |
| Developer | Ali | TBD |
| Stakeholder | Instructor | TBD |

## Definition of Done

A user story is Done only when:

- [ ] Every acceptance criterion is met.
- [ ] Code is on a feature branch and merged to `main` through a pull request.
- [ ] The other Developer reviewed and approved the pull request.
- [ ] The pull request closes its issue (`Closes #<issue number>`).
- [ ] The program runs with `python main.py` without errors, and `python -m unittest` passes.
- [ ] The PO accepted the story at the Sprint Review.

## Run the application

Requires Python 3.10 or newer; there are no third-party dependencies.

```bash
python main.py
```

The application creates `library_data.json` on first run. Choose **Reset sample data** from the menu to restore the starter dataset.

## Run the tests

```bash
python -m unittest -v
```

Tests use a temporary data file and do not overwrite the application's data.

## Backlog reference

The intended Product Backlog is US-01 Add a book (Must), US-02 List all books (Must), US-03 Edit or delete a book (Should), US-04 Search books (Should), US-05 Register and remove members (Must), US-06 Issue a book (Must), US-07 Return a book (Must), US-08 Overdue loans and fines (Should), and US-09 Dashboard (Could). The team should create and order the corresponding issues and track sprint work in the linked Scrum Board.
