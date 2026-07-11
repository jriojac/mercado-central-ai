"""
=========================================================
Factory para el módulo Decision Engine.
=========================================================
"""

from src.llm.decision_engine import DecisionEngine
from src.llm.interfaces import DecisionEngineInterface


class DecisionEngineFactory:
    """
    Factory responsable de crear instancias del
    Decision Engine.
    """

    @staticmethod
    def create() -> DecisionEngineInterface:
        """
        Crea una instancia del Decision Engine.

        Returns
        -------
        DecisionEngineInterface
            Instancia lista para utilizarse.
        """

        return DecisionEngine()