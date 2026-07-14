"""
=========================================================
Knowledge Initializer.

Responsable de construir la Base Vectorial del proyecto.

Pipeline:

PDF
    ↓
Document Loader
    ↓
Text Splitter
    ↓
Metadata Manager
    ↓
Embeddings
    ↓
Document Mapper
    ↓
Vector Store

Sprint 14 - Hito 12
=========================================================
"""

from src.knowledge.loader import DocumentLoader

from src.knowledge.text_splitter import TextSplitter

from src.knowledge.metadata import MetadataManager

from src.knowledge.embeddings import Embeddings

from src.knowledge.document_mapper import DocumentMapper

from src.knowledge.vector_store import VectorStore

from src.knowledge.providers.chroma_provider import ChromaProvider


class KnowledgeInitializer:
    """
    Inicializa completamente la Base Vectorial.
    """

    def __init__(self) -> None:
        """
        Inicializa todos los componentes del pipeline.
        """

        self._loader = DocumentLoader()

        self._splitter = TextSplitter()

        self._metadata = MetadataManager()

        self._embeddings = Embeddings()

        self._mapper = DocumentMapper()

        self._provider = ChromaProvider()

        self._vector_store = VectorStore(
            self._provider
        )
    
    def _load_documents(self):
        """
        Carga todos los documentos desde el directorio configurado.
        """
        print("📄 Cargando documentos...")

        documents = self._loader.load_all()

        print(f"   ✓ Documentos cargados: {len(documents)}")

        return documents

    def _split_documents(self, documents):
        """
        Divide los documentos en chunks.
        """
        print("✂️ Dividiendo documentos...")

        chunks = self._splitter.split_documents(
            documents
        )

        print(f"   ✓ Chunks generados: {len(chunks)}")

        return chunks

    def _process_metadata(self, chunks):
        """
        Procesa el metadata de cada chunk.
        """
        print("🏷️ Procesando metadata...")

        processed = self._metadata.process_documents(
            chunks
        )

        print(f"   ✓ Metadata procesada: {len(processed)}")

        return processed

    def _generate_embeddings(self, documents):
        """
        Genera embeddings para todos los documentos.
        """
        print("🧠 Generando embeddings...")

        embedded = self._embeddings.generate_embeddings(
            documents
        )

        print(f"   ✓ Embeddings generados: {len(embedded)}")

        return embedded

    def _map_documents(self, embedded_documents):
        """
        Convierte los documentos al modelo interno utilizado
        por el Vector Store.
        """
        print("🗂️ Construyendo documentos vectoriales...")

        mapped = self._mapper.map_documents(
            embedded_documents
        )

        print(f"   ✓ Documentos preparados: {len(mapped)}")

        return mapped

    def _store_documents(self, documents):
        """
        Guarda todos los documentos en la colección vectorial.
        """
        print("💾 Guardando documentos en Chroma...")

        self._vector_store.add_documents(
            documents
        )

        total = self._vector_store.count_documents()

        print(f"   ✓ Documentos almacenados: {total}")

        return total
    
    def run(self) -> None:
        """
        Ejecuta todo el pipeline de construcción de la Base Vectorial.
        """

        print("\nInicializando Base Vectorial...\n")

        try:

            # 1. Cargar documentos
            documents = self._load_documents()

            if not documents:
                print("No se encontraron documentos.")
                return

            # 2. Dividir documentos
            chunks = self._split_documents(documents)

            if not chunks:
                print("No fue posible generar chunks.")
                return

            # 3. Procesar metadata
            metadata_documents = self._process_metadata(chunks)

            # 4. Generar embeddings
            embedded_documents = self._generate_embeddings(
                metadata_documents
            )

            # 5. Mapear documentos
            vector_documents = self._map_documents(
                embedded_documents
            )

            # 6. Reiniciar colección
            print("Limpiando colección existente...")
            self._vector_store.reset()

            # 7. Guardar documentos
            self._store_documents(vector_documents)

            # 8. Verificación
            final_total = self._vector_store.count_documents()

            print(f"Base vectorial inicializada correctamente ({final_total} documentos).")

        except Exception as error:

            print(f"Error inicializando la Base Vectorial: {error}")
            raise
    
if __name__ == "__main__":
    initializer = KnowledgeInitializer()
    initializer.run()