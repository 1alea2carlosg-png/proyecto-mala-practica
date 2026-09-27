import tempfile
from pathlib import Path

from flask import Flask

from .controllers import docs_bp, pdf_bp

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_PATH = PROJECT_ROOT / "docs" / "como-funciona.md"
UPLOAD_FOLDER = Path(tempfile.gettempdir()) / "proyecto_mala_practica_uploads"


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB
    app.config["DOCS_PATH"] = DOCS_PATH
    app.register_blueprint(pdf_bp)
    app.register_blueprint(docs_bp)
    return app


def main() -> None:
    create_app().run(debug=True)
