"""
=========================================================
Factory para el módulo Tools.
=========================================================
"""

from src.tools.interfaces import ToolManagerInterface
from src.tools.tool_manager import ToolManager
from src.tools.interfaces import ToolManagerInterface


class ToolFactory:
    """
    Factory responsable de crear instancias
    del Tool Manager.
    """

    @staticmethod
    def create() -> ToolManagerInterface:
        """
        Crea una instancia del Tool Manager.

        Returns
        -------
        ToolManagerInterface
            Instancia lista para utilizarse.
        """

        manager = ToolManager()

        #
        # Registro de herramientas
        # (Sprint futuro)
        #

        return ToolManager()