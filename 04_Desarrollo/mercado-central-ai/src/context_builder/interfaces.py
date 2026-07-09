"""
Context Builder Interfaces.

Define los contratos públicos para los constructores de contexto del
pipeline RAG.

Sprint 9 - Hito 7
Release v0.7.0
"""

from abc import ABC, abstractmethod

from langchain_core.documents import Document

from typing import TypeAlias

Documents: TypeAlias = list[Document]

class ContextBuilderInterface(ABC):
    """
    Contrato base para los constructores de contexto.

    Un Context Builder transforma una colección de documentos recuperados
    por el Retriever en un único contexto textual listo para ser
    consumido por el Decision Engine.

    La implementación concreta NO debe:

    - invocar modelos LLM;
    - ejecutar búsquedas;
    - modificar documentos;
    - depender de un proveedor específico.

    Su única responsabilidad es construir el contexto.
    """

    @abstractmethod
    def build_context(
        self,
        documents: Documents,
    ) -> str:
        """
        Construye un contexto textual a partir de una colección de
        documentos recuperados.

        Parameters
        ----------
        documents : list[Document]
            Documentos obtenidos por el Retriever.

        Returns
        -------
        str
            Contexto consolidado listo para ser utilizado por el
            Decision Engine.
        """
        pass