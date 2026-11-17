# Codex Task & Review Templates

## A. Read-only ticket preparation (owner to Codex)

> Task: [TICKET-ID] — [TITLE]
> Repository branch/commit: [ACTUAL]
> Scope/paths to inspect: [PATHS]
> Acceptance: [BEHAVIORS + FAILURES]
> Read AGENTS.md, docs/README.md and relevant accepted ADR/contracts first.
> READ-ONLY. Do NOT edit code/docs, install dependencies, commit, create branches, PR or deploy.
> Explain constraints, identify open design questions, suggest 2–3 alternatives with trade-offs, and provide test cases. I will design and write all code.

## B. Design review (before coding)

> Review my proposed domain objects/state diagram/API. Challenge invariants, concurrency, retries, authentication and domain ownership. Classify each concern by severity and give the smallest adjustment. No generated implementation.

## C. Code review (after human implementation)

> Compare my branch diff against the ticket and approved ADRs. Report issues BLOCKER/HIGH/MEDIUM/LOW with exact file:line, evidence/reproduction, why wrong, minimal fix direction and test to verify. Identify tests NOT RUN. Do not write or modify code.

## D. Test/failure audit

> Inspect the tests I wrote and execution logs. Suggest missing boundary, malformed-input, cancellation, race, retry, resource-limit and recovery cases. Do not invent test results. If a test fails, propose hypotheses and commands I can run to distinguish them.

## E. Architecture audit

> Inspect dependency directions and public contract compatibility. Look for Domain→ORM/Framework leaks, cross-domain SQL, duplicate scheduler/state ownership, unauthorized knowledge scope and unsafe tools. Output a compact risk register with evidence.

## F. Verification report template

| Field | Required content |
| --- | --- |
| Ticket / branch / commit | Stable identity |
| Scope | Exact reviewed paths |
| Evidence | Source lines, test commands/results, CI run URL if observed |
| Findings | Severity, file:line, minimal fix direction, verification test |
| Status | VERIFIED / IMPLEMENTED_UNVERIFIED / PROPOSED / BLOCKED |
| Regression risk | Shared contracts, DB, security, traces, downstream consumers |
| Human follow-up | One bounded next task; Codex does not auto-apply |

## G. AI permissions escalation

Default L1–L3 hints only. If the engineer requests a targeted code correction, ask for the exact offending snippet/path/behavior when not already available; limit code to that correction and preserve all unrelated changes. The owner still reviews/runs/commits. Never infer permission to push based solely on having GitHub access.
