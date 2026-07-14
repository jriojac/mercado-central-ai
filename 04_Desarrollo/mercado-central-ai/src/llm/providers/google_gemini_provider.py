"""
=========================================================
Proveedor Google Gemini.
=========================================================
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import settings
from src.llm.interfaces import LLMProviderInterface
from src.llm.interfaces import LLMProviderInterface


class GoogleGeminiProvider(LLMProviderInterface):
    """
    Implementación del proveedor Google Gemini.
    """

    def __init__(self) -> None:
        """
        Inicializa el proveedor Google Gemini.
        """

        self._llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=settings.GEMINI_TEMPERATURE,
            max_output_tokens=settings.GEMINI_MAX_OUTPUT_TOKENS,
        )

    def generate_response(
        self,
        prompt: str,
    ) -> str:
        """
        Genera una respuesta utilizando Google Gemini.

        Parameters
        ----------
        prompt:
            Prompt construido por el Decision Engine.

        Returns
        -------
        str
            Respuesta generada por el modelo.
        """

        response = self._llm.invoke(prompt)

        return response.content
