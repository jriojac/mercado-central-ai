"""
Excepciones personalizadas del proyecto Mercado Central AI.

Este módulo centraliza las excepciones utilizadas por los
diferentes componentes del pipeline RAG.
"""


# ==========================================================
# METADATA
# ==========================================================

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


# ==========================================================
# DOCUMENTS
# ==========================================================

class InvalidDocumentCollectionError(Exception):
    """
    La colección de documentos recibida no es válida.
    """
    pass


class InvalidDocumentError(Exception):
    """
    Se recibió un documento inválido para el procesamiento
    dentro del pipeline RAG.
    """
    pass


# ==========================================================
# EMBEDDINGS
# ==========================================================

class EmbeddingProviderError(Exception):
    """
    Error generado por el proveedor de embeddings.
    """
    pass


class EmbeddingConfigurationError(Exception):
    """
    Configuración inválida del módulo Embeddings.
    """
    pass


class EmbeddingTimeoutError(Exception):
    """
    Tiempo de espera agotado durante la generación
    de embeddings.
    """
    pass


# ==========================================================
# VECTOR STORE
# ==========================================================

class VectorStoreError(Exception):
    """
    Excepción base del módulo Vector Store.
    """
    pass


class ProviderError(VectorStoreError):
    """
    Error generado por el proveedor del Vector Store.
    """
    pass


class CollectionNotFoundError(VectorStoreError):
    """
    La colección solicitada no existe.
    """
    pass


class PersistenceError(VectorStoreError):
    """
    Error durante la persistencia del Vector Store.
    """
    pass


class VectorStoreConfigurationError(VectorStoreError):
    """
    Configuración inválida del módulo Vector Store.
    """
    pass