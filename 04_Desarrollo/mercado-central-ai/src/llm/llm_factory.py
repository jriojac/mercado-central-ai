"""
=========================================================
Factory para proveedores LLM.
=========================================================
"""

from src.llm.interfaces import LLMProviderInterface
from src.llm.providers.google_gemini_provider import (
    GoogleGeminiProvider,
)


class LLMProviderFactory:
    """
    Factory responsable de crear proveedores LLM.
    """

    @staticmethod
    def create() -> LLMProviderInterface:
        """
        Crea una instancia del proveedor LLM configurado.

        Returns
        -------
        LLMProviderInterface
            Instancia lista para utilizarse.
        """

        return GoogleGeminiProvider()