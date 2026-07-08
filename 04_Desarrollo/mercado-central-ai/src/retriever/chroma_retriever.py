"""
Chroma Retriever implementation.

Sprint 8 - Hito 6
Proyecto: Mercado Central AI

Implementación del contrato IRetriever utilizando el
módulo VectorStore del proyecto.
"""

from langchain_core.documents import Document

from src.knowledge.vector_store import VectorStore

from .interfaces import IRetriever

from src.config.settings import (
    RETRIEVER_TOP_K,
    RETRIEVER_VALIDATE_QUERY,
)



class ChromaRetriever(IRetriever):
    """
    Retriever implementation backed by the project's VectorStore.

    Esta clase no conoce ChromaDB directamente.
    Toda la interacción con el almacenamiento vectorial
    se realiza mediante la fachada VectorStore.
    """

    def __init__(
        self,
        vector_store: VectorStore,
    ) -> None:
        """
        Inicializa el Retriever.

        Args:
            vector_store:
                Fachada del módulo Vector Store.
        """
        self._vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
    ) -> list[Document]:
        """
        Recupera los documentos más relevantes para una consulta.

        Args:
            query:
                Consulta del usuario.

            top_k:
                Número máximo de documentos a recuperar.
                Si es None se utilizará el valor por defecto
                del Vector Store.

        Returns:
            Lista de documentos ordenados por relevancia.
        """

        k = top_k if top_k is not None else RETRIEVER_TOP_K

        return self._vector_store.similarity_search(
            query=query,
            k=k,
        )