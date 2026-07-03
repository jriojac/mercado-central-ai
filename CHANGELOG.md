# Changelog


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