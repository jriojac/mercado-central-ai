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
from langchain_core.documents import Document

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

            try:
                self._collection = self._client.get_collection(
                    name=VECTOR_DB_COLLECTION
                )
            except Exception:
                # La colección todavía no existe.
                self._collection = None

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

            #metadatas.append(document.metadata)

            clean_metadata: dict[str, Any] = {}

            for key, value in document.metadata.items():

                if value is None:
                    continue

                clean_metadata[str(key)] = value

            metadatas.append(clean_metadata)


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

            for i, metadata in enumerate(metadatas):

                for key, value in metadata.items():

                    if not isinstance(
                        value,
                        (str, int, float, bool, type(None)),
                    ):

                        print()
                        print("=================================")
                        print(f"Documento: {i}")
                        print(f"Campo: {key}")
                        print(f"Tipo: {type(value)}")
                        print(f"Valor: {value}")
                        print("=================================")


            self._collection.add(
                ids=ids,
                documents=contents,
                metadatas=metadatas,
                embeddings=embeddings,
            )

            print()
            print("Documentos en colección:", self._collection.count())
            print()


        except Exception as exc:
            raise ProviderError(
                "No fue posible almacenar los documentos."
            ) from exc

    def similarity_search(
        self,
        embedding: list[float],
        k: int = 4,
    ) -> list[Document]:
        """
        Realiza una búsqueda por similitud sobre la colección activa.
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

            documents = []

            retrieved_docs = results.get("documents", [[]])[0]
            retrieved_metadata = results.get("metadatas", [[]])[0]

            for text, metadata in zip(
                retrieved_docs,
                retrieved_metadata,
            ):
                documents.append(
                    Document(
                        page_content=text,
                        metadata=metadata or {},
                    )
                )

            return documents

        except Exception:
            import traceback

            traceback.print_exc()

            raise

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

        Si la colección existe, la elimina y la crea nuevamente.
        Si no existe, simplemente crea una nueva colección.
        """

        try:

            name = self._resolve_collection_name(None)

            try:

                self._client.delete_collection(
                    name=name,
                )

            except Exception:
                # La colección aún no existe.
                pass

            self._collection = self._client.create_collection(
                name=name,
            )

        except Exception as exc:
            raise ProviderError(
                "No fue posible reiniciar la colección."
            ) from exc