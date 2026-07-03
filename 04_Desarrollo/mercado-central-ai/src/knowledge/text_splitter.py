from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config.settings import TEXT_SPLITTER

class TextSplitter:
    """
    Módulo responsable de fragmentar documentos para el pipeline RAG.
    """

    def __init__(self):
        """
        Inicializa el Text Splitter.
        """

        self.chunk_size = TEXT_SPLITTER["chunk_size"]
        self.chunk_overlap = TEXT_SPLITTER["chunk_overlap"]
        self.version = TEXT_SPLITTER["version"]

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

    def _validate_documents(self, documents):
        """
        Valida la colección de documentos de entrada.
        """

        if documents is None:
            raise ValueError(
                "La colección de documentos no puede ser None."
            )

        if not isinstance(documents, list):
            raise TypeError(
                "La entrada debe ser una lista de documentos."
            )

        if len(documents) == 0:
            raise ValueError(
                "La colección de documentos está vacía."
            )


    def _split(self, documents):
        """
        Fragmenta los documentos utilizando
        RecursiveCharacterTextSplitter.
        """

        chunks = self.splitter.split_documents(documents)

        return chunks


    def _enrich_metadata(self, chunks):
        """
        Enriquece la metadata de cada chunk.
        """

        total_chunks = len(chunks)

        for index, chunk in enumerate(chunks):

            chunk.metadata["chunk_index"] = index

            chunk.metadata["total_chunks"] = total_chunks

            chunk.metadata["chunk_size"] = len(chunk.page_content)

            chunk.metadata["splitter_version"] = self.version

        return chunks

    def split_documents(self, documents):
        """
        Fragmenta una colección de documentos.
        """

        self._validate_documents(documents)

        chunks = self._split(documents)

        chunks = self._enrich_metadata(chunks)

        return chunks