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

from src.knowledge.embeddings import Embeddings


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

        self._embeddings = Embeddings()

    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
    ) -> list[Document]:

        k = top_k if top_k is not None else RETRIEVER_TOP_K

        embedding = self._embeddings.generate_query_embedding(
            query
        )

        return self._vector_store.similarity_search(
            embedding=embedding,
            k=k,
        )