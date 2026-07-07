#---------------------------------------------------------------
#Contendrá únicamente la clase principal.

#Responsabilidad:

#administrar el almacenamiento vectorial;
#recibir un proveedor mediante inyección de dependencias;
#exponer la API pública del módulo.

#Sin lógica específica del proveedor.
#---------------------------------------------------------------

"""
Módulo principal del Vector Store.

Este módulo expone la clase VectorStore, que actúa como fachada
para el almacenamiento vectorial del proyecto Mercado Central AI.

La implementación concreta del almacenamiento se delega a un
VectorStoreProvider, permitiendo desacoplar el pipeline RAG
de cualquier tecnología específica (ChromaDB, FAISS, Qdrant,
Pinecone, etc.).
"""

from typing import Any

from .provider import VectorStoreProvider


class VectorStore:
    """
    Fachada del módulo Vector Store.

    Expone una API unificada para interactuar con el almacenamiento
    vectorial, delegando todas las operaciones al proveedor
    configurado.

    Esta clase no contiene lógica específica del proveedor.
    """

    def __init__(self, provider: VectorStoreProvider) -> None:
        """
        Inicializa el Vector Store.

        Parameters
        ----------
        provider : VectorStoreProvider
            Implementación concreta del proveedor de almacenamiento
            vectorial.
        """
        self._provider = provider

    def create_collection(self) -> None:
        """
        Crea una nueva colección vectorial.
        """
        self._provider.create_collection()

    def load_collection(
        self,
        collection_name: str | None = None,
    ) -> None:
        """
        Carga una colección existente.

        Parameters
        ----------
        collection_name : str | None, optional
            Nombre de la colección a cargar. Si es None,
            el proveedor utilizará la colección configurada.
        """
        self._provider.load_collection(collection_name)

    def add_documents(
        self,
        documents: list[Any],
    ) -> None:
        """
        Agrega documentos al Vector Store.

        Parameters
        ----------
        documents : list[Any]
            Colección de documentos vectoriales.
        """
        self._provider.add_documents(documents)

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ) -> list[Any]:
        """
        Realiza una búsqueda por similitud.

        Parameters
        ----------
        query : str
            Consulta de búsqueda.

        k : int
            Número máximo de resultados.

        Returns
        -------
        list[Any]
            Documentos recuperados por similitud.
        """
        return self._provider.similarity_search(query, k)

    def delete_documents(
        self,
        ids: list[str],
    ) -> None:
        """
        Elimina documentos utilizando sus identificadores.

        Parameters
        ----------
        ids : list[str]
            Identificadores de los documentos.
        """
        self._provider.delete_documents(ids)

    def count_documents(self) -> int:
        """
        Obtiene la cantidad de documentos almacenados.

        Returns
        -------
        int
            Número de documentos almacenados.
        """
        return self._provider.count_documents()

    def reset(self) -> None:
        """
        Elimina completamente la colección.

        Uso exclusivo para pruebas y mantenimiento.
        """
        self._provider.reset()