UV ?= uv
.PHONY: bootstrap python architecture contract go rust check
bootstrap:
	$(UV) sync --locked --all-packages
python:
	$(UV) run --locked python -m unittest discover -s domains/research/tests -v
architecture:
	python3 -m unittest discover -s tests/architecture -v
contract:
	$(UV) run --locked python scripts/validate_openapi.py
go:
	cd apps/gateway-go && go test ./... && go vet ./...
rust:
	cd engines/document-rs && cargo test --locked --workspace && cargo fmt --all -- --check
check: python architecture contract go rust
