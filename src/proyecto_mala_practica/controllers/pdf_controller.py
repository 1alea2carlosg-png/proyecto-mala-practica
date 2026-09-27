"""Controlador: recibe las peticiones, usa el modelo y elige la vista."""

import io
from pathlib import Path

from flask import Blueprint, abort, current_app, render_template, request, send_file

from ..models import InvalidPdfError, PdfDocument

pdf_bp = Blueprint("pdf", __name__)


def _upload_folder() -> Path:
    return Path(current_app.config["UPLOAD_FOLDER"])


@pdf_bp.get("/")
def index():
    return render_template("index.html")


@pdf_bp.post("/")
def cargar():
    file = request.files.get("pdf")
    if file is None or not file.filename:
        return render_template("index.html", error="Selecciona un archivo PDF."), 400
    try:
        document = PdfDocument.save_upload(file, _upload_folder())
    except InvalidPdfError as exc:
        return render_template("index.html", error=str(exc)), 400
    return render_template(
        "index.html", document=document, pages=document.extract_pages()
    )


@pdf_bp.get("/exportar/<doc_id>")
def exportar(doc_id: str):
    document = PdfDocument.find(doc_id, _upload_folder())
    if document is None:
        abort(404)
    data = io.BytesIO(document.to_txt().encode("utf-8"))
    return send_file(
        data,
        mimetype="text/plain",
        as_attachment=True,
        download_name=document.txt_filename(),
    )
