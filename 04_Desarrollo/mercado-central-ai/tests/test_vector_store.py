"""
==============================================================
TEST-005
Vector Store (ChromaDB)

Pruebas unitarias del proveedor de Vector Store.
==============================================================
"""

import pytest

from langchain_core.documents import Document

from src.knowledge.providers.chroma_provider import ChromaProvider
from src.knowledge.types import VectorDocument

TEST_COLLECTION = "test_vector_store"


@pytest.fixture
def provider() -> ChromaProvider:
    """
    Proveedor preparado para las pruebas.
    Siempre inicia con una colección limpia.
    """

    provider = ChromaProvider()

    try:
        provider._client.delete_collection(TEST_COLLECTION)
    except Exception:
        pass

    provider.create_collection(TEST_COLLECTION)

    return provider


def test_create_provider() -> None:
    """
    Debe crear correctamente una instancia del proveedor.
    """

    provider = ChromaProvider()

    assert provider is not None

def test_create_collection(
    provider: ChromaProvider,
) -> None:

    assert provider._collection is not None

def test_load_collection(
    provider: ChromaProvider,
) -> None:

    new_provider = ChromaProvider()

    new_provider.load_collection(
        TEST_COLLECTION
    )

    assert new_provider._collection is not None

def test_add_documents(
    provider: ChromaProvider,
) -> None:
    """
    Debe agregar correctamente un documento a la colección.
    """

    document = VectorDocument(
        id="DOC-001",
        page_content="Documento de prueba.",
        metadata={
            "source": "pytest",
            "page": 1,
        },
        embedding=[0.1] * 3072,
    )

    provider.add_documents([document])

    assert provider.count_documents() == 1

def test_count_documents(
    provider: ChromaProvider,
) -> None:
    """
    Debe contar correctamente los documentos almacenados.
    """
    document = VectorDocument(
        id="DOC-001",
        page_content="Documento de prueba.",
        metadata={
            "source": "pytest",
            "page": 1,
        },
        embedding=[0.1] * 3072,
    )

    provider.add_documents([document])

    count = provider.count_documents()

    assert count == 1

def test_similarity_search(
    provider: ChromaProvider,
) -> None:
    """
    Debe recuperar correctamente un documento mediante búsqueda vectorial.
    """

    document = VectorDocument(
        id="DOC-001",
        page_content="Documento de prueba.",
        metadata={
            "source": "pytest",
            "page": 1,
        },
        embedding=[0.1] * 3072,
    )

    provider.add_documents([document])

    result = provider.similarity_search(
        embedding=[0.1] * 3072,
        k=1,
    )

    assert len(result) == 1

    assert isinstance(
        result[0],
        Document,
    )

    assert (
        result[0].page_content
        == "Documento de prueba."
    )

    assert (
        result[0].metadata["source"]
        == "pytest"
    )

    assert (
        result[0].metadata["page"]
        == 1
    )

def test_delete_documents(
    provider: ChromaProvider,
) -> None:
    """
    Debe eliminar correctamente un documento de la colección.
    """

    document = VectorDocument(
        id="DOC-001",
        page_content="Documento para eliminar.",
        metadata={
            "source": "pytest",
            "page": 1,
        },
        embedding=[0.1] * 3072,
    )

    provider.add_documents([document])

    assert provider.count_documents() == 1

    provider.delete_documents(["DOC-001"])

    assert provider.count_documents() == 0

def test_reset(
    provider: ChromaProvider,
) -> None:
    """
    Debe reiniciar correctamente la colección.
    """

    document = VectorDocument(
        id="DOC-001",
        page_content="Documento para reset.",
        metadata={
            "source": "pytest",
            "page": 1,
        },
        embedding=[0.1] * 3072,
    )

    provider.add_documents([document])

    assert provider.count_documents() == 1

    provider.reset()

    assert provider.count_documents() == 0

    assert provider._collection.get()["ids"] == []