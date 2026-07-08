# Changelog

Todos los cambios relevantes del proyecto se documentarán en este
archivo.

## \[0.1.0\] - 2026-06-30

### Added

-   Estructura base del proyecto.
-   Configuración del entorno virtual (.venv).
-   Configuración centralizada mediante `settings.py`.
-   Implementación del `DocumentLoader`.
-   Prueba funcional del Loader (4 PDF / 124 documentos).
-   Documentación H1 (DOC, SDS, INST, MTR, LOG, ADR, HANDBOOK).


## \[0.6.0\] - 2026-07-08

### Added

- Implementación del módulo Retriever.
- Implementación de la interfaz `IRetriever`.
- Implementación de `ChromaRetriever`.
- Implementación de `RetrieverFactory`.
- Integración del Retriever con `VectorStore`.
- Configuración centralizada mediante:
  - `RETRIEVER_TOP_K`
  - `RETRIEVER_VALIDATE_QUERY`
- Incorporación del paquete `src/retriever/`.
- Incorporación de `tests/test_retriever.py`.

### Changed

- Actualización de `settings.py` con la configuración del Retriever.
- Actualización del README del proyecto.
- Actualización del PLAN-006.
- Actualización del SDS-006.
- Actualización del MTR-001.
- Estandarización del uso de imports con el prefijo `src.` entre paquetes.
- Definición del primer Factory Pattern oficial del proyecto.

### Fixed

- Corrección de imports entre paquetes utilizando el estándar `src.`.
- Implementación de la interfaz `IRetriever` faltante.
- Eliminación de valores hardcodeados (*magic numbers*) del módulo Retriever.

### Validated

- Implementación completa de `IRetriever`.
- Implementación completa de `ChromaRetriever`.
- Validación de integración con `VectorStore`.
- Validación de `RetrieverFactory`.
- Configuración centralizada verificada.
- Ejecución satisfactoria de **18 pruebas automatizadas (18 passed)**.
- Compatibilidad total con los Sprint 3 al 7.

### Pipeline actualizado

```text
Knowledge Base
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Metadata Manager
      │
      ▼
Embeddings Engine
      │
      ▼
Vector Store
      │
      ▼
Retriever
