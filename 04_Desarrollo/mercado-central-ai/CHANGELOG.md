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
```


## \[0.8.0\] - 2026-07-10

### Added

- Implementación del módulo Decision Engine.
- Implementación de DecisionEngineInterface.
- Implementación del modelo LLMRequest.
- Implementación de DecisionEngine.
- Implementación de DecisionEngineFactory.
- Preparación del pipeline para proveedores LLM desacoplados.
- Pruebas automatizadas del módulo.
- Archivo tests/test_models.py.
- Archivo tests/test_decision_engine.py.
- Archivo tests/test_decision_engine_factory.py.
- Cuatro nuevos casos de prueba automatizados.

### Changed

- Actualización del README.
- Actualización del PLAN-008.
- Actualización del SDS-008_Decision_Engine.md.
- Actualización del HANDBOOK.
- Actualización del ROADMAP.
- Actualización del MTR-001.
- Actualización del LOG.
- Actualización del pipeline RAG incorporando el Decision Engine.
- Consolidación de la arquitectura desacoplada entre Context Builder y el proveedor LLM mediante LLMRequest.

### Fixed

- 

### Validated

- Construcción correcta de objetos LLMRequest.
- Validación de DecisionEngine.
- Validación de DecisionEngineFactory.
- Ejecución satisfactoria de 29 pruebas automatizadas.
- Validación arquitectónica del desacoplamiento entre Context Builder, Decision Engine y el futuro proveedor LLM.

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
      │
      ▼
Context Builder
      │
      ▼
Decision Engine
      │
      ▼
LLM Provider
