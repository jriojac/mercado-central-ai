# SDS-003
# Software Design Specification
## Metadata Manager

---

# 1. Información del documento

| Campo | Valor |
|--------|-------|
| Documento | SDS-003 |
| Título | Software Design Specification – Metadata Manager |
| Versión | 1.0 |
| Estado | En desarrollo |
| Sprint | 5 |
| Hito | 3 |
| Módulo | Metadata Manager |
| Release objetivo | v0.3.0 |
| Autor | Jacqueline Rioja |
| Fecha | 02/07/2026 |
| Última actualización | 02/07/2026 |

---

# 2. Objetivo

Describe el propósito del módulo Metadata Manager.

Debe responder las siguientes preguntas:

- ¿Por qué existe este módulo?
- ¿Qué problema resuelve?
- ¿Cuál es su función dentro del pipeline RAG?
- ¿Qué información entrega al siguiente módulo?

---

# 3. Alcance

## Incluye

- Recepción de chunks provenientes del Text Splitter.
- Validación de metadata.
- Normalización de metadata.
- Enriquecimiento de metadata.
- Entrega de documentos listos para generar embeddings.

## No incluye

- Generación de embeddings.
- Almacenamiento en Vector Store.
- Recuperación de información.
- Consultas al modelo LLM.
- Procesamiento de prompts.

---

# 4. Referencias

Documentos relacionados:

- HANDBOOK
- ROADMAP
- README
- CHANGELOG
- MTR
- SDS-002 (Text Splitter)

---

# 5. Contexto dentro del Pipeline RAG

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
Gemini
```

## Entrada

Colección de objetos `Document`.

## Salida

Colección de objetos `Document` con metadata validada, normalizada y enriquecida.

---

# 6. Requerimientos funcionales

## RF-011

Recibir la colección de chunks generados por el Text Splitter.

### Entrada

Lista de objetos Document.

### Proceso

Validar estructura recibida.

### Salida

Colección preparada para validación.

---

## RF-012

Validar metadata mínima requerida.

Campos mínimos:

- source
- file_name
- file_type
- chunk_index
- total_chunks
- chunk_size
- splitter_version

---

## RF-013

Normalizar la metadata para mantener un formato consistente.

---

## RF-014

Agregar metadata adicional.

Ejemplo:

- document_id
- ingest_date
- pipeline_version
- language
- category

---

## RF-015

Entregar la colección lista para el módulo Embeddings.

---

# 7. Responsabilidades del módulo

El Metadata Manager será responsable de:

- Recibir documentos.
- Validar metadata.
- Completar metadata cuando sea posible.
- Normalizar formatos.
- Enriquecer metadata.
- Retornar la colección procesada.

---

# 8. Arquitectura del módulo

```text
Text Splitter
      │
      ▼
Metadata Manager
      │
 ┌────┴─────────┐
 │              │
Validación
Normalización
Enriquecimiento
      │
      ▼
Embeddings
```

---

# 9. Flujo de procesamiento

```text
Recibir Document

        │

        ▼

Validar Metadata

        │

        ▼

Normalizar

        │

        ▼

Agregar Metadata

        │

        ▼

Verificar Resultado

        │

        ▼

Retornar Colección
```

---

# 10. Modelo de datos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| source | str | Sí | Ruta del documento |
| file_name | str | Sí | Nombre del archivo |
| file_type | str | Sí | Tipo de archivo |
| chunk_index | int | Sí | Posición del chunk |
| total_chunks | int | Sí | Total de chunks |
| chunk_size | int | Sí | Tamaño del chunk |
| splitter_version | str | Sí | Versión del splitter |
| document_id | str | Sí | Identificador único |
| ingest_date | datetime | Sí | Fecha de ingestión |
| pipeline_version | str | Sí | Versión del pipeline |
| language | str | No | Idioma |
| category | str | No | Categoría documental |

---

# 11. Diseño de clases

## Clase principal

```python
class MetadataManager:
```

### Responsabilidad

Administrar la metadata asociada a cada chunk antes de la generación de embeddings.

---

# 12. Interfaces públicas

```python
process_documents()

validate_metadata()

normalize_metadata()

