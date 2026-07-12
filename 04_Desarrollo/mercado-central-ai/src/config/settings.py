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

PROJECT_VERSION = "0.5.0-dev"

# -------------------------------------------------------
# Directorio raíz del proyecto
# -------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

# -------------------------------------------------------
# Carpetas del proyecto
# -------------------------------------------------------

SRC_DIR = ROOT_DIR / "src"

LOGS_DIR = ROOT_DIR / "logs"

DATA_DIR = ROOT_DIR / "data"

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

VECTOR_STORE_DIR = KNOWLEDGE_BASE / "06_VectorDB"

# -------------------------------------------------------
# API KEY
# -------------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# -------------------------------------------------------
# Configuración RAG
# TEXT SPLITTER
# -------------------------------------------------------

TEXT_SPLITTER = {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "separators": [
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ],
    "version": "1.0"
}

# -------------------------------------------------------
# Metadata Manager
# -------------------------------------------------------

DEFAULT_LANGUAGE = "es"

DEFAULT_CATEGORY = None

# ==========================================================
# GEMINI
# ==========================================================

GEMINI_MODEL = "gemini-2.5-flash"

# ==========================================================
# LLM
# ==========================================================

LLM_PROVIDER = "google"

GEMINI_TEMPERATURE = 0.2

GEMINI_MAX_OUTPUT_TOKENS = 2048

GEMINI_TIMEOUT = 30

GEMINI_MAX_RETRIES = 3

# ==========================================================
# EMBEDDINGS
# ==========================================================

EMBEDDING_PROVIDER = "google"

EMBEDDING_MODEL = "gemini-embedding-2-preview"

EMBEDDING_BATCH_SIZE = 32

EMBEDDING_TIMEOUT = 30

EMBEDDING_RETRIES = 3

# ==========================================================
# VECTOR DATABASE
# ==========================================================

VECTOR_DB_PROVIDER = "chroma"

VECTOR_DB_PATH = DATA_DIR / "chroma"

VECTOR_DB_COLLECTION = "mercado_central_ai"

VECTOR_SEARCH_K = 4

# ==========================================================
# RETRIEVER
# ==========================================================

RETRIEVER_TOP_K = 4

RETRIEVER_VALIDATE_QUERY = True


# ==========================================
# Context Builder
# ==========================================

# Separador utilizado entre documentos del contexto.
CONTEXT_SEPARATOR = "\n\n----------------------------------------\n\n"

# Longitud máxima permitida para el contexto consolidado.
MAX_CONTEXT_CHARS = 12_000

# Indica si el Context Builder debe incluir metadatos de los documentos.
INCLUDE_METADATA = False