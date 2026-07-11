# Changelog

#----------------------------------------------------------------------------------------------------------------
Este documento registra los cambios relevantes realizados en el proyecto siguiendo las recomendaciones de Keep a Changelog y versionado semántico adaptado al Challenge Alura + Oracle Next Education.
#----------------------------------------------------------------------------------------------------------------

## Convención utilizada

Este documento sigue las recomendaciones de **Keep a Changelog**, adaptadas al ciclo de desarrollo incremental del proyecto.

Cada Release registra:

- Funcionalidades incorporadas (**Added**).
- Cambios relevantes (**Changed**).
- Correcciones (**Fixed**, cuando aplique).
- Validaciones realizadas (**Validated**).

Las versiones se publican al cierre de cada Sprint/Hito estable del proyecto.



## [0.9.0] - 2026-07-11

### Added

- Implementación del módulo **Tools**.
- Implementación de `ToolInterface`.
- Implementación de `ToolManagerInterface`.
- Implementación de `ToolManager`.
- Implementación de `ToolFactory`.
- Incorporación de `DuplicateToolError`.
- Incorporación de `DummyTool` para pruebas unitarias.
- Registro y administración de herramientas mediante `ToolManager`.
- Ejecución de herramientas a través de una interfaz desacoplada.
- Preparación de la arquitectura para futuras herramientas especializadas (FAQ, Inventario, Políticas, entre otras).
- Pruebas automatizadas mediante `pytest`.
- Archivos:
  - `tests/test_tools_interface.py`
  - `tests/test_tool_manager.py`
  - `tests/test_tool_factory.py`

### Changed

- Actualización del `README.md`.
- Actualización de `PLAN-009`.
- Actualización de `SDS-009_Tools.md`.
- Actualización del `HANDBOOK`.
- Actualización del `ROADMAP`.
- Actualización de `MTR-001`.
- Actualización del `LOG`.
- Actualización del pipeline RAG incorporando la infraestructura del módulo **Tools**.
- Consolidación de la arquitectura basada en interfaces y Factory Pattern para el registro y ejecución de herramientas.
- Incorporación de `ToolManagerInterface` para mantener el desacoplamiento entre consumidores e implementación.
- Incorporación del método `has_tool()` para preservar el encapsulamiento y eliminar el acceso directo al estado interno del `ToolManager`.

### Validated

- Registro correcto de herramientas.
- Validación del contrato `ToolInterface`.
- Validación del contrato `ToolManagerInterface`.
- Validación de `ToolManager`.
- Validación de `ToolFactory`.
- Detección de registros duplicados mediante `DuplicateToolError`.
- Ejecución de herramientas registradas.
- Validación del comportamiento cuando ninguna herramienta puede atender una consulta.
- Ejecución satisfactoria de las pruebas automatizadas.
- Validación arquitectónica del desacoplamiento entre el Decision Engine y el módulo Tools.

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
Tool Manager
```



## [0.8.0] - 2026-07-10

### Added

- Implementación del módulo Decision Engine.
- Implementación de `DecisionEngineInterface`.
- Implementación de `DecisionEngine`.
- Implementación de `DecisionEngineFactory`.
- Implementación del modelo `LLMRequest`.
- Construcción de solicitudes desacopladas del proveedor LLM.
- Preparación de la arquitectura para soportar múltiples proveedores LLM.
- Pruebas automatizadas mediante `pytest`.
- Archivos:
  - `tests/test_models.py`
  - `tests/test_decision_engine.py`
  - `tests/test_decision_engine_factory.py`

### Changed

- Actualización del `README.md`.
- Actualización de `PLAN-008`.
- Actualización de `SDS-008_Decision_Engine.md`.
- Actualización del `HANDBOOK`.
- Actualización del `ROADMAP`.
- Actualización de `MTR-001`.
- Actualización del `LOG`.
- Actualización del pipeline RAG incorporando el módulo Decision Engine.
- Consolidación de la arquitectura basada en interfaces y Factory Pattern para el módulo LLM.

### Validated

- Construcción correcta de `LLMRequest`.
- Validación de `DecisionEngine`.
- Validación de `DecisionEngineFactory`.
- Construcción desacoplada de solicitudes para proveedores LLM.
- Ejecución satisfactoria de las pruebas automatizadas.
- Validación arquitectónica del desacoplamiento entre Context Builder y Decision Engine.

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
```

## [0.7.0] - 2026-07-09

### Added

