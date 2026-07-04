"""
---------------------------------------------------------
Debe ejecutarse desde la raíz del proyecto con:

  python -m py_compile src/llm/embedding_provider.py
=========================================================
"""


from langchain_google_genai import GoogleGenerativeAIEmbeddings

#from src.config.settings import EMBEDDING_MODEL

from src.config.settings import (
    EMBEDDING_MODEL,
    GOOGLE_API_KEY,
)


from src.core.exceptions import (
    EmbeddingConfigurationError,
    EmbeddingProviderError,
    InvalidDocumentError,
)


class EmbeddingProvider:
    """
    Proveedor de embeddings utilizando Google Generative AI.
    """

    def __init__(self) -> None:
        """
        Inicializa el proveedor.
        """
        self._embedding_model = None




    def _initialize_model(self) -> None:
        """
        Inicializa el modelo de embeddings.
        """

        if self._embedding_model is not None:
            return

        if not GOOGLE_API_KEY:
            raise EmbeddingConfigurationError(
                "No se encontró la variable GOOGLE_API_KEY. "
                "Configure el archivo .env antes de utilizar "
                "el proveedor de embeddings."
            )

        try:
            self._embedding_model = GoogleGenerativeAIEmbeddings(
                model=EMBEDDING_MODEL
            )

        except Exception as error:
            raise EmbeddingConfigurationError(
                "No fue posible inicializar el modelo de embeddings."
            ) from error

    def generate_document_embedding(
        self,
        text: str,
    ) -> list[float]:
        """
        Genera el embedding de un documento.
        """

        text = text.strip()

        if not text:
            raise InvalidDocumentError(
                "El documento no contiene texto."
            )

        self._initialize_model()

        try:

            embedding = self._embedding_model.embed_documents(
                [text]
            )

            return embedding[0]

        except Exception as error:

            raise EmbeddingProviderError(
                "Error al generar el embedding del documento."
            ) from error

    def generate_query_embedding(
        self,
        text: str,
    ) -> list[float]:
        """
        Genera el embedding de una consulta.
        """

        text = text.strip()

        if not text:
            raise InvalidDocumentError(
                "La consulta no contiene texto."
            )

        self._initialize_model()

        try:

            return self._embedding_model.embed_query(text)

        except Exception as error:

            raise EmbeddingProviderError(
                "Error al generar el embedding de la consulta."
            ) from error