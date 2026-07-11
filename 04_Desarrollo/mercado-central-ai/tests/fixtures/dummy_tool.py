"""
Implementación Dummy de ToolInterface para pruebas unitarias.
"""

from src.tools.interfaces import ToolInterface


class DummyTool(ToolInterface):
    """
    Implementación mínima de ToolInterface utilizada
    exclusivamente para pruebas.
    """

    @property
    def name(self) -> str:
        """
        Nombre de la herramienta.
        """
        return "dummy"

    @property
    def description(self) -> str:
        """
        Descripción de la herramienta.
        """
        return "Dummy Tool"

    def can_handle(self, query: str) -> bool:
        """
        Indica si la herramienta puede atender la consulta.
        """
        return query == "dummy"

    def execute(self, query: str) -> str:
        """
        Ejecuta la herramienta.
        """
        return f"Executed: {query}"