- Implementación del módulo Context Builder.
- Implementación de ContextBuilderInterface.
- Implementación de SimpleContextBuilder.
- Implementación de ContextBuilderFactory.
- Construcción de contexto textual a partir de documentos recuperados.
- Preservación del orden de relevancia entregado por el Retriever.
- Configuración centralizada del Context Builder mediante settings.py.
- Incorporación de CONTEXT_SEPARATOR.
- Incorporación de MAX_CONTEXT_CHARS.
- Incorporación de INCLUDE_METADATA.
- Pruebas automatizadas mediante pytest.
- Archivo tests/test_context_builder.py.
- Seis nuevos casos de prueba automatizados (CP-040 a CP-045).

### Changed

- Actualización de README.md.
- Actualización de PLAN-007.
- Actualización de SDS-007_Context_Builder.md.
- Actualización de HANDBOOK.
- Actualización de ROADMAP.
- Actualización de MTR-001.
- Actualización de LOG.
- Actualización del pipeline RAG incorporando el módulo Context Builder.
- Consolidación de la arquitectura basada en interfaces y Factory Pattern para el nuevo módulo.


### Validated

- Construcción de contexto con documentos válidos.
- Construcción de contexto vacío.
- Preservación del orden recibido del Retriever.
- Exclusión de documentos sin contenido.
- Validación de ContextBuilderFactory.
- Ejecución satisfactoria de todas las pruebas automatizadas del módulo.
- Validación arquitectónica del desacoplamiento entre Retriever, Context Builder y Decision Engine.

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

```


## [0.6.0] - 2026-07-08

### Added

- Implementación del módulo Retriever.
- Definición de RetrieverInterface.
- Implementación de ChromaRetriever.
- Implementación de RetrieverFactory.
- Integración con ChromaDB para recuperación por similitud.
- Configuración centralizada del Retriever.
- Pruebas automatizadas del módulo.

### Changed
- Actualización del pipeline RAG incorporando el módulo Retriever.
- Actualización del README.
- Actualización del SDS-006.
- Actualización del PLAN-006.
- Actualización del HANDBOOK.
- Actualización del MTR.
- Actualización del ROADMAP.

### Validated

-  Recuperación de documentos por similitud.
-  Validación de consultas.
-  Integración Vector Store → Retriever.
-  Ejecución satisfactoria de las pruebas automatizadas del módulo.
-  Validación de la arquitectura basada en interfaces.

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


## [0.5.0] - 2026-07-05

### Added

- Implementación del módulo Vector Store.
- Implementación de la interfaz VectorStoreProvider.
- Implementación de ChromaProvider como proveedor de almacenamiento vectorial.
- Integración con ChromaDB para la persistencia local de documentos vectoriales.
- Implementación del modelo VectorDocument.
- Implementación del modelo SearchResult.
- Incorporación de provider.py.
- Incorporación de constants.py.
- Administración de colecciones vectoriales.
- Inserción de documentos vectoriales.
- Búsquedas por similitud (similarity_search()).
- Eliminación de documentos (delete_documents()).
- Reinicio completo de colecciones (reset()).
- Conteo de documentos (count_documents()).
- Persistencia local del Vector Store.
- Pruebas automatizadas mediante pytest.
- Archivo tests/test_vector_store.py.
- Ocho casos de prueba automatizados (CP-501 a CP-508).

### Changed

- Actualización de settings.py para incorporar la configuración del Vector Store.
- Actualización del README del proyecto.
- Actualización de la Matriz de Trazabilidad (MTR-001).
- Actualización de LOG-001_Bitacora_Tecnica.md.
- Actualización de SDS-005_Vector_Store.md.
- Actualización del pipeline RAG incorporando el módulo Vector Store.
- Refactorización de la suite de pruebas mediante pytest.fixture.
- Estandarización de la interfaz VectorStoreProvider.
- Separación entre la interfaz pública y la implementación específica del proveedor ChromaDB.

### Validated

- Creación de colecciones vectoriales.
- Carga de colecciones existentes.
- Inserción de documentos vectoriales.
- Persistencia local mediante ChromaDB.
- Conteo de documentos almacenados.
- Búsquedas por similitud.
- Eliminación de documentos.
- Reinicio completo de colecciones.
- Ejecución satisfactoria de las ocho pruebas automatizadas (8 passed).
- Validación completa de la interfaz pública del módulo.

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
```

---

## [0.4.0] - 2026-07-04

### Added

