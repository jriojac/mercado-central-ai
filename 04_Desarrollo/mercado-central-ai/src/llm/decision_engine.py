"""
=========================================================
Implementación del Decision Engine.
=========================================================
"""

from src.llm.interfaces import DecisionEngineInterface
from src.llm.models import LLMRequest


class DecisionEngine(DecisionEngineInterface):
    """
    Implementación del motor de decisión.

    Su responsabilidad consiste en construir una
    solicitud preparada para un proveedor LLM.
    """

    def build_request(
        self,
        query: str,
        context: str,
    ) -> LLMRequest:
        """
        Construye una solicitud para un proveedor LLM.

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

        return LLMRequest(
            query=query,
            context=context,
        )