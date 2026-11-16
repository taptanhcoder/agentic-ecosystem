"""Validate repository operations docs and non-deployable Compose template."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "docs/ops/README.md",
    "docs/ops/01_REPOSITORY.md",
    "docs/ops/02_GIT_WORKFLOW.md",
    "docs/ops/03_GITHUB_GOVERNANCE.md",
    "docs/ops/04_CI_CD.md",
    "docs/ops/05_DEPLOYMENT.md",
    "docs/ops/06_RELEASE_ROLLBACK.md",
    "docs/ops/07_SECRETS_SECURITY.md",
    "docs/ops/08_OPERATIONS_CHECKLIST.md",
    "docs/adr/0003-repo-git-ci-cd-deployment-policy.md",
    ".github/workflows/ops-validation.yml",
    "deployments/templates/compose.production.yaml",
    "deployments/templates/production.validation.env",
]
errors = []
for name in REQUIRED:
    p = ROOT / name
    if not p.is_file() or not p.read_text(encoding="utf-8").strip():
        errors.append(f"missing/empty: {name}")
for doc in (ROOT / "docs/ops").glob("*.md"):
    text = doc.read_text(encoding="utf-8")
    for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        url = href.split("#", 1)[0]
        if not url or url.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (doc.parent / url).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"broken local link: {doc.relative_to(ROOT)} -> {href}")
template = ROOT / "deployments/templates/compose.production.yaml"
if template.is_file():
    contents = template.read_text(encoding="utf-8")
    if "build:" in contents:
        errors.append("production template must consume immutable images, not build")
    for required_token in ("${RESEARCH_API_IMAGE:?", "${RESEARCH_WORKER_IMAGE:?", "127.0.0.1:"):
        if required_token not in contents:
            errors.append(f"missing deploy safeguard: {required_token}")
if errors:
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(REQUIRED)} required files; ops local links and template safeguards")
