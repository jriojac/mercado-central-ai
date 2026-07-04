from langchain_core.documents import Document

from src.core.exceptions import InvalidDocumentError
from src.llm.embedding_provider import EmbeddingProvider


class Embeddings:
    """
    Genera embeddings para una colección de documentos.
    """

    def __init__(self) -> None:
        """
        Inicializa el módulo Embeddings.
        """
        self._provider = EmbeddingProvider()

    def generate_embeddings(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Genera embeddings para cada documento de la colección.

        Args:
            documents: Lista de documentos enriquecidos por Metadata Manager.

        Returns:
            Lista de documentos con el embedding almacenado en metadata.
        """

        if not isinstance(documents, list):
            raise InvalidDocumentError(
                "La colección de documentos debe ser una lista."
            )

        if not documents:
            return documents

        for document in documents:

            if not isinstance(document, Document):
                raise InvalidDocumentError(
                    "Todos los elementos deben ser objetos Document."
                )

            embedding = self._provider.generate_document_embedding(
                document.page_content
            )

            document.metadata["embedding"] = embedding

        return documents