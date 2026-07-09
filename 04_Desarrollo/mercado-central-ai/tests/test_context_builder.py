"""
Pruebas unitarias para el Context Builder.

Sprint 9 - Hito 7
Release v0.7.0
"""

import pytest
from langchain_core.documents import Document

from src.config.settings import CONTEXT_SEPARATOR
from src.context_builder.context_builder_factory import ContextBuilderFactory
from src.context_builder.interfaces import ContextBuilderInterface
from src.context_builder.simple_context_builder import SimpleContextBuilder


@pytest.fixture
def builder() -> SimpleContextBuilder:
    """
    Fixture que proporciona una instancia del Context Builder.
    """
    return SimpleContextBuilder()


def test_build_context_empty_documents(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe retornar una cadena vacía cuando no existen documentos.
    """
    assert builder.build_context([]) == ""


def test_build_context_single_document(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe construir correctamente el contexto con un único documento.
    """
    documents = [
        Document(page_content="Documento A"),
    ]

    context = builder.build_context(documents)

    assert context == "Documento A"


def test_build_context_multiple_documents(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe unir múltiples documentos utilizando el separador configurado.
    """
    documents = [
        Document(page_content="Documento A"),
        Document(page_content="Documento B"),
        Document(page_content="Documento C"),
    ]

    context = builder.build_context(documents)

    expected = CONTEXT_SEPARATOR.join(
        [
            "Documento A",
            "Documento B",
            "Documento C",
        ]
    )

    assert context == expected


def test_build_context_preserves_document_order(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe preservar el orden recibido desde el Retriever.
    """
    documents = [
        Document(page_content="Primero"),
        Document(page_content="Segundo"),
        Document(page_content="Tercero"),
    ]

    context = builder.build_context(documents)

    assert context.index("Primero") < context.index("Segundo")
    assert context.index("Segundo") < context.index("Tercero")


def test_build_context_ignores_empty_documents(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe ignorar documentos vacíos o con solo espacios.
    """
    documents = [
        Document(page_content="Documento A"),
        Document(page_content=""),
        Document(page_content="   "),
        Document(page_content="Documento B"),
    ]

    context = builder.build_context(documents)

    expected = CONTEXT_SEPARATOR.join(
        [
            "Documento A",
            "Documento B",
        ]
    )

    assert context == expected


def test_context_builder_factory_returns_interface() -> None:
    """
    La Factory debe devolver una implementación válida del contrato.
    """
    builder = ContextBuilderFactory.create()

    assert isinstance(builder, ContextBuilderInterface)

    assert isinstance(builder, SimpleContextBuilder)

def test_build_context_respects_max_context_chars(
    builder: SimpleContextBuilder,
) -> None:
    """
    Debe respetar la longitud máxima configurada.
    """
    from src.config.settings import MAX_CONTEXT_CHARS

    long_text = "A" * (MAX_CONTEXT_CHARS + 500)

    documents = [
        Document(page_content=long_text),
    ]

    context = builder.build_context(documents)

    assert len(context) == MAX_CONTEXT_CHARS