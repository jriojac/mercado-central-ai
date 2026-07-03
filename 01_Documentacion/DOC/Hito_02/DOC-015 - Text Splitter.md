# DOC-015
# Text Splitter
## Sprint 4 – Hito 2

---

# 1. Objetivo

Implementar el módulo **Text Splitter** del pipeline RAG para fragmentar los documentos cargados por el Document Loader en unidades de texto (chunks), preservando la metadata original y agregando información adicional necesaria para las siguientes etapas del pipeline.

---

# 2. Alcance

El módulo es responsable de:

- Validar la colección de documentos recibida.
- Fragmentar documentos mediante `RecursiveCharacterTextSplitter`.
- Conservar la metadata original.
- Enriquecer la metadata de cada chunk.
- Entregar una colección de `Document` lista para la generación de embeddings.

No forma parte de este módulo:

- Generación de embeddings.
- Almacenamiento vectorial.
- Recuperación de contexto.

---

# 3. Arquitectura

El módulo ocupa la siguiente posición dentro del pipeline RAG:

Knowledge Base
      ↓
Document Loader
      ↓
Text Splitter
      ↓
Embeddings
      ↓
Vector Store
      ↓
Retriever
      ↓
Gemini

---

# 4. Componentes

La implementación está compuesta por la clase:

TextSplitter

con los siguientes métodos:

- `__init__()`
- `_validate_documents()`
- `_split()`
- `_enrich_metadata()`
- `split_documents()`

---

# 5. Flujo de procesamiento

1. Recibir una lista de documentos.
2. Validar la entrada.
3. Fragmentar los documentos.
4. Enriquecer la metadata.
5. Retornar la colección de chunks.

---

# 6. Metadata generada

Cada chunk conserva la metadata proporcionada por el Document Loader y añade:

| Campo | Descripción |
|--------|-------------|
| chunk_index | Índice del chunk dentro del documento |
| total_chunks | Cantidad total de chunks generados |
| chunk_size | Longitud del contenido del chunk |
| splitter_version | Versión del algoritmo de fragmentación |

---

# 7. Configuración

La configuración del módulo se centraliza en:

`src/config/settings.py`

Parámetros utilizados:

- `chunk_size`
- `chunk_overlap`
- `separators`
- `version`

---

# 8. Validaciones implementadas

El módulo valida:

- colección nula;
- lista vacía;
- tipo de dato incorrecto.

Las validaciones generan excepciones controladas antes del proceso de fragmentación.

---

# 9. Resultados obtenidos

Durante las pruebas de integración se obtuvo:

- PDFs procesados: 4
- Documentos cargados: 124
- Chunks generados: 367
- Errores: 0

---

# 10. Pruebas realizadas

Pruebas unitarias:

- Inicialización del módulo.
- Validación de errores.
- Documento corto.
- Documento largo.

Pruebas de integración:

- Document Loader + Text Splitter.

Todas las pruebas fueron satisfactorias.

---

# 11. Conclusiones

El módulo Text Splitter cumple con los requerimientos funcionales definidos en el SDS-002.

La salida del módulo está preparada para ser utilizada por el siguiente componente del pipeline RAG: **Embeddings**.

---

# 12. Control de versiones

| Versión | Fecha | Descripción |
|----------|-------|-------------|
| 1.0 | (fecha) | Implementación inicial del módulo Text Splitter correspondiente al Sprint 4 – Hito 2. |