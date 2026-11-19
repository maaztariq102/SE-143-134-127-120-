# SE-143-134-127-120 — Library Management System

A simple Library Management System developed using two compressed Scrum sprints and GitHub Projects.

## Product Goal
A simple system that lets our department library keep track of its books, its members and who has borrowed what.

## Team and roles
| Role | Name | GitHub username |
| --- | --- | --- |
| Product Owner (PO) | Maaz | @maaztariq102 |
| Scrum Master (SM) | To be confirmed by team | TBD |
| Developer 1 | To be confirmed by team | TBD |
| Developer 2 | To be confirmed by team | TBD |
| Stakeholder | Instructor | TBD |

**Team:** replace every TBD with the actual member name and GitHub username; the earlier README repeated an unverified `@Ali` placeholder.

## Definition of Done
A story counts as Done only when **all** of the following are met:

- [ ] Every acceptance criterion is met.
- [ ] Code was developed on a feature branch and merged into `main` through a pull request.
- [ ] The other Developer reviewed and approved the PR.
- [ ] The PR linked and closed the story issue with `Closes #<issue-number>`.
- [ ] `python main.py` runs without errors and `python -m unittest` passes.
- [ ] The Product Owner accepted the story at its Sprint Review.

## Scrum tracking
- [Product Backlog (user-story issues)](../../issues?q=is%3Aissue+label%3Auser-story)
- [Scrum Log](../../issues/11)
- [Pull requests](../../pulls)

The nine required user stories are US-01 through US-09. The proposed Sprint 1 goal from the lab handout is **“A librarian can add books and see the full catalogue.”** The actual Sprint Goal, scope, dates, and results must be documented after team agreement.

## Development
The complete example application is currently on `feature/library-management-system` rather than `main`. Review it as reference code, then implement/deliver individual chosen stories with genuine feature-specific branches, tests, PR reviews and Sprint records. Do **not** treat the presence of reference code as proof that a story is Done.

Commands (once the relevant code is available locally):

```bash
python main.py
python -m unittest -v
```
