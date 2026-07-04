# Changelog

#----------------------------------------------------------------------------------------------------------------
Este documento registra los cambios relevantes realizados en el proyecto siguiendo las recomendaciones de Keep a Changelog y versionado semántico adaptado al Challenge Alura + Oracle Next Education.
#----------------------------------------------------------------------------------------------------------------




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
Embeddings
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