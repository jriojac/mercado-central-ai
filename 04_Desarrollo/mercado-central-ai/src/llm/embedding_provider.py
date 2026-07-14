"""
---------------------------------------------------------
Debe ejecutarse desde la raíz del proyecto con:

  python -m py_compile src/llm/embedding_provider.py
=========================================================
"""

import re
import time

from langchain_google_genai._common import (
    GoogleGenerativeAIError,
)

import asyncio
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
    print(f"Modelo de embeddings: {EMBEDDING_MODEL}")

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

#        try:
#            self._embedding_model = GoogleGenerativeAIEmbeddings(
#                model=EMBEDDING_MODEL
#            )
#
#        except Exception as error:
#            raise EmbeddingConfigurationError(
#                "No fue posible inicializar el modelo de embeddings."
#            ) from error

        try:
            asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            self._embedding_model = GoogleGenerativeAIEmbeddings(
                model=EMBEDDING_MODEL
            )

        except Exception as error:
            import traceback

            traceback.print_exc()

            raise
    

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

        while True:

            try:

                embedding = self._embedding_model.embed_documents(
                    [text]
                )

                return embedding[0]

            except GoogleGenerativeAIError as error:

                message = str(error)

                if (
                    "RESOURCE_EXHAUSTED" in message
                    or "429" in message
                    or "Please retry in" in message
                ):

                    retry_seconds = 30

                    match = re.search(
                        r"Please retry in ([0-9.]+)s",
                        message,
                    )

                    if match:

                        retry_seconds = int(
                            float(match.group(1))
                        ) + 1

                    print(
                        f"⚠️ Cuota de Gemini alcanzada. "
                        f"Esperando {retry_seconds} segundos..."
                    )

                    time.sleep(retry_seconds)

                    continue

                raise EmbeddingProviderError(
                    "Error al generar el embedding del documento."
                ) from error

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
        
        print(self._embedding_model)