- Implementación del módulo **Embeddings**.
- Implementación de la clase `EmbeddingProvider`.
- Integración con **Google Generative AI**.
- Soporte para el modelo `gemini-embedding-2`.
- Configuración mediante archivo `.env`.
- Incorporación de la variable `GOOGLE_API_KEY`.
- Script de integración `temp/check_pipeline_embeddings.py`.
- Generación de embeddings para documentos.
- Generación de embeddings para consultas.
- Validación de configuración antes de inicializar el proveedor.

### Changed

- Actualización de `settings.py` para incorporar la configuración del proveedor de embeddings.
- Actualización de `exceptions.py` con excepciones específicas para Embeddings.
- Actualización del documento `SDS-004_Embeddings.md`.
- Actualización de `LOG-001_Bitacora_Tecnica.md`.
- Actualización del pipeline RAG incorporando el módulo Embeddings.
- Optimización del script de integración utilizando una muestra representativa de documentos para respetar las restricciones del nivel gratuito de Google Generative AI.

### Validated

- Inicialización del proveedor de embeddings.
- Lectura correcta de la configuración desde `.env`.
- Validación de `GOOGLE_API_KEY`.
- Integración Metadata Manager → Embeddings.
- Generación satisfactoria de embeddings mediante Google Generative AI.
- Validación del pipeline completo:

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
```

- Generación exitosa de embeddings de **3072 dimensiones**.
- Ejecución satisfactoria de `check_pipeline_embeddings.py`.
- Pipeline RAG completado correctamente.

---

## [0.3.0] - 2026-07-03

### Added

- Implementación del módulo **Metadata Manager**.
- Validación de metadata obligatoria.
- Normalización automática de metadata.
- Enriquecimiento automático de metadata.
- Incorporación de `document_id`.
- Incorporación de `ingest_date`.
- Incorporación de `pipeline_version`.
- Incorporación de `language`.
- Incorporación de `category`.
- Archivo `src/core/exceptions.py` para centralizar las excepciones del proyecto.
- Script de integración `check_metadata.py`.
- Pruebas automatizadas mediante `pytest`.
- Archivo `tests/test_metadata.py`.
- Nueve casos de prueba (CP-001 a CP-009).

### Changed

- Actualización del README del proyecto.
- Actualización del HANDBOOK con la estrategia oficial de pruebas.
- Actualización de la Matriz de Trazabilidad (MTR).
- Actualización del LOG del proyecto.
- Incorporación del DOC-016 correspondiente al Metadata Manager.
- Actualización del SDS-003.
- Actualización del pipeline RAG incorporando el Metadata Manager.
- Incorporación oficial de la metodología de Casos de Prueba (CP).
- Separación entre scripts locales de validación (`temp/`) utilizados durante el desarrollo y pruebas automatizadas oficiales (`tests/`) versionadas en el repositorio.
- Adopción oficial de `pytest` como framework de pruebas del proyecto.
- Estandarización del uso de `python -m pip` para la instalación de dependencias.

### Validated

- Validación de metadata obligatoria.
- Validación de colecciones de documentos.
- Normalización de metadata.
- Enriquecimiento automático de metadata.
- Integración Text Splitter → Metadata Manager.
- Ejecución satisfactoria de `check_metadata.py`.
- Ejecución satisfactoria de `test_metadata.py`.
- **9 casos de prueba aprobados (9 passed).**

---

## [0.2.0] - 2026-07-02

### Added

- Implementación del módulo **Text Splitter**.
- Integración de `RecursiveCharacterTextSplitter`.
- Configuración centralizada mediante `settings.py`.
- Enriquecimiento de metadata de los chunks.
- Scripts de validación:
  - `check_text_splitter`
  - `check_loader_splitter`
- Integración entre Document Loader y Text Splitter.

### Changed

- Actualización del README del proyecto.
- Actualización del LOG del proyecto.
- Actualización de la Matriz de Trazabilidad (MTR).
- Incorporación de la documentación funcional del Hito 2.
- Actualización del estado del pipeline RAG.

### Validated

- Pruebas unitarias del Text Splitter.
- Pruebas de integración Loader → Text Splitter.
- Validación de documentos reales de la Knowledge Base.
- Generación correcta de 367 chunks sin errores.

---

## [0.1.1] - 2026-07-01

### Changed

- Se reorganizó la documentación del repositorio.
- Se agregó README principal en la raíz.
- Se consolidó la estructura documental del Hito 1.
- Se cerró oficialmente el Sprint 3.

---

## [0.1.0] - 2026-06-30

### Added

- Configuración del entorno.
- Document Loader.
- Pruebas funcionales.
- Documentación inicial.
- Versionado Git.