"""Modelo: lee la guía de usuario en Markdown y la convierte a HTML."""

from dataclasses import dataclass
from pathlib import Path

import markdown


@dataclass
class DocsPage:
    path: Path

    def exists(self) -> bool:
        return self.path.is_file()

    def to_html(self) -> str:
        text = self.path.read_text(encoding="utf-8")
        return markdown.markdown(text, extensions=["tables", "fenced_code"])
