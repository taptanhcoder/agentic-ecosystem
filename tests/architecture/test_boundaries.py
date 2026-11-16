"""Static import fitness checks, including relative imports."""
import ast
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "domains/research/src"


def violations(source, module, layer):
    allowed = {"domain": ("agentic_research.domain",),
               "application": ("agentic_research.domain", "agentic_research.application"),
               "agentic": ("agentic_research.domain", "agentic_research.application", "agentic_research.agentic")}[layer]
    errors = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            name = node.module or ""
            if node.level:
                name = importlib.util.resolve_name("." * node.level + name, module)
            names = [name + "." + a.name for a in node.names]
        else:
            continue
        for name in names:
            if name.split(".")[0] in sys.stdlib_module_names:
                continue
            if any(name == a or name.startswith(a + ".") for a in allowed):
                continue
            errors.append(name)
    return errors


class Boundaries(unittest.TestCase):
    def test_source_imports(self):
        for layer in ("domain", "application", "agentic"):
            for path in (SRC / "agentic_research" / layer).rglob("*.py"):
                package = ".".join(path.relative_to(SRC).parts[:-1])
                with self.subTest(path=path):
                    self.assertEqual(violations(path.read_text(), package, layer), [])

    def test_guard_rejects_framework_and_adapter_leaks(self):
        for source in ("import fastapi", "from sqlalchemy import select",
                       "from ..adapters import database", "from agentic_research import adapters"):
            with self.subTest(source=source):
                self.assertTrue(violations(source, "agentic_research.application", "application"))

    def test_guard_accepts_domain_and_standard_library(self):
        self.assertEqual(violations("from ..domain import entity\nfrom typing import Protocol",
                                    "agentic_research.application", "application"), [])

    def test_no_global_orchestrator(self):
        self.assertFalse((ROOT / "platform/orchestrator").exists())
