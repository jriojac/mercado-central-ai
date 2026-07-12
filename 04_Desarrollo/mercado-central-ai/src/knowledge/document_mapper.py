"""
Document Mapper.

Convierte documentos enriquecidos del pipeline RAG al modelo
VectorDocument utilizado por el Vector Store.

Responsabilidad única:
- Transformar Document -> VectorDocument.
"""

from uuid import uuid4

from langchain_core.documents import Document

from .types import VectorDocument


class DocumentMapper:
    """
    Convierte documentos de LangChain al modelo VectorDocument.

    Esta clase no genera embeddings ni interactúa con el Vector Store.
    Su única responsabilidad es transformar los documentos del dominio.
    """

    def map_documents(
        self,
        documents: list[Document],
        embeddings: list[list[float]],
    ) -> list[VectorDocument]:
        """
        Convierte documentos enriquecidos a VectorDocument.

        Parameters
        ----------
        documents : list[Document]
            Documentos provenientes del pipeline.

        embeddings : list[list[float]]
            Embeddings generados para cada documento.

        Returns
        -------
        list[VectorDocument]
            Lista de documentos lista para almacenarse
            en el Vector Store.
        """

        if len(documents) != len(embeddings):
            raise ValueError(
                "La cantidad de documentos y embeddings no coincide."
            )

        vector_documents: list[VectorDocument] = []

        for document, embedding in zip(
            documents,
            embeddings,
        ):

            vector_documents.append(
                VectorDocument(
                    id=str(uuid4()),
                    page_content=document.page_content,
                    metadata=document.metadata,
                    embedding=embedding,
                )
            )

        return vector_documents