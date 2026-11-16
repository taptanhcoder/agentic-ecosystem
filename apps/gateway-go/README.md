# Optional thin gateway

Run `go test ./...` and `go vet ./...` here. `go run ./cmd/gateway`
prints scaffold status and exits; it does not listen or proxy requests.
Only standard-library dependencies: no go.sum is needed or fabricated.
Go may consume contracts/openapi/research.v1.json only; no Research DB access,
job lifecycle, workflow planning or Global Orchestrator. HTTP/auth/SSE/OTel
implementation belongs to GO-00. Module path is local placeholder until a remote exists.
