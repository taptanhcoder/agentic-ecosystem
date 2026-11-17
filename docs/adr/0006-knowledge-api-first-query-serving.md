# ADR-0006 — Knowledge API-first, Tool-enabled and Scoped Query Serving

Date: 2026-11-17
Status: **PROPOSED — OWNER APPROVAL REQUIRED**

## Context
The shared KB must be usable independently by humans/apps and as a knowledge retrieval provider to multiple Agent domains. Direct DB access or Agent tools bound to pgvector/GraphRAG internals are unsafe and costly to evolve.

## Decision proposed
- Knowledge API is the stable public inter-domain interface.
- Application services call KB deterministically through KnowledgePort and HTTP/RPC adapters.
- Agent Knowledge Tools are **read-only wrappers** around the same KnowledgePort/API; tools never bypass authorization.
- Query Engine supports pluggable exact/structured, lexical, semantic, hybrid, future relational graph and optional GraphRAG, selected by explicit strategy/budget or validated planner.
- KB returns KnowledgeResult, ContextBundle or optional GroundedAnswer, all with source identity/version/locator and verified access scope.
- Multi-space querying is federated over authorized spaces; caller-supplied scope cannot grant access.
- Publication/revocation are authorized application workflows with idempotency and durable state, not autonomous LLM tools.
- GraphRAG is NOT the storage model: relational graph is an optional representation; GraphRAG is a retrieval/synthesis strategy benchmarked against hybrid baseline.

## Alternatives
- Tool-only KB: couples knowledge to Agent Framework; rejects UI/app clients.
- Direct SQL/graph calls: leaks internals and weakens authorization.
- API with Tool adapters: selected; slightly more adapter work, stable ownership.

## Delivery steps
KB registry → fake scoped Query API → exact/lexical baseline → optional vector/hybrid → per-space ACL/revocation tests → context bundles → RESEARCH tool adapter → multi-space federation → graph/GraphRAG only if benchmark shows value.

## Acceptance / rollout
No cross-space leakage, deterministic no-results, citation/version lineage, no unauthorized LLM input, bounded cost/latency and persisted publication status. No Knowledge service, schema or API is claimed implemented today.
