"""
Context Builder Factory.

Factory responsable de crear implementaciones del Context Builder.

Sprint 9 - Hito 7
Release v0.7.0
"""

from .interfaces import ContextBuilderInterface
from .simple_context_builder import SimpleContextBuilder


class ContextBuilderFactory:
    """
    Factory para crear implementaciones del Context Builder.
    """

    @staticmethod
    def create() -> ContextBuilderInterface:
        """
        Crea una instancia del Context Builder configurado.

        Returns
        -------
        ContextBuilderInterface
            Implementación concreta del constructor de contexto.
        """
        return SimpleContextBuilder()