"""
=========================================================
Interfaces del módulo LLM.
=========================================================
"""

from abc import ABC, abstractmethod

from src.llm.models import LLMRequest



class DecisionEngineInterface(ABC):
    """
    Define el contrato para los motores de decisión.
    """

    @abstractmethod
    def build_request(
        self,
        query: str,
        context: str,
    ) -> LLMRequest:
        """
        Construye una solicitud preparada para un proveedor LLM.

        Parameters
        ----------
        query:
            Consulta realizada por el usuario.

        context:
            Contexto generado por el Context Builder.

        Returns
        -------
        LLMRequest
            Solicitud preparada para un proveedor LLM.
        """


class LLMProviderInterface(ABC):
    """
    Define el contrato para los proveedores de Modelos
    de Lenguaje (LLM).
    """

    @abstractmethod
    def generate_response(
        self,
        request: LLMRequest,
    ) -> str:
        """
        Genera una respuesta utilizando un proveedor LLM.

        Parameters
        ----------
        request:
            Solicitud preparada por el Decision Engine.

        Returns
        -------
        str
            Respuesta generada por el modelo.
        """