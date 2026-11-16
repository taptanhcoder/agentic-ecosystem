# AUD-00 — Setup baseline

Date: 2026-11-16, Asia/Saigon. Scope: read-only code audit; only this report and
PROJECT_STATUS.md are written. No installs, scaffolding, refactors, services,
migrations or new features. Smoke commands may generate ordinary build caches.

## Authority and reading order

Read handoff AGENTS.md → AI_AGENT_ENGINEERING_GUIDE.md → PROJECT_STATUS.md →
IMPLEMENTATION_BACKLOG.md → actual repo ADRs 0001/0002 → handoff REFERENCE_MAP.md
→ actual contracts/source/manifests/tests. The first four and REFERENCE_MAP are
absent in this repo (PROJECT_STATUS is created by this audit). The active guide
is the user-supplied file in:
`C:/Users/Nghia/Downloads/AGENTIC_ECOSYSTEM_CODING_AGENT_HANDOFF_V1/docs/AI_AGENT_ENGINEERING_GUIDE.md`.
It is used as requested, not bulk-copied. Source instruction conflicts are recorded
below rather than silently resolving architecture during an audit.

## Repository and components

`git rev-parse --show-toplevel`: /mnt/d/ai_agent. Branch main. HEAD verification
fails (no commits). `git status --short`: pre-existing files untracked.
`git remote -v`: empty. Preserve this work; no usable committed rollback base.

| Area | Observed implementation | Classification |
| --- | --- | --- |
| Python Research | Package + empty domain module + DocumentText/DocumentProcessor protocol | VERIFIED scaffold only |
| API | OpenAPI 3.0.3, version 0.0.0, draft /health/live only; no server | PROPOSED runtime |
| Go gateway | main prints scaffold message and exits, no HTTP proxy | VERIFIED compile only |
| Rust | Empty document-core crate, unsafe forbidden; no parser/FFI | IMPLEMENTED_UNVERIFIED this audit |
| Frontend | No app/package manifest/UI | PROPOSED; technology OPEN |
| DB/jobs | No migrations, repositories, queue, worker or runtime configuration | PROPOSED |
| MAF/model/skills | No dependencies or adapters | PROPOSED |
| Observability | Environment placeholders; no SDK/collector integration | PROPOSED |
| CI | Six jobs, path filters, independent architecture job | IMPLEMENTED_UNVERIFIED hosted execution |
| Provenance/memory/evaluation | No evidence pipeline, retrieval, golden corpus | PROPOSED |

## Commands and actual evidence

- `python3 --version`: Python 3.12.3.
- `python3 -m unittest discover -s tests/architecture -v`: PASS, 7 tests.
- `.venv/bin/python -m unittest discover -s domains/research/tests -v`: PASS, 1 fake-adapter test.
- `.venv/bin/python scripts/validate_openapi.py`: PASS; validates draft schema only.
- `'/mnt/c/Program Files/Go/bin/go.exe' -C D:/ai_agent/apps/gateway-go test ./...`:
  PASS compilation, output `[no test files]`. Current version not remeasured;
  previous audit reported Windows Go 1.26.10, not assumed reverified.
- `docker info --format '{{.ServerVersion}}'`: 29.9.2; daemon reachable now.
- `docker ps --format '{{.Names}} {{.Image}} {{.Status}}'`: existing cloudgo frontend,
  backend, dashboard, dind, embedder and pgvector:pg16 containers. Association with
  this repository UNKNOWN; not queried, changed, restarted or treated as Research
  integrations. Database extension/version/schema/credentials not verified.
- PATH inspection: python3 and docker available; uv, Linux Go, rustc, cargo, cc absent.
  Prior temporary `/tmp/eco-cargo/bin/cargo` and uv executable no longer exist.
- Rust tests/check/fmt: NOT RUN this audit; cargo unavailable. Prior missing-cc
  failure is historical, not a current Rust test result.
- uv lock validation: NOT RUN (uv unavailable); manifest/lock contents read only.
- Hosted CI, API/DB integration, frontend, framework/model, recovery, security/load,
  parser parity, coverage percentage and quality benchmarks: NOT RUN.

## Dependency versions

Python manifests require >=3.12,<3.13, no runtime dependencies. Dev validator
pinned 0.7.2; build backend hatchling 1.27.0. Go module declares 1.23.0, standard
library only (no go.sum). CI chooses Go 1.23.6; local baseline differs. Rust
rust-toolchain pins 1.85.0/rustfmt; crate edition 2021, rust-version 1.85, no
external dependencies. Cargo.lock contains only document-core 0.0.0.
The following are lockfile versions, not a claim that every package was runtime-tested:

