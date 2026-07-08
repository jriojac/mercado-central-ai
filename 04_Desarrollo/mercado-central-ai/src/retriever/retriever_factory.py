"""
==============================================================
Retriever Factory

Sprint 8 - Hito 6
Proyecto: Mercado Central AI
==============================================================
"""

from src.knowledge.providers.chroma_provider import ChromaProvider
from src.knowledge.vector_store import VectorStore

from .chroma_retriever import ChromaRetriever
from .interfaces import IRetriever


class RetrieverFactory:
    """
    Factory responsible for creating Retriever instances.
    """

    @staticmethod
    def create() -> IRetriever:
        """
        Create a configured Retriever instance.

        Returns:
            IRetriever
        """

        provider = ChromaProvider()

        vector_store = VectorStore(provider)

        return ChromaRetriever(vector_store)