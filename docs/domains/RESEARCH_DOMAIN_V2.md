# RESEARCH Domain v2 — AI Engineering Research & Decision Intelligence

**Status: PRODUCT DESIGN PROPOSAL.** No working Research API, Agent, worker or evidence pipeline has been verified in the existing GitHub scaffold. Owner writes source; Codex reviews.

## Purpose and user

Primary user: solo AI Engineer progressing toward Senior AI Engineer, who researches technology choices, production architectures, algorithms, codebases and engineering decisions. RESEARCH is an **evidence-led Co-Engineer**, not merely a document summarizer and not an autonomous coding agent.

## Business capabilities

| Capability | Input | Expected output | Explicit boundary |
| --- | --- | --- | --- |
| Explore / Technical Research | topic, constraints, resources | concept map, sources, key findings | No ungrounded generalizations |
| Deep Research | scoped question + budget | plans, findings, evidence report | Bounded steps/calls/time |
| Compare & Decide | criteria, candidates | trade-off matrix, conditions, ADR **draft** | Human approves final decision |
| Architecture Review | proposal, scenarios, artifacts | risks, missing assumptions, alternatives | Read-only review, no code edits |
| Experiment Design / Analysis | hypothesis, evidence/logs | methodology, metrics, conclusions with uncertainty | Does not claim benchmark execution unless actually run |
| Knowledge Exploration | question, prior work | annotated explanation and exercises | User owns learning and implementation |
| Research Continuation | Research project / artifact refs | updated analysis with source versions | Cross-project ACL, no stale silent memory |

## Domain ownership

- ResearchQuestion, ResearchGoal, ResearchProject (when needed), ResearchRun/attempt, source acquisition manifest, SourceVersion reference, EvidenceSpan, Finding, ResearchArtifact, ReportVersion, ExperimentPlan and DecisionDraft.
- Canonical Research run state and durable jobs stay inside Research.
- RESEARCH may cache retrieved context for a run and keep historical reports, but **does NOT own cross-domain KB indexes or personal Second-Brain memories**.
- Report claims must link to source version/hash/locator; support status distinguish VERIFIED / UNVERIFIED / CONFLICTED / UNAVAILABLE. Human technical approval is distinct from LLM synthesis.

## Research run example

Question: "For a recoverable Agentic Research workload, how do Microsoft Agent Framework and LangGraph compare?"

Expected flow:
1. Interpret goals and explicit constraints (cost, retry, checkpoint, maintenance, provider capabilities).
2. Build bounded research plan with required evidence.
3. Retrieve trusted technical docs, repository release/issue data and relevant experiments.
4. Extract findings and contradictory evidence linked to exact versions.
5. Compare behavior, API guarantees, trade-offs, failure scenarios.
6. Recommend conditional PoCs, not assert fake benchmark measurements.
7. Produce Research Brief, Source Registry, Evidence Register, Technology Matrix, Risk Analysis, PoC Plan and ADR Draft.
8. Persist artifacts, and optionally **publish approved references** to KB through governed inter-domain workflow.

## Runtime and functional requirements

- One authoritative ResearchRun lifecycle with explicit QUEUED/RUNNING/PARTIAL/COMPLETED/FAILED/CANCEL_REQUESTED/CANCELLED semantics (final transition rules require RES-CORE-01 design).
- Persistent accepted jobs: 202 only after atomic durable commit. Lease/fencing/retry/cancel, bounded queues and provider limits.
- Source acquisition through authorized adapters with SSRF/timeout/resource limits; preserve content hash, fetched version and license.
- Prompt/Context/Loop/Tool/Harness are **engineering responsibilities** within Research, not six mandatory microservices.
- A single primary Agent Framework selected by measured PoC (ADR-0001 references MAF but actual versions/behaviors unverified). No nested duplicate workflow owners.
- Model output is untrusted; validation and citation checks are enforced outside pure prompting.
- Frontend independent; Go Gateway and Rust processor optional for Research standalone.
- Optional KB: deterministic initial ContextBundle lookup or model-invoked read-only Knowledge Tool through one adapter/port, not direct KB SQL.

## Failure & result integrity

- No sources found => honest empty/partial outcome with limitations.
- Provider timeout or KB outage => typed failure/degraded mode, never invent support.
- Evidence contradiction => visible conflict; do not silently merge sources.
- Worker crash => idempotent resume/recovery without double committed artifacts.
- Human can audit source versions, locator, query/decision steps and report version.

## Initial product release

M1 is **technical Research foundation** (fake execution + durable jobs); M2 is first **usable Research alpha** (real sources, evidence, report). KB and Second Brain are not prerequisites for M1/M2.

## Tests and quality

- Domain transitions including cancellation races and terminal states.
- Source provenance (version changes, unavailable/revoked docs, mismatched hashes).
- Golden evidence/citation support cases with negative false-citation samples.
- Cost/time/provider-failure/timeout limits, injection/unsafe URL tests.
- User can navigate report → claim → evidence → source version + locator.

## Exclusions

No automatic code commits, self-training model, uncontrolled scientific skill scripts, self-updating approved ADRs, giant shared memory engine or global orchestrator. Future CODING owns coding workflows.

## Suggested implementation slices

RES-CORE-01 domain model/state machine → RES-APP-01 use cases with fakes → HARNESS-01 minimal policies/ports → RES-API-01 HTTP contract → RES-JOB-01 durable queue/worker → RES-DATA-01 source integrity → RES-AGENT-01 bounded Agent → RES-EVIDENCE-01 reports/citation.

See: ../architecture/ECOSYSTEM_CONTEXT_MAP_V1.md and ../implementation/ENGINEER_LED_DELIVERY_PLAN_V2.md.
