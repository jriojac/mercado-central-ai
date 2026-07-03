"""
Pruebas unitarias del módulo Metadata Manager.

Sprint 5 - Hito 3
Release objetivo: v0.3.0
"""

import pytest
from langchain_core.documents import Document
from src.knowledge.metadata import MetadataManager
from src.core.exceptions import MissingMetadataError
from uuid import UUID

from src.config.settings import PROJECT_VERSION



@pytest.fixture
def manager():
    """
    Devuelve una instancia del MetadataManager.
    """
    return MetadataManager()


@pytest.fixture
def valid_document():
    """
    Devuelve un Document con metadata válida.
    """

    return Document(
        page_content="Texto de prueba",
        metadata={
            "source": r"C:\Documentos\Manual.PDF",
            "file_name": "Manual.PDF",
            "file_type": " PDF ",
            "chunk_index": "0",
            "total_chunks": "1",
            "chunk_size": "100",
            "splitter_version": " 1.0 ",
        },
    )

def test_cp001_process_valid_document(manager, valid_document):
    """
    CP-001
    Verifica que una colección válida de documentos
    pueda procesarse correctamente.
    """

    documents = manager.process_documents([valid_document])

    assert len(documents) == 1


def test_cp002_valid_metadata(manager, valid_document):
    """
    CP-002
    Verifica que un documento con metadata válida
    pase todas las validaciones.
    """

    documents = manager.process_documents([valid_document])

    metadata = documents[0].metadata

    assert metadata["file_type"] == "pdf"
    assert metadata["chunk_index"] == 0
    assert metadata["total_chunks"] == 1
    assert metadata["chunk_size"] == 100


def test_cp003_missing_metadata(manager, valid_document):
    """
    CP-003

    Verifica que una metadata incompleta
    genere MissingMetadataError.
    """

    del valid_document.metadata["file_type"]

    with pytest.raises(MissingMetadataError):
        manager.process_documents([valid_document])

def test_cp004_normalize_metadata(manager, valid_document):
    """
    CP-004

    Verifica la normalización
    de la metadata.
    """

    documents = manager.process_documents([valid_document])

    metadata = documents[0].metadata

    assert metadata["source"] == "C:/Documentos/Manual.PDF"

    assert metadata["file_name"] == "Manual.pdf"

    assert metadata["file_type"] == "pdf"

    assert metadata["chunk_index"] == 0

    assert metadata["total_chunks"] == 1

    assert metadata["chunk_size"] == 100

    assert metadata["splitter_version"] == "1.0"


def test_cp005_enrich_metadata(manager, valid_document):
    """
    CP-005

    Verifica que el MetadataManager
    agregue correctamente la metadata
    enriquecida.
    """

    documents = manager.process_documents([valid_document])

    metadata = documents[0].metadata

    # document_id
    assert "document_id" in metadata

    UUID(metadata["document_id"])

    # ingest_date
    assert "ingest_date" in metadata

    assert metadata["ingest_date"] != ""

    # pipeline_version
    assert metadata["pipeline_version"] == PROJECT_VERSION

    # language
    assert metadata["language"] == "es"

    # category
    assert metadata["category"] is None


def test_cp006_empty_collection(manager):
    """
    CP-006

    Verifica que una colección vacía
    retorne una lista vacía.
    """

    documents = manager.process_documents([])

    assert documents == []


def test_cp007_invalid_collection(manager):
    """
    CP-007

    Verifica que una entrada distinta
    de una lista genere TypeError.
    """

    with pytest.raises(TypeError):
        manager.process_documents("texto")

def test_cp008_invalid_document(manager):
    """
    CP-008

    Verifica que una colección con elementos
    que no sean Document genere TypeError.
    """

    with pytest.raises(TypeError):
        manager.process_documents([1])


def test_cp009_complete_pipeline(manager, valid_document):
    """
    CP-009

    Verifica el flujo completo
    del MetadataManager.
    """

    documents = manager.process_documents([valid_document])

    metadata = documents[0].metadata

    required_fields = {
        "source",
        "file_name",
        "file_type",
        "chunk_index",
        "total_chunks",
        "chunk_size",
        "splitter_version",
        "document_id",
        "ingest_date",
        "pipeline_version",
        "language",
        "category",
    }

    assert required_fields.issubset(metadata.keys())