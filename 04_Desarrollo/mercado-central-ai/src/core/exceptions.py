"""
Excepciones personalizadas del proyecto Mercado Central AI.

Este módulo centraliza las excepciones utilizadas por los
diferentes componentes del pipeline RAG.
"""


class MetadataValidationError(Exception):
    """
    Error general de validación de metadata.
    """

    pass


class MissingMetadataError(MetadataValidationError):
    """
    Se genera cuando faltan campos obligatorios
    en la metadata de un Document.
    """

    pass


class InvalidDocumentCollectionError(Exception):
    """La colección de documentos recibida no es válida."""
    pass


class InvalidDocumentError(Exception):
    """Se recibió un objeto que no es un Document de LangChain."""
    pass


class EmbeddingProviderError(Exception):
    """Error generado por el proveedor de embeddings."""


class EmbeddingConfigurationError(Exception):
    """Configuración inválida del módulo Embeddings."""


class EmbeddingTimeoutError(Exception):
    """Tiempo de espera agotado durante la generación de embeddings."""


class InvalidDocumentError(Exception):
    """Documento inválido para generar embeddings."""