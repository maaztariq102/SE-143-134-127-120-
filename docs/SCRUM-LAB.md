# Scrum lab execution guide

This guide records the GitHub-side Scrum artifacts and work still needed for the two-sprint lab. The application code is in the repository root; the Product Backlog should be created as GitHub Issues from these story definitions and managed in the linked Project.

## Product Goal

A simple system that lets the department library keep track of its books, its members and who has borrowed what.

## Product Backlog issue drafts

Create one issue per story using `.github/ISSUE_TEMPLATE/user-story.md`. Apply the `user-story` label and set the Priority and Size project fields. Suggested initial ordering follows the lab; the Product Owner decides the final order. Reference sizes are suggestions and must be agreed by the Developers in planning poker.

### US-01: Add a book
**Story:** As a librarian, I want to add a book so that it appears in the catalogue.
**Acceptance criteria:**
- [ ] Title, author and ISBN are required.
- [ ] ISBN is 10 or 13 digits after removing spaces and hyphens, and is unique.
- [ ] Copies must be at least 1.
**Priority:** Must · **Reference size:** M

### US-02: List all books
**Story:** As a librarian, I want to see all books with their available copies so that I know what can be lent.
**Acceptance criteria:**
- [ ] Each row shows ID, title, author, ISBN, category and available / total copies.
- [ ] Books are sorted by title.
**Priority:** Must · **Reference size:** S

### US-03: Edit or delete a book
**Story:** As a librarian, I want to edit or delete a book so that the catalogue stays correct.
**Acceptance criteria:**
- [ ] Book details can be edited and saved.
- [ ] Copies cannot be reduced below the number currently on loan.
- [ ] Deletion asks for confirmation and is blocked while copies are on loan.
**Priority:** Should · **Reference size:** M

### US-04: Search books
**Story:** As a member, I want to search books so that I can find a title quickly.
**Acceptance criteria:**
- [ ] Search matches title, author, ISBN or category without case sensitivity.
- [ ] An empty result displays “No books found”.
**Priority:** Should · **Reference size:** S

### US-05: Register and remove members
**Story:** As an admin, I want to register and remove members so that only members can borrow.
**Acceptance criteria:**
- [ ] Name and a valid email address are required.
- [ ] Duplicate email addresses are rejected.
- [ ] A member with books on loan cannot be removed.
**Priority:** Must · **Reference size:** M

### US-06: Issue a book
**Story:** As a librarian, I want to issue a book to a member so that every loan is recorded.
**Acceptance criteria:**
- [ ] Only books with available copies can be issued.
- [ ] Due date is 14 days after issue.
- [ ] A member cannot have more than 3 active loans or duplicate active copies of the same book.
- [ ] Available copies decrease by one after issue.
**Priority:** Must · **Reference size:** L; split into smaller, independently useful stories before sprint selection.

### US-07: Return a book
**Story:** As a librarian, I want to record a returned book so that it can be lent again.
**Acceptance criteria:**
- [ ] A book is returned by its loan ID.
- [ ] The returned copy becomes available again.
- [ ] The default loan list shows active loans; returned loans are shown only when requested.
**Priority:** Must · **Reference size:** M

### US-08: Overdue loans and fines
**Story:** As a librarian, I want to see overdue loans and fines so that I can follow up with members.
**Acceptance criteria:**
- [ ] Overdue loans are marked OVERDUE with days late.
- [ ] Fine is Rs 10 per day late.
- [ ] Fine is shown when a late book is returned.
**Priority:** Should · **Reference size:** M

### US-09: Dashboard
**Story:** As an admin, I want a dashboard with key numbers so that I see the library’s state at a glance.
**Acceptance criteria:**
- [ ] Shows counts of book titles, members, books on loan and overdue loans.
- [ ] Shows a list of overdue loans.
**Priority:** Could · **Reference size:** S

## Suggested sprint planning

- **Sprint 1 goal:** “A librarian can add books and see the full catalogue.” Suggested stories: the project skeleton task, US-01, and US-02.
- **Sprint 2:** Plan from the inspected Sprint 1 result, stakeholder feedback, team capacity, and updated backlog order. The lab suggests US-05 or US-04 as likely candidates; US-06 must be split before selection if it remains size L.
- Create technical tasks as `task`-labelled sub-issues only for stories selected into a sprint. The skeleton task has no parent story.

## Definition of Done

- [ ] Every story acceptance criterion is met.
- [ ] Code is merged to `main` from a feature branch through a pull request.
- [ ] The other Developer reviewed and approved the pull request.
- [ ] The pull request contains `Closes #<issue number>`.
- [ ] `python main.py` runs without errors and `python -m unittest` passes.
- [ ] The Product Owner accepts the story at Sprint Review.

## GitHub setup and lab evidence checklist

Complete these in the repository and the linked Project:

- [ ] Confirm team member names and GitHub usernames; replace the TBD entries in README.
- [ ] Add collaborators and grant Project write access to the team.
- [ ] Create `user-story`, `task`, `bug`, and `blocked` repository labels.
- [ ] Create the repository Project board and configure Status options: Product Backlog, Sprint Backlog, In Progress, In Review, Done.
- [ ] Add Size (S/M/L), Priority (Must/Should/Could), and Sprint (Sprint 1/Sprint 2) fields and iterations.
- [ ] Add Product Backlog and current-sprint Sprint Board views; enable item-added, item-closed, merged-PR, and auto-add workflows.
- [ ] Protect `main` by requiring a pull request and one approval.
- [ ] Create/pin a Scrum Log issue; record Daily Scrum notes, Sprint Goals, and Sprint results there.
- [ ] Create Sprint 1 and Sprint 2 status charts and attach screenshots to the Scrum Log.
- [ ] Hold the stakeholder reviews and team retrospectives; record feedback and improvement actions.
- [ ] Create the `v1.0` release from `main` after Sprint 2, listing delivered stories.

The repository guide is preparatory documentation only; checking a box here does not configure or create the corresponding GitHub resource.
