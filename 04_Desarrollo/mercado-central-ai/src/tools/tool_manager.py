"""
Administrador de herramientas.

Gestiona el registro y la ejecución de las herramientas
disponibles para el sistema.
"""

from src.core.exceptions import DuplicateToolError

from src.tools.interfaces import (
    ToolInterface,
    ToolManagerInterface,
)


class ToolManager(ToolManagerInterface):
    """
    Administra el registro y ejecución de herramientas.
    """

    def __init__(self) -> None:
        self._tools: dict[str, ToolInterface] = {}

    def register(self, tool: ToolInterface) -> None:
        """
        Registra una herramienta.

        Raises:
            TypeError:
                Si el objeto no implementa ToolInterface.

            DuplicateToolError:
                Si ya existe una herramienta registrada con el
                mismo nombre.
        """

        if not isinstance(tool, ToolInterface):
            raise TypeError(
                "Tool must implement ToolInterface."
            )

        if tool.name in self._tools:
            raise DuplicateToolError(
                f"Tool '{tool.name}' is already registered."
            )

        self._tools[tool.name] = tool

    def has_tool(
        self,
        name: str,
    ) -> bool:
        """
        Indica si una herramienta se encuentra registrada.

        Parameters
        ----------
        name : str
            Nombre de la herramienta.

        Returns
        -------
        bool
            True si la herramienta está registrada;
            False en caso contrario.
        """

        return name in self._tools


    def execute(self, query: str) -> str | None:
        """
        Ejecuta la herramienta adecuada para la consulta.
        """

        tool = self._find(query)

        if tool is None:
            return None

        return tool.execute(query)

    def _find(self, query: str) -> ToolInterface | None:
        """
        Busca internamente una herramienta capaz de resolver
        la consulta.
        """

        for tool in self._tools.values():
            if tool.can_handle(query):
                return tool

        return None
    
    def has_tool(
    self,
    name: str,
    ) -> bool:
        """
        Indica si existe una herramienta registrada.
        """

        return name in self._tools