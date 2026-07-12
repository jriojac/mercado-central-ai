"""
=========================================================
Pruebas para GoogleGeminiProvider.
=========================================================
"""

from unittest.mock import MagicMock
from unittest.mock import patch

from src.llm.interfaces import LLMProviderInterface
from src.llm.providers.google_gemini_provider import (
    GoogleGeminiProvider,
)


def test_provider_implements_interface():
    """
    Verifica que el Provider implementa
    LLMProviderInterface.
    """

    provider = GoogleGeminiProvider()

    assert isinstance(
        provider,
        LLMProviderInterface,
    )


@patch(
    "src.llm.providers.google_gemini_provider.ChatGoogleGenerativeAI"
)
def test_generate_response_returns_content(
    mock_chat,
):
    """
    Verifica que generate_response() devuelve el
    contenido generado por el proveedor LLM.
    """

    mock_llm = MagicMock()

    mock_response = MagicMock()

    mock_response.content = "Respuesta simulada"

    mock_llm.invoke.return_value = mock_response

    mock_chat.return_value = mock_llm

    provider = GoogleGeminiProvider()

    response = provider.generate_response(
        "Hola"
    )

    assert response == "Respuesta simulada"

    mock_llm.invoke.assert_called_once_with(
        "Hola"
    )