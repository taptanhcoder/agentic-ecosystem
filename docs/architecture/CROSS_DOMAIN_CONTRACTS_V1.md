# Cross-Domain Knowledge & Context Contracts v1 — Design Notes

Status: PROPOSED; JSON below is **illustrative**, not a committed OpenAPI implementation or generated SDK.

## 1. Integration rule: API-first, Tool-enabled

- KB exposes versioned Knowledge API as domain-agnostic transport.
- Application code calls KB via KnowledgePort → KnowledgeAPIAdapter for deterministic workflow steps.
- Agents call KnowledgeSearchTool / KnowledgeContextTool → the same KnowledgePort/API when a model chooses a read-only query.
- Avoid low-level tools such as direct_sql, pgvector_search or unrestricted graph_query available to Agent LLMs.
- Write operations (publish, update, revoke) are application commands/events, not default autonomous agent tools.
- Optional MCP adapter only if external MCP clients appear; it must wrap KB API rather than own another knowledge store.

## 2. API candidates (proposed namespace only)

| Method/path | Purpose | Durability/auth |
| --- | --- | --- |
| POST /api/v1/knowledge/query | Scoped retrieval, hybrid/optional graph/federated | Auth + per-space ACL, bounded timeout |
| POST /api/v1/knowledge/context-bundles | Token-bounded evidence/context package | Auth + policy, source/citation IDs |
| GET /api/v1/knowledge/documents/{id} | Versioned document/locator lookup | Re-check ACL on resource |
| POST /api/v1/knowledge/ingestions | Async file/source ingest | Persistent accepted-job receipt |
| GET /api/v1/knowledge/jobs/{id} | Ingest/index status | Authorized job scope |
| POST /api/v1/knowledge/publications | Domain artifact publication | Idempotency, owner policy, durable intent |
| POST /api/v1/knowledge/publications/{id}/revoke | Authorized revocation | Revocation visible before async index cleanup |

No route above exists in source at current snapshot. Do not hand-code DTOs without approving the canonical OpenAPI.

## 3. KnowledgeQuery contract (illustration)

```json
{
  "question": "Which decisions govern workflow recovery?",
  "purpose": "architecture_review",
  "scope": {
    "space_ids": ["kb.project.agentic-ecosystem", "kb.shared.architecture"]
  },
  "response_mode": "evidence",
  "top_k": 8,
  "token_budget": 3000,
  "require_provenance": true
}
```

Trusted caller identity, role, allowed space list and project scopes are resolved from validated authorization context, **not** blindly trusted as user/model-supplied arguments.

KB must return stable knowledge IDs, source IDs/version/locator, provenance and verification status. Similarity scores are ranking signals, not calibrated probabilities. A grounded answer is only supported by verified returned evidence, and may explicitly say no support found.

## 4. Tool surface

Read-only Tool capabilities:
- knowledge_search(question, hints?, limit?) → KnowledgeResult
- knowledge_get_context(question, budget?) → ContextBundle
- knowledge_get_document(reference) → resource metadata/authorized excerpt

Wrapper enforces: allowlist, scoped identity from runtime, max tokens/k, timeouts, structured schema checking, citations, error classification and redaction. The Tool cannot extend the caller's permissions, even if the LLM provides extra space_ids.

## 5. Publication and eventual consistency

1. Research stores a completed artifact in its own persistence.
2. A human or authorized policy approves publication; Research writes the outbox intention transactionally with its own state update.
3. Publication worker sends artifact reference/content permitted for sharing with unique publication idempotency key.
4. KB verifies source, rights, scope and version; persists document registration and indexing job.
5. KB returns RECEIVED/INDEXING/READY or FAILED; indexes update asynchronously.
6. RESEARCH must not equate accepted publication with query-visible knowledge.
7. Revocation must block visibility at authorization/query time immediately; asynchronous removal of embeddings/caches can follow verified cleanup policy.

Contracts require retries and duplicate delivery handling; no distributed two-phase transaction assumption.

## 6. Failure and error vocabulary

| Situation | Domain response |
| --- | --- |
| No matching evidence | Completed query, empty results and limitations |
| Unauthorized space/doc | 403/404 according to resource-disclosure policy, no leaked metadata |
| Invalid scope/schema | 400/422 |
| Query budget/provider exhausted | Bounded 429/503 or typed capacity error |
| KB unavailable | Tool failure; Research policy decides degrade/fail, no fabricated context |
| Index pending | Explicit not-ready or older-version policy; never pretend current |
| Revoked document referenced | Exclude from answer and invalidate cached result |
| Network retry repeats publication | Same publication key produces one logical KB document/version |

## 7. Multi-domain isolation

A multi-space search is **federated over authorized Spaces**. ACL filtering precedes retrieval/rerank/LLM input, plus resource re-authorization on delivery. No cross-domain direct DB access. Preserve source Space/version in result fusion; avoid one Space monopolizing top-k; evaluate space-specific recall.

## 8. Evidence

Every retrieved citation requires (source_id, source_version/hash, locator, access/verification status). LLM-generated citation strings without matching registered references fail validation. Record query strategy, model/index version, latency and errors without raw documents/personal memory in traces by default.

## 9. Contract versioning

Research OpenAPI JSON remains authoritative for Research only. KB receives its own future approved knowledge.v1.json and Second Brain its own future contract; do not create these files until the owner starts those implementation tickets. Avoid duplicate JSON/YAML serializations.

## 10. Acceptance tests for future API

Contract consumer fake, schema malformed/unknown fields, authorization before scoring, cross-space access denial, no-result, source/version change, revocation and cached result invalidation, duplicate publication, KB outage, tight token budget, latency/cost limit and no direct DB calls from other domains.
