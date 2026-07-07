#---------------------------------------------------------------
#Definirá los tipos compartidos del módulo, como VectorDocument y otros modelos de datos que sean necesarios.
#---------------------------------------------------------------

from dataclasses import dataclass
from typing import Any

@dataclass(slots=True)
class VectorDocument:
    """
    Representa un documento almacenado en el Vector Store.

    Contiene toda la información necesaria para persistir y
    recuperar un documento dentro de una base vectorial.
    """

    id: str
    page_content: str
    metadata: dict[str, Any]
    embedding: list[float]

@dataclass(slots=True)
class SearchResult:
    """
    Resultado de una búsqueda por similitud.
    """

    document: VectorDocument
    score: float


