"""
=========================================================
Pruebas unitarias para LLMProviderFactory.
=========================================================
"""

from src.llm.interfaces import LLMProviderInterface
from src.llm.llm_factory import LLMProviderFactory


def test_create_returns_llm_provider_interface():
    """
    Verifica que la Factory devuelve un proveedor
    compatible con LLMProviderInterface.
    """

    provider = LLMProviderFactory.create()

    assert isinstance(provider, LLMProviderInterface)