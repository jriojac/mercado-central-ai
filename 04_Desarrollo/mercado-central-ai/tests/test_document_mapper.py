"""
Document Mapper.

Convierte documentos enriquecidos del pipeline RAG al modelo
VectorDocument utilizado por el Vector Store.
"""

from uuid import uuid4

from langchain_core.documents import Document

from src.core.exceptions import InvalidDocumentError

from .types import VectorDocument


class DocumentMapper:
    """
    Convierte documentos LangChain al modelo VectorDocument.
    """

    def map_documents(
        self,
        documents: list[Document],
    ) -> list[VectorDocument]:

        if not isinstance(documents, list):
            raise InvalidDocumentError(
                "La colección de documentos debe ser una lista."
            )

        vector_documents: list[VectorDocument] = []

        for document in documents:

            if not isinstance(document, Document):
                raise InvalidDocumentError(
                    "Todos los elementos deben ser objetos Document."
                )

            embedding = document.metadata.get("embedding")

            if embedding is None:
                raise InvalidDocumentError(
                    "El documento no contiene embedding."
                )

            vector_documents.append(
                VectorDocument(
                    id=str(uuid4()),
                    page_content=document.page_content,
                    metadata=document.metadata,
                    embedding=embedding,
                )
            )

        return vector_documents