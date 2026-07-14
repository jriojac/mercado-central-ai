
"""
Pruebas unitarias para DocumentMapper.
"""

import pytest

from langchain_core.documents import Document

from src.core.exceptions import InvalidDocumentError
from src.knowledge.document_mapper import DocumentMapper
from src.knowledge.types import VectorDocument


@pytest.fixture
def mapper() -> DocumentMapper:
    """
    Instancia reutilizable del mapper.
    """
    return DocumentMapper()


@pytest.fixture
def sample_document() -> Document:
    """
    Documento válido con embedding.
    """
    return Document(
        page_content="Documento de prueba",
        metadata={
            "source": "test.pdf",
            "page": 1,
            "embedding": [0.1, 0.2, 0.3],
        },
    )


def test_map_documents_returns_vector_documents(
    mapper: DocumentMapper,
    sample_document: Document,
):
    """
    Debe convertir documentos LangChain en VectorDocument.
    """

    result = mapper.map_documents(
        [sample_document]
    )

    assert len(result) == 1

    assert isinstance(
        result[0],
        VectorDocument,
    )


def test_map_documents_preserves_content(
    mapper: DocumentMapper,
    sample_document: Document,
):
    """
    Debe conservar el contenido.
    """

    result = mapper.map_documents(
        [sample_document]
    )

    assert (
        result[0].page_content
        == sample_document.page_content
    )


def test_map_documents_preserves_metadata(
    mapper: DocumentMapper,
    sample_document: Document,
):
    """
    Debe conservar el metadata.
    """

    result = mapper.map_documents(
        [sample_document]
    )

    assert result[0].metadata == {
        "source": "test.pdf",
        "page": 1,
    }

def test_map_documents_preserves_embedding(
    mapper: DocumentMapper,
    sample_document: Document,
):
    """
    Debe conservar el embedding.
    """

    result = mapper.map_documents(
        [sample_document]
    )

    assert (
        result[0].embedding
        == sample_document.metadata["embedding"]
    )


def test_map_documents_generates_id(
    mapper: DocumentMapper,
    sample_document: Document,
):
    """
    Debe generar un identificador.
    """

    result = mapper.map_documents(
        [sample_document]
    )

    assert result[0].id

    assert isinstance(
        result[0].id,
        str,
    )


def test_map_documents_requires_list(
    mapper: DocumentMapper,
):
    """
    Debe validar que la entrada sea una lista.
    """

    with pytest.raises(
        InvalidDocumentError
    ):
        mapper.map_documents(
            "documento"
        )


def test_map_documents_requires_document_instances(
    mapper: DocumentMapper,
):
    """
    Todos los elementos deben ser Document.
    """

    with pytest.raises(
        InvalidDocumentError
    ):
        mapper.map_documents(
            [object()]
        )


def test_map_documents_requires_embedding(
    mapper: DocumentMapper,
):
    """
    El documento debe contener embedding.
    """

    document = Document(
        page_content="Texto",
        metadata={},
    )

    with pytest.raises(
        InvalidDocumentError
    ):
        mapper.map_documents(
            [document]
        )


def test_map_documents_empty_list(
    mapper: DocumentMapper,
):
    """
    Una lista vacía debe devolver una lista vacía.
    """

    result = mapper.map_documents(
        []
    )

    assert result == []
