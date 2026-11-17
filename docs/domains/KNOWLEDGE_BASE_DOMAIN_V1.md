# KNOWLEDGE BASE Domain v1 — Shared Knowledge & Query Intelligence

**Status: PRODUCT / ARCHITECTURE PROPOSAL.** KB is NOT present as working code. Distinct bounded context; may initially deploy on same host/process with strict logical boundaries.

## Mission

A single, shared platform for **ingesting, governing, retrieving and answering over knowledge** independently or for one/many Agent domains. API-first and Tool-enabled. Not just a vector store. Not the owner of operational Research jobs or private personal-memory semantics.

## Two major execution paths

### Knowledge Write Path
Authorized document or domain artifact → verify owner/rights/scope → identity/version/content hash → durable register + ingestion job → parse/normalize → page/section/offset-aware chunks → FTS/vector indexes (optional graph node/edge) → index readiness status.

Write path may be asynchronous. Knowledge publication accepted ≠ already queryable. Idempotent per source/version/publication key. Revocation must be enforced on reads immediately, with index cleanup eventually consistent.

### Knowledge Read / Query Path
Agent/UI/App submits query → authenticate and authorize caller and spaces → parse/query-plan → exact/structured or full-text/vector/hybrid (optional relational graph/GraphRAG) → per-space retrieval → fusion/rerank → recheck access & provenance → evidence, ContextBundle or GroundedAnswer.

KB answers are bounded, cite versions/locators and report uncertainty; no automatic fake answer when there is no support. Query planning starts deterministic; LLM query expansion/answer synthesis is optional.

## Knowledge Spaces and scopes

KnowledgeSpace is the logical namespace with owner, visibility, policies, collections and allowed-purpose metadata:
- Domain-scoped: research, coding, automation, etc.
- Project-scoped: agentic-ecosystem or other private projects.
- Ecosystem-shared: *explicitly published*, curated material.
- Personal/restricted: explicit owner/authorization; do not conflate with Second Brain.

Federated multi-space query combines only authorized spaces. KB must re-check document ACL when retrieving source excerpts; an LLM-provided space id cannot grant access.

## Core aggregate candidates

KnowledgeSpace, KnowledgeCollection, KnowledgeDocument, DocumentVersion, SourceReference, IngestionJob, KnowledgeChunk, EmbeddingRecord (versioned by model), KnowledgeEntity, KnowledgeRelation, KnowledgePublication, KnowledgePolicy. Treat embeddings as derived indexes, not canonical truth.

Provenance: original source domain/object id, license/publishing right, content hash, source document version, parser/chunker/index model versions, chunk locator, timestamp, verification state and supersession/revocation status.

## Query contracts

A single portable KB API serves:
- KnowledgeResult: ranked evidence/document excerpts with source/version/locator/space.
- ContextBundle: token-budgeted, redacted, scope-authorized context for Agent reasoning.
- GroundedAnswer: optional synthesized answer with validated citations and explicitly expressed missing/conflicting evidence.

**Agent Tool is an adapter** that validates arguments and calls KB API; Application may call KB API directly for deterministic initial context. Do not expose raw SQL, unrestricted pgvector or graph traversal to an LLM. Publish/update/revoke are authorized application operations, not default model-initiated tools.

## Retrieval maturity

1. KB MVP: registry + lexical/exact search and provenance + scoped ContextBundle.
2. Add pgvector embeddings/hybrid ranking only after a measured exact baseline; model/version + access scope stored.
3. Add relational graph entities/relations if domain queries need relations. This graph can live in PostgreSQL initially.
4. GraphRAG is a **retrieval/synthesis strategy**, not a replacement for the data model or an inevitable performance win. Benchmark on multi-hop/cross-domain questions against hybrid RAG. Do not install separate graph DB without evidence.
5. Federated query balances per-space relevance/cost/ACL. Keep knowledge space metadata and trace source independent of index vendor.

## KB independence

Knowledge UI/API can create spaces, ingest documents, query and inspect provenance without RESEARCH or SECOND BRAIN running. RESEARCH uses KB when available/approved; KB owns none of Research's runtime.

## Correctness and safety tests

- Cross-space access denial **before ranking** and before model input; no leaked result counts/metadata.
- 404/403 according to disclosure policy; malformed filters; no-result correctness.
- Publication retries, duplicate sources, version changes, stale cache, document revocation, orphan cleanup.
- Input size/time bounds, URL SSRF, malicious document prompt injection and safe tool output.
- Recall@K, citation validity, retrieval latency, query cost, multi-space fairness, index rebuild.
- KB unavailable: consumer failure/degraded policy explicit. Trace without content/secret leakage.

## Non-goals for KB MVP

No globally trusted LLM memory, autonomous external tool execution, mandatory GraphRAG, graph DB microservice, real-time indexing SLA without measurement or single global mutable cache for all domains.

## Implementation sequence

KB-00 contracts/ownership → KB-01 Space/Document registry → KB-02 fake scoped query + API → KB-03 FTS/exact retrieval → KB-04 context bundle/version provenance → KB-05 Research integration (read + authorized publication) → KB-06 hybrid/vector benchmark → KB-07 federated/relational graph/GraphRAG only based on workload and tests.

Related: ../architecture/CROSS_DOMAIN_CONTRACTS_V1.md; ../adr/0006-knowledge-api-first-query-serving.md.
