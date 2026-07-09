"""
Simple Context Builder.

Implementación básica del constructor de contexto para el pipeline RAG.

Sprint 9 - Hito 7
Release v0.7.0
"""

from langchain_core.documents import Document

from .interfaces import ContextBuilderInterface

from src.config.settings import (
    CONTEXT_SEPARATOR,
    MAX_CONTEXT_CHARS,
)

class SimpleContextBuilder(ContextBuilderInterface):
    """
    Implementación básica del Context Builder.

    Consolida una colección de documentos recuperados por el Retriever
    en un único contexto textual, preservando el orden recibido.
    """

   # CONTEXT_SEPARATOR = "\n\n----------------------------------------\n\n"

    def build_context(
        self,
        documents: list[Document],
    ) -> str:
        """
        Construye un contexto textual a partir de los documentos recuperados.

        Parameters
        ----------
        documents : list[Document]
            Documentos recuperados por el Retriever.

        Returns
        -------
        str
            Contexto consolidado listo para ser utilizado por el
            Decision Engine.
        """
        context = CONTEXT_SEPARATOR.join(
            document.page_content.strip()
            for document in documents
            if document.page_content.strip()
        )

        return context[:MAX_CONTEXT_CHARS]
