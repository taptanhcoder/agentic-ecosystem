import unittest
from dataclasses import FrozenInstanceError
from agentic_research.application.ports import DocumentProcessor, DocumentText


class DocumentPortTest(unittest.TestCase):
    def test_python_adapter_needs_no_native_engine(self):
        class FakeProcessor:
            def extract(self, content: bytes, *, media_type: str) -> DocumentText:
                return DocumentText(content.decode("utf-8"), media_type)

        processor: DocumentProcessor = FakeProcessor()
        result = processor.extract(b"research", media_type="text/plain")
        self.assertEqual(result.text, "research")
        with self.assertRaises(FrozenInstanceError):
            result.text = "changed"