- `agentic-ecosystem==0.0.0`
- `agentic-research==0.0.0`
- `attrs==26.1.0`
- `certifi==2026.10.23`
- `charset-normalizer==3.5.2`
- `idna==3.20`
- `jsonschema==4.26.0`
- `jsonschema-path==0.3.4`
- `jsonschema-specifications==2025.9.1`
- `lazy-object-proxy==1.13.0`
- `openapi-schema-validator==0.6.3`
- `openapi-spec-validator==0.7.2`
- `pathable==0.4.4`
- `pyyaml==6.0.3`
- `referencing==0.36.2`
- `requests==2.34.2`
- `rfc3339-validator==0.1.4`
- `rpds-py==2026.9.1`
- `six==1.17.0`
- `typing-extensions==4.16.0`
- `urllib3==2.8.0`

## Coverage limits and deviations

1. Seven architecture tests cover static Python imports, forbidden global
   orchestrator path and duplicate OpenAPI serialization. They do not validate
   dynamic imports, runtime authorization, SQL ownership or cross-language calls.
2. Python fake adapter demonstrates immutable output and port use, not parsing.
   Go has no tests; Rust has no parser behavior. No measured coverage percentage.
3. ADR 0002/README/local guide/old roadmap assume React/TypeScript; active guide
   makes frontend OPEN (templ/htmx candidate, Leptos alternative, React exception).
   Record a superseding ADR in a later approved change; no frontend exists to migrate.
4. Old R0 means research output; active guide R0 is durable foundation, R1 useful
   Research, R2 operational ecosystem. Old ticket IDs/status cannot be reused
   without mapping. No release gate passed by these scaffold checks.
5. Existing JSON OpenAPI remains valid single authority. Target YAML illustrations
   do not require duplicate contracts. Current document port lacks page/section/
   offsets and parser version; evolve with a real parser use case and parity tests.
6. Missing in-repo operating guide/backlog/AGENTS makes future onboarding depend
   on the external bundle. Documentation reconciliation is pending, not performed.
7. Missing toolchain reproducibility and no Git commit/remote limit reproducible
   builds/rollback. Existing Docker services must not be assumed owned by this repo.

## Proposed next ticket — TECH-01A: bounded model/runtime feasibility

Status: PROPOSED, not started; first bounded portion of handoff TECH-01.

Objective: compare one direct model call against one MAF plan → read-only fake
tool → structured result on the same fixture, recording actual failures and costs.
Prerequisites: select/verify model endpoint, model identifier, local/remote policy,
resource budget and existing configuration without dumping credentials. No verified
model profile exists here; do not install or call a provider until resolved.

Allowed files: experiments/tech-01/{pyproject.toml,uv.lock,README.md,probe.py,tests/},
docs/benchmarks/TECH-01.md, docs/adr/ADR-runtime.md, PROJECT_STATUS.md/backlog when
available. Existing domain, public contract and root runtime dependencies unchanged.
Use an isolated experiment; MAF and alternatives are comparisons, never nested
owners of one Research Run. Full frontend/parser/queue gates remain separate.

Acceptance: exact tested versions/model/hardware; validated structured output;
allowlisted deterministic tool invocation; invalid schema/tool failure handling;
bounded timeout/cancellation; checkpoint interruption/recovery evidence or explicit
FAIL/unsupported result. Compare identical inputs against direct SDK; no fabricated
latency or blanket G0 approval. Redact prompts/secrets in recorded telemetry.

Tests: isolated unit fixtures for schema/tool validation and budget exhaustion;
opt-in real-provider smoke; bounded interruption/restart case; rerun existing
Python architecture/unit/OpenAPI checks. Commands are to be fixed after dependency
selection, not invented API calls. No test for this ticket has run.

Risks: unavailable/incompatible local model, VRAM contention, API charges/data
export, SDK/checkpoint churn. Prefer local fixture and one active probe, hard
budgets, no autonomous external tools. Remote use requires explicit configured policy.
Rollback: remove only newly introduced experiment files and its environment;
restore only ticket-owned doc edits from captured pre-edit copies. No DB migrations,
root lock changes or git reset/clean. Existing uncommitted files must be preserved.

AUD-00 is complete as an inventory with explicit unknowns, not setup/G0 approval.
