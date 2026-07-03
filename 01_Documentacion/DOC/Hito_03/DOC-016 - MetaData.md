# DOC-016

# Metadata Manager

## Sprint 5 – Hito 3

---

# 1. Objetivo

Implementar el módulo **Metadata Manager** del pipeline RAG, responsable de validar, normalizar y enriquecer la metadata asociada a cada chunk generado por el Text Splitter, preparando la información para el módulo Embeddings.

---

# 2. Alcance

El módulo es responsable de:

- Recibir la colección de chunks generados por el Text Splitter.
- Validar la metadata mínima requerida.
- Normalizar la información de la metadata.
- Enriquecer automáticamente la metadata.
- Preparar los documentos para el módulo Embeddings.

No forma parte de este módulo:

- Generación de embeddings.
- Almacenamiento vectorial.
- Recuperación de contexto.
- Generación de respuestas mediante LLM.

---

# 3. Arquitectura

El módulo ocupa la siguiente posición dentro del pipeline RAG.

```text
Knowledge Base
      ↓
Document Loader
      ↓
Text Splitter
      ↓
Metadata Manager
      ↓
Embeddings
      ↓
Vector Store
      ↓
Retriever
      ↓
Context Builder
      ↓
Gemini
      ↓
Respuesta
```

---

# 4. Componentes

La implementación está compuesta por:

## Clase principal

```text
MetadataManager
```

Métodos implementados:

- `__init__()`
- `_validate_documents()`
- `_validate_metadata()`
- `_normalize_metadata()`
- `_enrich_metadata()`
- `process_documents()`

---

## Excepciones

El módulo utiliza excepciones compartidas definidas en:

```text
src/core/exceptions.py
```

Actualmente se emplean excepciones para validar:

- metadata obligatoria;
- documentos inválidos;
- errores de procesamiento.

---

# 5. Flujo de procesamiento

```text
Colección de Document

        │

        ▼

Validación de documentos

        │

        ▼

Validación de metadata

        │

        ▼

Normalización

        │

        ▼

Enriquecimiento

        │

        ▼

Colección preparada para Embeddings
```

---

# 6. Metadata administrada

## Metadata obligatoria

| Campo | Descripción |
|--------|-------------|
| source | Ruta del documento original |
| file_name | Nombre del archivo |
| file_type | Tipo de archivo |
| chunk_index | Índice del chunk |
| total_chunks | Cantidad total de chunks |
| chunk_size | Tamaño del chunk |
| splitter_version | Versión del Text Splitter |

---

## Metadata enriquecida

| Campo | Descripción |
|--------|-------------|
| document_id | Identificador único del documento |
| ingest_date | Fecha de incorporación al pipeline |
| pipeline_version | Versión del pipeline |
| language | Idioma del documento |
| category | Categoría del documento |

---

# 7. Configuración

La configuración del módulo se centraliza en:

```text
src/config/settings.py
```

Entre los parámetros utilizados se encuentran:

- PROJECT_VERSION
- DEFAULT_LANGUAGE
- DEFAULT_CATEGORY

---

# 8. Validaciones implementadas

El módulo valida:

- colección vacía;
- tipo de dato incorrecto;
- objetos distintos de `Document`;
- metadata incompleta;
- campos obligatorios ausentes.

Las validaciones se ejecutan antes del enriquecimiento de la metadata.

---

# 9. Resultados obtenidos

Durante las pruebas se verificó:

- Validación correcta de metadata.
- Normalización automática.
- Enriquecimiento automático.
- Integración con Text Splitter.
- Compatibilidad con Embeddings.

Resultado general:

- Errores detectados: **0**
- Casos de prueba aprobados: **9/9**

---

# 10. Pruebas realizadas

## Pruebas de integración

Estos scripts se utilizan durante el desarrollo para realizar validaciones rápidas de integración entre módulos.
Ejecutadas mediante:

```text
temp/check_metadata.py
```

Se verificó:

- integración con Text Splitter;
- procesamiento completo de documentos;
- enriquecimiento correcto de metadata.

---

## Pruebas automatizadas

Implementadas mediante:

```text
tests/test_metadata.py
```

Framework utilizado:

```text
pytest
```

Casos implementados:

| Caso | Estado |
|------|:------:|
| CP-001 | ✅ |
| CP-002 | ✅ |
| CP-003 | ✅ |
| CP-004 | ✅ |
| CP-005 | ✅ |
| CP-006 | ✅ |
| CP-007 | ✅ |
| CP-008 | ✅ |
| CP-009 | ✅ |

Resultado:

```text
9 passed
```

---

# 11. Conclusiones

El módulo **Metadata Manager** cumple con los requisitos funcionales definidos en el **SDS-003**.

La metadata generada es consistente, enriquecida y se encuentra preparada para el proceso de generación de embeddings.

Durante este Sprint se incorporó oficialmente el uso de **pytest** como framework de pruebas automatizadas del proyecto, complementando los scripts de integración utilizados durante el desarrollo.

---

# 12. Relación con otros documentos

| Documento | Propósito |
|-----------|-----------|
| SDS-003 | Diseño técnico del módulo |
| LOG-001 | Registro del Sprint |
| MTR-001 | Trazabilidad |
| README | Estado del proyecto |
| HANDBOOK-001 | Metodología oficial |

---

# 13. Control de versiones

| Versión | Fecha | Descripción |
|----------|--------|-------------|
| 1.0 | 03/07/2026 | Implementación inicial del módulo Metadata Manager correspondiente al Sprint 5 – Hito 3. |