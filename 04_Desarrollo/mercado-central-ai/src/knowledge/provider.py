#---------------------------------------------------------------
#Definirá la interfaz abstracta (ABC) VectorStoreProvider.

#Esta interfaz será el contrato que deberán implementar todos los proveedores futuros (ChromaDB, FAISS, Qdrant, etc.).
#---------------------------------------------------------------


from abc import ABC, abstractmethod
from typing import Any

from src.knowledge.types import SearchResult


class VectorStoreProvider(ABC):
    """
    Interfaz base para los proveedores de almacenamiento vectorial.

    Todo proveedor (ChromaDB, FAISS, Qdrant, Pinecone, etc.)
    deberá implementar esta interfaz.
    """

    @abstractmethod
    def create_collection(self) -> None:
        """Crea una nueva colección vectorial.
        """
        pass
    
    @abstractmethod
    def load_collection(
        self,
        collection_name: str | None = None,
    ) -> None:
        """
        Carga una colección existente.
        """
        pass

    @abstractmethod
    def add_documents(self, documents: list[Any]) -> None:
        """Agrega documentos al almacén vectorial.
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        embedding: list[float],
        k: int = 4,
    ) -> list[Any]:
        """Realiza una búsqueda por similitud.
        """
        pass

    @abstractmethod
    def delete_documents(
        self,
        ids: list[str],
    ) -> None:
        """Elimina documentos por identificador.
        """
        pass

    @abstractmethod
    def count_documents(self) -> int:
        """
        Obtiene la cantidad de documentos almacenados.

        Returns
        -------
        int
            Número de documentos almacenados.
        """
        pass

    @abstractmethod
    def reset(self) -> None:
        """Elimina completamente la colección.
        """
        pass