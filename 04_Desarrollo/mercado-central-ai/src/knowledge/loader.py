"""
Document Loader
Proyecto: Mercado Central AI

Responsabilidad:
Cargar los documentos PDF oficiales desde la Base de Conocimiento.

Versión actual:
    - PDF

Versiones futuras:
    - DOCX
    - TXT
    - XLSX
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from src.config.settings import PDF_DIR


class DocumentLoader:
    """
    Document Loader.

    Responsable de cargar los documentos oficiales
    de la Base de Conocimiento y convertirlos en
    objetos Document de LangChain.
    """

    def __init__(self):
        self.pdf_directory = PDF_DIR

    def get_pdf_files(self) -> List[Path]:
        """
        Obtiene todos los archivos PDF disponibles
        en la Base de Conocimiento.

        Returns:
            Lista de rutas Path.
        """

        if not self.pdf_directory.exists():
            raise FileNotFoundError(
                f"No existe la carpeta: {self.pdf_directory}"
            )

        pdf_files = sorted(self.pdf_directory.glob("*.pdf"))

        return pdf_files

    def load_pdf(self, pdf_path: Path) -> List[Document]:
        """
        Carga un único archivo PDF.

        Args:
            pdf_path: Ruta del archivo PDF.

        Returns:
            Lista de objetos Document.
        """

        loader = PyPDFLoader(str(pdf_path))

        documents = loader.load()

        documents = self._enrich_metadata(
            documents,
            pdf_path,
        )

        return documents
   
    def load_all(self) -> List[Document]:
        """
        Carga todos los documentos PDF encontrados.

        Returns:
            Lista completa de objetos Document.
        """

        documents: List[Document] = []

        processed = 0
        errors = 0

        pdf_files = self.get_pdf_files()

        if not pdf_files:

            print("No se encontraron archivos PDF.")

            return documents

        print(f"\nPDF encontrados: {len(pdf_files)}\n")

        for pdf in pdf_files:

            print(f"Cargando: {pdf.name}")

            try:

                documents.extend(self.load_pdf(pdf))

                processed += 1

            except Exception as error:

                errors += 1

                print(f"Error leyendo {pdf.name}")

                print(error)

        print("\n" + "=" * 45)
        print("Carga finalizada")
        print(f"PDF procesados : {processed}")
        print(f"Documentos     : {len(documents)}")
        print(f"Errores        : {errors}")
        print("=" * 45)

        return documents


    def _enrich_metadata(
        self,
        documents: List[Document],
        pdf_path: Path,
    ) -> List[Document]:
        """
        Enriquece la metadata básica de los documentos cargados.

        Args:
            documents: Lista de documentos cargados.
            pdf_path: Ruta del archivo PDF.

        Returns:
            Lista de documentos con metadata enriquecida.
        """

        for document in documents:

            document.metadata["file_name"] = pdf_path.name

            document.metadata["file_type"] = (
                pdf_path.suffix.lower().replace(".", "")
            )

        return documents

