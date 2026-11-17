# SECOND BRAIN Domain v1 — Personal Memory & Engineering Continuity

Status: PRODUCT DESIGN PROPOSAL. Independent from Research and KB; no working implementation is claimed.

## Purpose

An AI Engineer's private, evolving second brain for goals, learning history, technical decisions, experiments and personal working context. Reuse high-quality KB knowledge while keeping personal memory governance distinct.

## Owned capabilities

- Personal Memory Registry: intentional items such as remembered principles, decisions, observations, project contexts and learning goals.
- Decision History: owner-approved ADR decisions, rationale, alternatives and supersession.
- Learning Continuity: concepts studied, open questions, exercises, practice evidence and next tasks.
- Memory Curation: propose, verify, approve, dispute, supersede, redact and delete memories.
- Context Intelligence: select relevant personal history and cite optional KB passages for task-specific ContextBundle.
- Retrieval + timeline: query current memory and past revisions without silently overwriting what the human decided.
- Personal privacy: explicit owner control, workspace scopes, retention and export/deletion strategy.

## Boundary with KB

**KB owns shareable documents, versions and retrieval indexes; SECOND BRAIN owns personal memory semantics and human context**. SB stores knowledge refs and limited private note representations, not a duplicate full copy of KB's source registry. SB may call KB Knowledge API or ask for a ContextBundle; KB must not automatically ingest every personal memory or query an SB DB.

## Boundary with RESEARCH

A Research report/artifact belongs to Research. SB may remember a human-approved decision or lesson referencing that artifact. A new Research run may optionally receive owner-approved project/personal context via its application interface; hidden implicit memory injection is forbidden.

## Memory model candidates

MemoryRecord: id, owner, scope, category, content or reference, provenance, visibility, verification_status, created_at, last_reviewed_at, valid_from/to, superseded_by, delete/retention status.
DecisionRecord: decision, alternatives, rationale, evidence refs, approval status, project context and version.
LearningRecord: topic, competency, evidence of learning, open questions, next action.
Do not label LLM-generated summaries VERIFIED without owner rule/evidence.

## Memory lifecycle (design)

PROPOSED → REVIEWED → APPROVED / REJECTED → ACTIVE → SUPERSEDED / REVOKED / DELETED as applicable. Decide legal transitions and transaction owner during SB-CORE-01. Versioned history is distinct from user-visible deletion/privacy requirements; retention rules require deliberate design.

## Example use case

The engineer researches HNSW, approves a pgvector architecture decision and later asks about GraphRAG. SB finds the prior decision and experiments, queries KB for current authorized material, states which evidence is historical/stale and proposes what should be retested. The engineer approves any new decision.

## Proposed implementation

SB-00 memory privacy/ownership ADR → SB-01 core memory model and lifecycle → SB-02 curated ingestion + decisions → SB-03 personal retrieval and history → SB-04 Knowledge API adapter → SB-05 context assembly with provenance → SB-06 evaluation, forget/revoke, multi-project authorization and recovery.

## Quality gates

- User can inspect what is remembered, source and validity; memory is not silently changed by Agent narrative.
- No cross-person/project leakage; no publication to ecosystem KB without explicit scope and rights.
- Missing KB does not erase personal memories; bounded fallback without fabricated citations.
- KB source revocation invalidates referenced external facts when necessary.
- Duplicate events do not create duplicate memories; conflicting records retain provenance.
- Memory deletion/retention are tested and documented; sensitive content excluded from telemetry.

## Non-goals

Second Brain is not Research, an unbounded LLM chat history dump, a general vector store for every domain or a substitute for KB query service.
