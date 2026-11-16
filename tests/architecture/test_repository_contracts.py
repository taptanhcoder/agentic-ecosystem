"""Repository boundaries shared by the backend and future frontend."""
import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


def frontend_imports(source):
    forbidden = ('apps.web', 'apps.research_web', 'packages.frontend')
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names = [item.name for item in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = ['.'.join(filter(None, (node.module, item.name))) for item in node.names]
        else:
            continue
        found.extend(name for name in names
                     if any(name == prefix or name.startswith(prefix + '.')
                            for prefix in forbidden))
    return found


class RepositoryContracts(unittest.TestCase):
    def test_research_package_has_no_frontend_imports(self):
        for path in (ROOT / 'domains/research/src').rglob('*.py'):
            with self.subTest(path=path):
                self.assertEqual(frontend_imports(path.read_text()), [])

    def test_frontend_import_guard_handles_both_import_forms(self):
        for source in ('import apps.web', 'from apps import web',
                       'from packages.frontend import client',
                       'import apps.research_web.routes'):
            with self.subTest(source=source):
                self.assertTrue(frontend_imports(source))
        self.assertEqual(frontend_imports('from agentic_research.application import ports'), [])

    def test_single_authoritative_research_contract(self):
        contracts = sorted(path.name for path in (ROOT / 'contracts/openapi').glob('research.v1.*')
                           if path.suffix in {'.json', '.yaml', '.yml'})
        self.assertEqual(contracts, ['research.v1.json'],
                         'Keep one authoritative contract; update ADR and consumers for a migration.')
