# ADR-0005 — Independent Research, Knowledge and Second Brain Contexts

Date: 2026-11-17
Status: **PROPOSED — OWNER APPROVAL REQUIRED**
Supersession: Intended to refine ADR-0001 and older Research Memory/product plans. No existing accepted ADR is automatically superseded.

## Context
The ecosystem originally proposed Research-first and embedded long-term research memory. The owner now requires an independent shared Knowledge Base that can both store **and query/serve** knowledge for single/multiple Agent domains, plus an independently evolving Second Brain for personal learning and decision continuity. A single shared DB or global Agent runtime would create excessive coupling.

## Decision proposed
- RESEARCH owns investigation runs, source/evidence versions and reports; no canonical shared knowledge or personal memory store.
- KB owns KnowledgeSpaces, ingestion, documents/versions/registry/indexes, structured/hybrid/optional graph and federated query serving, access control and context bundles.
- SECOND BRAIN owns personal memory records, learning/decision continuity and owner-approved curation; uses KB as authorized knowledge reference/query service.
- CORE HARNESS LITE supplies reusable technical execution contracts only, not global workflow business state.
- Integration uses versioned APIs, events and artifact references. Each domain owns its own database schema/roles and business state, even on a shared Postgres instance.
- Research is **implemented and released first**, independently of KB/SB. KB then ships standalone Query MVP; only then integrate RESEARCH↔KB and build SB.

## Alternatives
1. Embed KB+SB in RESEARCH — lower initial module count, fails independent cross-domain ownership.
2. Make KB store personal memory and long-term decisions as owner of all data — reduced domains but confuses user-memory governance and knowledge indexing.
3. Separate contexts with thin contract boundaries — selected for long-term clarity, costs extra API/auth/version work.

## Consequences
Explicit cross-domain auth, eventual consistency and source ownership; easier domain evolution and standalone testing. Must control operational complexity; bounded contexts may initially deploy in one process/host without shared direct data access.

## Approval / migration work
Owner reviews, approves or revises this ADR. Only then update old plan references, Research Memory endpoints/ownership and new public contracts through separate task tickets. No DB/data migrations now.

## Verification
Architecture fitness tests against cross-domain imports/SQL, mock KB outage during Research, publication idempotency and Second-Brain scoped context tests once implemented.