enrich_metadata()
```

---

# 13. Reglas de validación

Validaciones mínimas:

- source obligatorio
- file_name obligatorio
- file_type obligatorio
- chunk_index >= 0
- total_chunks > 0
- chunk_size > 0
- splitter_version obligatorio

---

# 14. Reglas de normalización

Ejemplos:

```
PDF
↓
pdf
```

```
Docx
↓
docx
```

```
Documento.PDF
↓
documento.pdf
```

```
Rutas Windows
↓
Formato estándar
```

---

# 15. Metadata enriquecida

Campos agregados automáticamente:

- document_id
- ingest_date
- pipeline_version
- language
- category

Debe documentarse:

- origen
- formato
- finalidad

---

# 16. Manejo de errores

Excepciones previstas:

- MetadataValidationError
- MissingMetadataError
- InvalidChunkError

Cada excepción debe indicar:

- causa
- impacto
- acción correctiva

---

# 17. Logging

Registrar:

- Inicio del procesamiento.
- Fin del procesamiento.
- Cantidad de documentos.
- Cantidad de chunks.
- Advertencias.
- Errores.

---

# 18. Consideraciones de rendimiento

Objetivos:

- Complejidad O(n).
- Evitar copias innecesarias.
- Modificar metadata en memoria.
- Reducir consumo de memoria.

---

# 19. Extensibilidad

La arquitectura deberá permitir incorporar nuevos campos sin modificar el pipeline.

Ejemplos:

- author
- department
- tags
- country
- version
- security_level

---

# 20. Casos de Prueba

La validación del módulo **Metadata Manager** se realizará mediante pruebas automatizadas utilizando **pytest**.

Cada caso de prueba mantiene trazabilidad con los requisitos funcionales definidos para el módulo.

| Caso | Requisito | Objetivo | Resultado esperado |
|------|-----------|----------|--------------------|
| CP-001 | RF-011 | Procesar una colección válida de objetos `Document`. | La colección se procesa sin errores. |
| CP-002 | RF-012 | Validar un documento con metadata completa. | La validación finaliza correctamente. |
| CP-003 | RF-012 | Validar un documento con metadata incompleta. | Se genera `MissingMetadataError`. |
| CP-004 | RF-013 | Verificar la normalización de la metadata. | Los campos se normalizan según las reglas definidas. |
| CP-005 | RF-014 | Verificar el enriquecimiento automático de metadata. | Se agregan `document_id`, `ingest_date`, `pipeline_version`, `language` y `category`. |
| CP-006 | RF-015 | Procesar una colección vacía. | Se devuelve una lista vacía sin generar excepciones. |
| CP-007 | RF-015 | Procesar una entrada que no sea una lista. | Se genera una excepción por tipo de dato inválido. |
| CP-008 | RF-015 | Procesar una colección con elementos que no sean objetos `Document`. | Se genera una excepción indicando el tipo inválido. |
| CP-009 | RF-015 | Ejecutar el flujo completo del módulo. | Los documentos quedan listos para el módulo Embeddings. |

---

## Cobertura de pruebas

La siguiente matriz muestra la relación entre los requisitos funcionales y los casos de prueba.

| Requisito | Casos de prueba |
|-----------|-----------------|
| RF-011 | CP-001 |
| RF-012 | CP-002, CP-003 |
| RF-013 | CP-004 |
| RF-014 | CP-005 |
| RF-015 | CP-006, CP-007, CP-008, CP-009 |

---

## Herramienta de pruebas

Las pruebas funcionales del proyecto se implementan utilizando **pytest**.

Las pruebas de integración rápida continúan ejecutándose mediante los scripts ubicados en:

Herramientas y scripts de apoyo para el desarrollo (locales, no forman parte de la Release)

```text
temp/
```


Las pruebas automatizadas se ubican en:

```text
tests/
```

Ejemplos de ejecución:

```bash
python -m pytest
```

```bash
python -m pytest tests
```

```bash
python -m pytest tests/test_metadata.py
```




---

# 21. Trazabilidad

| RF | Clase | Método | Implementación | Caso de prueba |
|----|--------|---------|----------------|----------------|
| RF-011 | MetadataManager | process_documents | IMP-02 | CP-001 |
| RF-012 | MetadataManager | _validate_metadata | IMP-02 | CP-002, CP-003 |
| RF-013 | MetadataManager | _normalize_metadata | IMP-03 | CP-004 |
| RF-014 | MetadataManager | _enrich_metadata | IMP-04 | CP-005 |
| RF-015 | MetadataManager | process_documents | IMP-05 | CP-006, CP-007, CP-008, CP-009 |

---

# 22. Riesgos técnicos

- Metadata incompleta.
- Cambios futuros en LangChain.
- Cambios en Document.metadata.
- Incremento del tamaño de metadata.
- Compatibilidad con futuras versiones del pipeline.

---

# 23. Estado de implementación

| Implementación | Estado | RF |
|---------------|--------|----|
| IMP-01 | ✅ | Estructura base |
| IMP-02 | ✅ | RF-011, RF-012 |
| IMP-03 | ✅ | RF-013 |
| IMP-04 | ⏳ | RF-014 |
| IMP-05 | ⏳ | RF-015 |


---

# 24. Control de versiones

| Versión | Fecha | Autor | Cambios |
|----------|--------|--------|----------|
| 1.0 | 02/07/2026 | Jacqueline Rioja | Creación inicial del documento. |