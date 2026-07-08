"""
==============================================================
INTERFACES
Retriever

Sprint 8 - Hito 6
Proyecto: Mercado Central AI

Define el contrato que deberán implementar todos los
Retrievers del proyecto.
==============================================================
"""

from abc import ABC, abstractmethod

from langchain_core.documents import Document


class IRetriever(ABC):
    """
    Interface for Retriever implementations.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
    ) -> list[Document]:
        """
        Retrieve the most relevant documents for a query.

        Args:
            query:
                User query.

            top_k:
                Maximum number of documents to retrieve.

        Returns:
            List of LangChain Document objects.
        """
        raise NotImplementedError