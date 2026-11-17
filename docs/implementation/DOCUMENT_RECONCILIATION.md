# Document Reconciliation — Historical Plans vs Proposed Four-Context Design

Status: REVIEW MATRIX, 2026-11-17. Do not silently rewrite accepted ADRs or the source. These are changes to **product direction** pending owner approval.

| Document / statement | Existing state | New direction / action | Authority |
| --- | --- | --- | --- |
| ADR-0001 — Research owns business state; Go/Rust optional | ACCEPTED | Preserve. Add KB/SB contexts without changing Research state owner. | Existing accepted |
| ADR-0001 — MAF named outbound runtime adapter | ACCEPTED direction, not tested SDK | Preserve until comparative PoC and explicit approved supersession; don't install speculatively. | Existing accepted + TECH validation |
| ADR-0002 — TypeScript/React frontend boundary | ACCEPTED design, no FE code yet | Preserve unless owner approves new ADR. Later proposals describing FE as OPEN do not override it. | Existing accepted |
| ADR-0003 — ops policy | PROPOSED | Preserve and use under ops review; Git branch specifics refined by 0004. | Proposed |
| ADR-0004 — dev/main with feature PRs | ACCEPTED | Preserve; no PR directly into main for task branches. | Existing accepted |
| Master Plan v2 — first release includes fully useful Research | Historical target | Adopt named M1 Technical Foundation and M2 Useful Research; avoid ambiguous "R0". | New proposed release plan |
| Master Plan v2 — only Research domain in Release 1 | Historical product scope | Keep first executable slice standalone Research; KB and SB are **separate later releases**. | New proposed milestone plan |
| RD-08 / POST /api/v1/research/memory/search | Planned, not implemented | Split research-local run artifacts from KB knowledge query and SB personal memory; remove cross-domain global memory from Research design after ADR approval. | Proposed ADR-0005 |
| Some target architecture references research.v1.yaml | Historic illustration | Preserve implemented contract: contracts/openapi/research.v1.json; no duplicate YAML. | Code + ADR-0001 |
| Earlier plan calls KB "storage" | Incomplete product description | KB owns ingestion **and Knowledge Query serving** for domain, multi-domain and standalone use. | Proposed ADR-0006 |
| Knowledge Graph vs GraphRAG | Often conflated in prose | Relational node/edge schema is storage/representation; GraphRAG is optional retrieval/synthesis strategy, benchmarked vs hybrid baseline. | Proposed KB design |
| Second Brain embedded inside Research | Earlier product framing | Second Brain independent personal memory domain; Research retains its operational state/artifacts. | Proposed ADR-0005 |
| Core Harness built before domains | Speculative | Define minimum interfaces early; implement with Research and extract after a second consumer; not a Global Orchestrator. | Proposed Core Harness |
| Agent coding autonomously | User rejected vibe coding | Human writes all source/tests; Codex read-only coach/reviewer by default. | Current user working policy |

## Pending owner decisions (do not assume)

- Approve/revise proposed ADR-0005, 0006, 0007.
- Research Agent Framework choice and exact model/profile after PoC.
- Whether to supersede the accepted TypeScript/React FE ADR.
- KB relational graph vs dedicated DB after workload/benchmark.
- User memory retention/access policies and deletion semantics.
- Future global orchestration need — only after real multi-domain workflow evidence.

## Required follow-up after approval

1. Owner approves/revises each ADR and records accepted status.
2. Update docs/implementation/ROADMAP.md and historical-plan pointers **without deleting the historical plan**.
3. Create dedicated implementation tickets; only create contracts/source when corresponding work starts.
4. Add architecture tests before changing cross-domain imports/DB access.
5. Update docs/PROJECT_STATUS.md from observed code/CI facts, not design.
