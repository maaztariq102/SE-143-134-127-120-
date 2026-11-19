# Scrum lab evidence log

Use this file as the team's evidence checklist and record. **Only enter events, estimates, approvals, test results, and decisions that actually happened.** Do not fill in meeting outcomes or claim a story is Done before the evidence exists. Keep the GitHub Scrum Log issue as the primary event log; this file is a structured index and fallback record.

## Team and roles

| Accountability | Student name | GitHub username | Confirmed by team? |
| --- | --- | --- | --- |
| Product Owner | Maaz | @MaazTariq102 | [ ] |
| Scrum Master | Ali | @Ali | [ ] |
| Developer | Ali | @Ali | [ ] |
| Developer | Confirm name | Confirm username | [ ] |
| Stakeholder | Instructor | Confirm username | [ ] |

Resolve the duplicate/incomplete Developer identity and verify that the listed usernames are real before submitting this record.

## Product Goal

> A simple system that lets our department library keep track of its books, its members and who has borrowed what.

## Definition of Done

A story is Done only after every acceptance criterion is demonstrated, the changes are on a feature branch and merged by an approved pull request, the other Developer reviewed and approved, the PR closes the correct issue, `python main.py` runs, `python -m unittest -v` passes, and the PO accepts the story at Sprint Review.

## Backlog and issue audit

Record live issue links and decisions. Opening/closing an issue is not proof of completion; issue state must match implementation, PR, tests, and PO acceptance.

| Story | GitHub issue | Priority (PO) | Size (Developers) | Current state | Acceptance/DoD evidence or remaining work |
| --- | --- | --- | --- | --- | --- |
| US-01 Add a book | Create/link issue | Must | Agree in planning poker | Not confirmed | |
| US-02 List all books | #7 | Must | Agree in planning poker | Verify/reopen unless DoD met | |
| US-03 Edit/delete a book | Create/link issue | Should | Agree in planning poker | Not confirmed | |
| US-04 Search books | Create/link issue | Should | Agree in planning poker | Not confirmed | |
| US-05 Register/remove members | #6 | Must | Agree in planning poker | Verify/reopen unless DoD met | |
| US-06 Issue a book | #5 | Must | L reference; split before sprint if still L | Split/verify | |
| US-07 Return a book | #4 | Must | Agree in planning poker | Verify/reopen unless DoD met | |
| US-08 Overdue/fines | #2 | Should | Agree in planning poker | Verify/reopen unless DoD met | |
| US-09 Dashboard | #3 | Could | Agree in planning poker | Verify/reopen unless DoD met | |

Issue #1 titled `user-story` was a test issue, not a real backlog story. Keep it closed or remove it through GitHub UI if permitted; do not present it as lab work.

## Sprint 1 record

**Sprint dates/timebox:** [enter actual start/end and 35-minute work timebox]  
**Sprint Goal agreed by team:** [record the exact sentence]  
**Planning attendees:** [names]  
**Selected story/task issue links:** [links]  
**Capacity rationale and estimates:** [record actual poker results and team reasoning]

### Daily Scrum (at planned midpoint)

Post one truthful summary comment to the Scrum Log issue; repeat a row per Developer.

| Developer | What was finished since last check? | Next step | Impediment and owner/action |
| --- | --- | --- | --- |
| | | | |
| | | | |

### Sprint Review and increment

- Demo date/attendees: [actual details]
- Stakeholder feedback (quote or accurate summary): [record]
- Stories accepted by PO, with acceptance evidence: [links and demonstration notes]
- Stories rejected/carried over and reason: [links and reason]
- Working increment on `main`: [PR/merge links]
- Test command/result and environment: [actual output or CI link]
- Sprint 1 Project Insights chart: [link and screenshot attached to Scrum Log]

### Sprint 1 Retrospective

Each team member adds at least one actual point for each heading, preferably as comments on the retrospective issue.

- **What went well:** [actual observations]
- **What did not go well:** [actual observations]
- **What we will change:** [one or two specific experiments, owner, and check date]
- Retrospective issue: [link]
- Improvement action issues assigned to Sprint 2: [links]

## Refinement and stakeholder change request

- Change request, as provided by instructor (quote/accurate summary): [record; instructor supplies this]
- New or changed story issue: [link]
- Developer estimate and discussion: [record actual consensus]
- PO priority/backlog-order decision and rationale: [record]
- Questions answered by stakeholder: [record]

## Sprint 2 record

**Sprint dates/timebox:** [actual start/end and 30-minute work timebox]  
**Sprint Goal agreed by team:** [exact sentence]  
**Planning attendees:** [names]  
**Selected stories/tasks and carry-over rationale:** [issue links and rationale]

### Daily Scrum

| Developer | What was finished since last check? | Next step | Impediment and owner/action |
| --- | --- | --- | --- |
| | | | |
| | | | |

### Sprint Review and increment

- Demo date/attendees: [actual details]
- Stakeholder feedback: [actual feedback]
- Stories accepted/rejected by PO and evidence: [links]
- Working increment on `main`: [PR/merge links]
- Test command/result: [actual output or CI link]
- Sprint 2 Project Insights chart: [link and screenshot attached to Scrum Log]

### Sprint 2 Retrospective

- **What went well:** [actual observations]
- **What did not go well:** [actual observations]
- **What we will change:** [specific action, owner, check date]
- Retrospective issue: [link]

## Results and release

| Sprint | Stories accepted | Sizes | Velocity (story count and sizes) | Evidence links |
| --- | --- | --- | --- | --- |
| Sprint 1 | | | | |
| Sprint 2 | | | | |

- Release tag/release URL: [create `v1.0` from `main` only after Sprint 2; list delivered stories]
- Final `main` commit: [SHA/link]
- Final test run: [actual command, date, Python version, result]

## Teacher-facing evidence checklist

- [ ] README identifies the actual team and roles; all usernames are confirmed.
- [ ] Scrum Project board is linked and shows the agreed Status, Size, Priority, and Sprint fields, two iterations, required views, and active workflows.
- [ ] Product Backlog issue ordering and estimates reflect actual PO/Developer decisions; no story is marked Done without the DoD.
- [ ] Sprint task issues are linked to their parent stories, labeled `task`, assigned to the Developers, and placed in the right iteration/status.
- [ ] Scrum Log is pinned and has actual Sprint Goals, Daily Scrum notes, review outcomes, chart screenshots, and velocity.
- [ ] Retrospective issue includes contributions from every team member and links improvement actions to Sprint 2.
- [ ] Stakeholder change request and PO prioritization decision are recorded.
- [ ] PRs link to their story with `Closes #<number>`, show the other Developer's approval, and are merged to `main`.
- [ ] Repository branch protection requires a PR and one approval.
- [ ] Program and unit-test results are recorded from an actual run.
- [ ] `v1.0` release lists only stories accepted and delivered by Sprint 2.
- [ ] Screenshots/links are readable and do not expose secrets or personal data.
