"""
=========================================================
Mercado Central AI

Inicializador de la Base Vectorial.

Ejecuta el proceso completo de carga de documentos,
generación de embeddings e indexación en ChromaDB.

Sprint 14 - Hito 12
=========================================================
"""

from src.core.knowledge_initializer import (
    KnowledgeInitializer,
)


def main() -> None:
    """
    Punto de entrada del inicializador.
    """

    initializer = KnowledgeInitializer()

    initializer.run()


if __name__ == "__main__":
    main()