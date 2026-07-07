"""
Proveedor ChromaDB para el módulo Vector Store.

Este módulo implementa la interfaz VectorStoreProvider utilizando
ChromaDB como motor de almacenamiento vectorial.
"""

from typing import Any

import chromadb

from src.config.settings import (
    VECTOR_DB_COLLECTION,
    VECTOR_DB_PATH,
)
from src.core.exceptions import ProviderError
from src.knowledge.provider import VectorStoreProvider


class ChromaProvider(VectorStoreProvider):
    """
    Implementación del proveedor de almacenamiento vectorial
    utilizando ChromaDB.
    """

    def __init__(self) -> None:
        """
        Inicializa el cliente persistente de ChromaDB.
        """
        try:
            self._client: Any = chromadb.PersistentClient(
                path=str(VECTOR_DB_PATH)
            )

            self._collection: Any | None = None

        except Exception as exc:
            raise ProviderError(
                "No fue posible inicializar el cliente de ChromaDB."
            ) from exc

    def _resolve_collection_name(
        self,
        collection_name: str | None,
    ) -> str:
        """
        Obtiene el nombre efectivo de la colección.

        Parameters
        ----------
        collection_name : str | None
            Nombre recibido por el método.

        Returns
        -------
        str
            Nombre definitivo de la colección.
        """
        return collection_name or VECTOR_DB_COLLECTION

    def _to_chroma_format(
        self,
        documents: list[VectorDocument],
    ) -> tuple[
        list[str],
        list[str],
        list[dict[str, Any]],
        list[list[float]],
    ]:
        """
        Convierte una lista de VectorDocument al formato
        requerido por ChromaDB.

        Parameters
        ----------
        documents : list[VectorDocument]
            Documentos del dominio.

        Returns
        -------
        tuple
            Tupla compuesta por:

            - ids
            - documents
            - metadatas
            - embeddings
        """

        ids: list[str] = []
        contents: list[str] = []
        metadatas: list[dict[str, Any]] = []
        embeddings: list[list[float]] = []

        for document in documents:

            ids.append(document.id)

            contents.append(document.page_content)

            metadatas.append(document.metadata)

            embeddings.append(document.embedding)

        return (
            ids,
            contents,
            metadatas,
            embeddings,
        )

    def create_collection(
        self,
        collection_name: str | None = None,
    ) -> None:
        """
        Crea una colección vectorial.

        Parameters
        ----------
        collection_name : str | None
            Nombre de la colección.
            Si es None se utilizará la colección definida
            en settings.py.
        """

        # name = collection_name or VECTOR_DB_COLLECTION
        name = self._resolve_collection_name(collection_name)

        try:
            self._collection = self._client.create_collection(
                name=name
            )

        except Exception as exc:
            raise ProviderError(
                f"No fue posible crear la colección '{name}'."
            ) from exc

    def load_collection(
        self,
        collection_name: str | None = None,
    ) -> None:
        """
        Carga una colección existente.

        Parameters
        ----------
        collection_name : str | None
            Nombre de la colección.
            Si es None se utilizará la colección definida
            en settings.py.
        """

        # name = collection_name or VECTOR_DB_COLLECTION
        name = self._resolve_collection_name(collection_name)

        try:
            self._collection = self._client.get_collection(
                name=name
            )

        except Exception as exc:
            raise ProviderError(
                f"No fue posible cargar la colección '{name}'."
            ) from exc

    def add_documents(
        self,
        documents: list[VectorDocument],
    ) -> None:
        """
        Agrega documentos al Vector Store.

        Parameters
        ----------
        documents : list[VectorDocument]
            Documentos del dominio que serán almacenados.
        """

        if self._collection is None:
            raise ProviderError(
                "No existe una colección cargada."
            )

        if not documents:
            raise ProviderError(
                "La lista de documentos no puede estar vacía."
            )

        try:

            ids, contents, metadatas, embeddings = (
                self._to_chroma_format(documents)
            )

            self._collection.add(
                ids=ids,
                documents=contents,
                metadatas=metadatas,
                embeddings=embeddings,
            )

        except Exception as exc:
            raise ProviderError(
                "No fue posible almacenar los documentos."
            ) from exc

    def similarity_search(
        self,
        embedding: list[float],
        k: int = 4,
    ) -> list[Any]:
        """
        Realiza una búsqueda por similitud sobre la colección activa.

        Parameters
        ----------
        query : str
            Texto de consulta.

        k : int, default=4
            Número máximo de resultados.

        Returns
        -------
        list[Any]
            Resultados obtenidos desde ChromaDB.
        """

        if self._collection is None:
            raise ProviderError(
                "No existe una colección cargada."
            )

        try:

            results = self._collection.query(
                query_embeddings=[embedding],
                n_results=k,
            )

            return results

        except Exception as exc:
            raise ProviderError(
                "No fue posible realizar la búsqueda por similitud."
            ) from exc

    def delete_documents(
        self,
        ids: list[str],
    ) -> None:
        """
        Elimina documentos de la colección activa.

        Parameters
        ----------
        ids : list[str]
            Identificadores de los documentos que serán eliminados.
        """

        if self._collection is None:
            raise ProviderError(
                "No existe una colección cargada."
            )

        if not ids:
            raise ProviderError(
                "La lista de identificadores no puede estar vacía."
            )

        try:

            self._collection.delete(
                ids=ids,
            )

        except Exception as exc:
            raise ProviderError(
                "No fue posible eliminar los documentos."
            ) from exc

    def count_documents(self) -> int:
        """
        Obtiene la cantidad de documentos almacenados
        en la colección activa.

        Returns
        -------
        int
            Número de documentos almacenados.
        """

        if self._collection is None:
            raise ProviderError(
                "No existe una colección cargada."
            )

        try:
            return self._collection.count()

        except Exception as exc:
            raise ProviderError(
                "No fue posible obtener la cantidad de documentos."
            ) from exc

    def reset(self) -> None:
        """
        Reinicia completamente la colección activa.

        Elimina la colección existente y crea una nueva con
        el mismo nombre configurado.
        """

        if self._collection is None:
            raise ProviderError(
                "No existe una colección cargada."
            )
        try:

            name = self._resolve_collection_name(None)

            self._client.delete_collection(
                name=name,
            )

            self._collection = self._client.create_collection(
                name=name,
            )

        except Exception as exc:
            raise ProviderError(
                "No fue posible reiniciar la colección."
            ) from exc
