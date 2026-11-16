# Public contract source

`openapi/research.v1.json` is the single authoritative Research OpenAPI document.
The v2/v3.2 design uses a `.yaml` example; ADR 0002 deliberately retains the
existing JSON source. Do not maintain equivalent hand-written contracts twice.

Current content is a draft liveness endpoint only, not a running API. RD-01 adds
run/error/status contracts. FE-02 generates TypeScript from this document and
adds schema/client compatibility checks. No generated SDK exists yet.

Validate using `uv run --locked python scripts/validate_openapi.py`.
