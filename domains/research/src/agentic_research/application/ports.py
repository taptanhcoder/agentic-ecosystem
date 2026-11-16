"""Document processing boundary; adapters are implemented in RD-04/RUST-00."""
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class DocumentText:
    text: str
    media_type: str


class DocumentProcessor(Protocol):
    def extract(self, content: bytes, *, media_type: str) -> DocumentText:
        """Extract text under adapter-enforced input/resource limits."""
        ...
