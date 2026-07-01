"""
Configuración central del proyecto Mercado Central AI.

Todas las rutas y parámetros globales deben definirse aquí.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# -------------------------------------------------------
# Cargar variables de entorno
# -------------------------------------------------------

load_dotenv()

# -------------------------------------------------------
# Información del proyecto
# -------------------------------------------------------

PROJECT_NAME = "Mercado Central AI"

PROJECT_VERSION = "1.0.0"

# -------------------------------------------------------
# Directorio raíz del proyecto
# -------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

# -------------------------------------------------------
# Carpetas del proyecto
# -------------------------------------------------------

SRC_DIR = ROOT_DIR / "src"

LOGS_DIR = ROOT_DIR / "logs"

VECTOR_DB_DIR = ROOT_DIR / "vector_db"

TEMP_DIR = ROOT_DIR / "temp"

TESTS_DIR = ROOT_DIR / "tests"

# -------------------------------------------------------
# Base de Conocimiento
# (Fuera del proyecto Python)
# -------------------------------------------------------

KNOWLEDGE_BASE = (
    ROOT_DIR.parent.parent /
    "03_Knowledge_Base"
)

PDF_DIR = KNOWLEDGE_BASE / "01_PDF_Originales"

TEXT_DIR = KNOWLEDGE_BASE / "02_Texto_Extraido"

CHUNKS_DIR = KNOWLEDGE_BASE / "03_Chunks"

METADATA_DIR = KNOWLEDGE_BASE / "04_Metadata"

EMBEDDINGS_DIR = KNOWLEDGE_BASE / "05_Embeddings"

FAISS_DIR = KNOWLEDGE_BASE / "06_VectorDB"

# -------------------------------------------------------
# API KEY
# -------------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# -------------------------------------------------------
# Configuración RAG
# -------------------------------------------------------

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# -------------------------------------------------------
# Modelo Gemini
# -------------------------------------------------------

GEMINI_MODEL = "gemini-2.5-flash"
