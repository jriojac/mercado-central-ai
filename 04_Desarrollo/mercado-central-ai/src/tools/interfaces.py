"""
Interfaces públicas del módulo Tools.

Define los contratos públicos del módulo.
"""

from abc import ABC, abstractmethod


class ToolInterface(ABC):
    """
    Contrato base para todas las herramientas.

    Cada herramienta debe indicar si puede atender una
    consulta y ejecutar su lógica cuando corresponda.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Nombre único de la herramienta.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Descripción funcional de la herramienta.
        """
        raise NotImplementedError

    @abstractmethod
    def can_handle(self, query: str) -> bool:
        """
        Indica si la herramienta puede atender la consulta.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self, query: str) -> str:
        """
        Ejecuta la herramienta.
        """
        raise NotImplementedError


class ToolManagerInterface(ABC):
    """
    Contrato para el administrador de herramientas.
    """

    @abstractmethod
    def register(
        self,
        tool: ToolInterface,
    ) -> None:
        """
        Registra una herramienta.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        query: str,
    ) -> str | None:
        """
        Ejecuta la herramienta adecuada para la consulta.
        """
        raise NotImplementedError

    @abstractmethod
    def has_tool(
        self,
        name: str,
    ) -> bool:
        """
        Indica si una herramienta se encuentra registrada.
        """
        raise NotImplementedError