print("=== Inicio del test ===")

from src.knowledge.loader import DocumentLoader

print("Clase importada correctamente")

loader = DocumentLoader()

print("Loader creado")

print("Ruta PDF:", loader.pdf_directory)

documents = loader.load_all()

print("Cantidad de documentos:", len(documents))

print("=== Fin del test ===")