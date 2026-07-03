# LOG-001 -- Bitácora Técnica

## 2026-07-01 -- Cierre del Hito 1

### Actividades realizadas

-   Finalización del módulo `DocumentLoader`.
-   Validación de la Base de Conocimiento.
-   Integración de 4 documentos PDF.
-   Carga exitosa de 124 objetos `Document`.
-   Refactorización de `loader.py`.
-   Ejecución de pruebas funcionales.
-   Configuración de Git y GitHub.
-   Creación de los tags `v0.1.0` y `v0.1.1`.
-   Consolidación de la documentación.

### Resultado

**Hito 1 finalizado satisfactoriamente.**

Estado del proyecto:

-   Loader operativo.
-   Base de Conocimiento integrada.
-   Proyecto documentado y versionado.
-   Listo para iniciar el Sprint 4.

# Registro de Avances (LOG)

---

## Sprint 4 – Hito 2

## 2026-07-01 -- Cierre del Hito 2

### Módulo
Text Splitter

### Estado
Finalizado

### Actividades realizadas

- Implementación de la clase `TextSplitter`.
- Integración de `RecursiveCharacterTextSplitter`.
- Lectura de configuración desde `settings.py`.
- Implementación de validación de documentos de entrada.
- Implementación de la fragmentación de documentos.
- Implementación del enriquecimiento de metadata de los chunks.
- Integración con el módulo `DocumentLoader`.
- Validación mediante pruebas unitarias y de integración.

### Resultados

- Fragmentación correcta de documentos.
- Conservación de metadata original.
- Incorporación de metadata enriquecida:
  - `chunk_index`
  - `total_chunks`
  - `chunk_size`
  - `splitter_version`
- Generación correcta de chunks para documentos reales de la Knowledge Base.

### Evidencias

#### check_text_splitter

- Validación de inicialización.
- Validación de errores.
- Documento corto.
- Documento largo.
- Metadata enriquecida.

#### check_loader_splitter

- Integración Document Loader → Text Splitter.
- 4 PDFs procesados.
- 124 documentos cargados.
- 367 chunks generados.
- 0 errores.

### Estado final

Sprint 4 – Hito 2 listo para documentación final, control de versiones y preparación de la Release v0.2.0.

---