"""Modelo: guarda los PDF subidos y extrae su texto."""

import re
import uuid
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

_ID_PATTERN = re.compile(r"^[0-9a-f]{32}$")


class InvalidPdfError(Exception):
    """El archivo subido no es un PDF válido."""


@dataclass
class PdfDocument:
    id: str
    path: Path
    name: str

    @classmethod
    def save_upload(cls, file: FileStorage, folder: Path) -> "PdfDocument":
        """Guarda el PDF subido y devuelve el documento, o lanza InvalidPdfError."""
        original = file.filename or ""
        if not original.lower().endswith(".pdf"):
            raise InvalidPdfError("El archivo debe tener extensión .pdf")

        folder.mkdir(parents=True, exist_ok=True)
        doc_id = uuid.uuid4().hex
        name = secure_filename(original) or "documento.pdf"
        path = folder / f"{doc_id}__{name}"
        file.save(path)

        document = cls(doc_id, path, name)
        try:
            document.extract_pages()
        except (PdfReadError, ValueError) as exc:
            path.unlink(missing_ok=True)
            raise InvalidPdfError("No se pudo leer el PDF") from exc
        return document

    @classmethod
    def find(cls, doc_id: str, folder: Path) -> "PdfDocument | None":
        """Busca un PDF subido previamente por su id."""
        if not _ID_PATTERN.match(doc_id):
            return None
        for path in folder.glob(f"{doc_id}__*"):
            return cls(doc_id, path, path.name.split("__", 1)[1])
        return None

    def extract_pages(self) -> list[str]:
        """Devuelve el texto de cada página del PDF."""
        reader = PdfReader(self.path)
        return [(page.extract_text() or "").strip() for page in reader.pages]

    def to_txt(self) -> str:
        """Devuelve todo el texto del PDF, separado por página."""
        pages = self.extract_pages()
        return "\n\n".join(
            f"--- Página {number} ---\n{text}"
            for number, text in enumerate(pages, start=1)
        )

    def txt_filename(self) -> str:
        stem = re.sub(r"[^0-9A-Za-z-]+", "_", Path(self.name).stem).strip("_")
        return f"{stem or 'documento'}.txt"
