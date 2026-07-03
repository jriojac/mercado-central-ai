"""
Módulo Metadata Manager.

Responsable de validar, normalizar y enriquecer la metadata
de los chunks antes de la generación de embeddings.

Sprint 5 – Hito 3
Release objetivo: v0.3.0
"""

from pathlib import Path

from langchain_core.documents import Document

from src.core.exceptions import (
    MetadataValidationError,
    MissingMetadataError,
)

from datetime import datetime, UTC
from uuid import uuid4

from src.config.settings import (
    PROJECT_VERSION,
    DEFAULT_LANGUAGE,
    DEFAULT_CATEGORY,
)


class MetadataManager:
    """
    Gestiona la metadata asociada a los documentos
    generados por el Text Splitter.
    """

    REQUIRED_METADATA = {
        "source",
        "file_name",
        "file_type",
        "chunk_index",
        "total_chunks",
        "chunk_size",
        "splitter_version",
    }

    def process_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Procesa una colección de documentos.

        Realiza:

        - Validación
        - Normalización
        - Enriquecimiento

        Parameters
        ----------
        documents : list[Document]
            Colección de documentos.

        Returns
        -------
        list[Document]
            Documentos listos para Embeddings.
        """

        if not isinstance(documents, list):
            raise TypeError(
                "documents debe ser una lista de Document."
            )

        if not documents:
            return []

        for document in documents:

            if not isinstance(document, Document):
                raise TypeError(
                    "Todos los elementos deben ser objetos Document."
                )

            self._validate_metadata(document)

            self._normalize_metadata(document)

            self._enrich_metadata(document)

        return documents


    def _validate_metadata(self, document: Document) -> None:
        """
        Valida que un documento contenga la metadata mínima requerida.
        """

        metadata = document.metadata

        if not metadata:
            raise MetadataValidationError(
                "El documento no contiene metadata."
            )

        missing_fields = self.REQUIRED_METADATA - metadata.keys()

        if missing_fields:
            raise MissingMetadataError(
                "Faltan campos obligatorios en la metadata: "
                f"{', '.join(sorted(missing_fields))}"
            )

    def _normalize_metadata(self, document: Document) -> None:
        """
        Normaliza la metadata del documento.
        """

        metadata = document.metadata

        # source
        metadata["source"] = str(
            Path(metadata["source"])
        ).replace("\\", "/")

        # file_name
        file_name = Path(metadata["file_name"])
        metadata["file_name"] = (
            f"{file_name.stem}{file_name.suffix.lower()}"
        )

        # file_type
        metadata["file_type"] = (
            str(metadata["file_type"])
            .strip()
            .lower()
        )

        # índices numéricos
        metadata["chunk_index"] = int(metadata["chunk_index"])
        metadata["total_chunks"] = int(metadata["total_chunks"])
        metadata["chunk_size"] = int(metadata["chunk_size"])

        # versión
        metadata["splitter_version"] = (
            str(metadata["splitter_version"])
            .strip()
        )

    def _enrich_metadata(self, document: Document) -> None:
        """
        Agrega metadata adicional al documento.
        """

        metadata = document.metadata

        metadata["document_id"] = str(uuid4())

        metadata["ingest_date"] = (
            datetime.now(UTC)
            .replace(microsecond=0)
            .isoformat()
        )

        metadata["pipeline_version"] = PROJECT_VERSION

        metadata["language"] = DEFAULT_LANGUAGE

        metadata["category"] = DEFAULT_CATEGORY