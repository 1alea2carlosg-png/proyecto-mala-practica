"""Controlador: muestra la guía de usuario."""

from pathlib import Path

from flask import Blueprint, abort, current_app, render_template

from ..models import DocsPage

docs_bp = Blueprint("docs", __name__)


@docs_bp.get("/docs")
def index():
    page = DocsPage(Path(current_app.config["DOCS_PATH"]))
    if not page.exists():
        abort(404)
    return render_template("docs.html", content=page.to_html())
