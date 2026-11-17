# Agentic AI Ecosystem — Engineering Documentation Hub

> **2026-11-17 • Documentation baseline / proposal, not software release.**
> Repo: https://github.com/taptanhcoder/agentic-ecosystem
> Working model: Solo Engineer owns code, Codex reads/reviews/audits/verifies on request.

## Start here (Codex + human)

1. Root [AGENTS.md](../AGENTS.md) — mandatory agent permissions, precedence and invariants.
2. [Codex Operating Contract](codex/OPERATING_CONTRACT.md) — read-only default, allowed hints/review flow.
3. [Context Map](architecture/ECOSYSTEM_CONTEXT_MAP_V1.md) — four boundaries, data ownership and integration.
4. [Build & Release Plan v2](implementation/ENGINEER_LED_DELIVERY_PLAN_V2.md) — dependency-driven sequence, tickets, evidence gates.
5. [First Week Mission](codex/FIRST_WEEK_MISSION.md) — safe starting tasks.
6. Domain-specific spec, public contracts and actual source/test code for the current ticket.

## Product domain design

| Document | Primary purpose | Status |
| --- | --- | --- |
| [RESEARCH](domains/RESEARCH_DOMAIN_V2.md) | AI Engineering Research & Decision Intelligence | PRODUCT PROPOSAL |
| [KNOWLEDGE BASE](domains/KNOWLEDGE_BASE_DOMAIN_V1.md) | Shared knowledge ingest **and querying** for one/multiple agents | PRODUCT PROPOSAL |
| [SECOND BRAIN](domains/SECOND_BRAIN_DOMAIN_V1.md) | Independent personal memory and decision continuity | PRODUCT PROPOSAL |
| [Core Harness Lite](architecture/CORE_HARNESS_V1.md) | Minimal reusable agent execution capabilities | ARCHITECTURE PROPOSAL |
| [Cross-domain Contracts](architecture/CROSS_DOMAIN_CONTRACTS_V1.md) | API-first/tool-enabled knowledge publication & queries | CONTRACT DESIGN, NOT IMPLEMENTED |

## Governance, ADR and engineering tasks

- [ADR-0005 proposed: ecosystem contexts and ownership](adr/0005-ecosystem-bounded-contexts.md)
- [ADR-0006 proposed: KB API-first and Tool-enabled](adr/0006-knowledge-api-first-query-serving.md)
- [ADR-0007 proposed: Engineer-led development rules](adr/0007-engineer-led-codex-collaboration.md)
- [Document reconciliation matrix](implementation/DOCUMENT_RECONCILIATION.md)
- [Codex Task/Review Templates](codex/TASK_AND_REVIEW_TEMPLATES.md)

Existing accepted ADR-0001 (Research boundaries), ADR-0002 (TypeScript/React frontend) and ADR-0004 (dev/main Git workflow) **remain authoritative until deliberately superseded**. Existing ADR-0003 operations policy is proposed. New docs must not override accepted records automatically.

## Verified baseline versus future design

The inspected GitHub dev source (2026-11-17) includes a Python Research package skeleton and document Protocol, Go gateway stub, Rust document-core stub, a draft OpenAPI with only /health/live, tests, and CI definitions. At that snapshot there is **no functioning Research API/Worker, KB Domain, Second Brain, shared Harness runtime, live GraphRAG, UI application or production release**.

[PROJECT_STATUS.md](PROJECT_STATUS.md) and [SETUP_BASELINE.md](SETUP_BASELINE.md) include dated local checks and historical notes. Do not infer today's local toolchain status from them. GitHub-hosted CI/deployment evidence must be independently inspected.

## Naming and precedence

1. Observed repository code, current tests, pinned manifests and executed logs establish **implementation facts**.
2. Accepted ADRs and published versioned contracts establish decisions.
3. This proposal set establishes **design intent pending approval**; it does not silently supersede accepted ADRs.
4. Status ledger records dated evidence; older plans provide historical rationale only.
5. If documents conflict, open an explicit resolution issue or ADR; do not reinterpret a conflict as permission to rewrite code.

Version naming: The old Master Plan v2 used R0 for an end-to-end useful research demo; the engineer-led plan uses R0 for durable execution foundation. For coordination **use explicit milestone names M0–M6**, never an unqualified R0/G0 when referring to acceptance. Proposed version tags do not imply deployed releases.

## Policy on changing docs

Owner approves product/business boundaries and accepted ADR changes. Codex can prepare docs when asked, but must not edit application source, dependencies, CI, production settings or issue state without scoped approval. Link verified tests from actual runs; no invented performance numbers, service endpoints or deployed URLs.

## Historical engineering exercises

[Build Roadmap v1](implementation/ENGINEER_LED_BUILD_ROADMAP_V1.md) preserves detailed
learning exercises. Its ordering and ownership assumptions are historical; use
Delivery Plan v2 for coordination and accepted ADRs for decisions.
