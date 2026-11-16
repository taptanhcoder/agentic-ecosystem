"""Validate the authoritative contract using the locked external validator."""
import json
from pathlib import Path
from openapi_spec_validator import validate_spec

path = Path(__file__).resolve().parents[1] / "contracts/openapi/research.v1.json"
validate_spec(json.loads(path.read_text()))
print(f"PASS: {path.name}")
