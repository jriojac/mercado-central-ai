# SDS-006
# Software Design Specification
## Módulo: Retriever
## Versión: 1.0
## Release objetivo: v0.6.0

---

# 1. Información del documento

| Campo | Valor |
|--------|-------|
| Documento | SDS-006 |
| Título | Software Design Specification – Retriever |
| Versión | 1.1 |
| Estado | En desarrollo |
| Sprint | 8 |
| Hito | 6 |
| Módulo | Retriever |
| Release objetivo | v0.6.0 |
| Dependencia | Vector Store (Sprint 7) |
| Autor | Jacqueline Rioja |
| Fecha | 06/07/2026 |
| Última actualización | 07/07/2026 |

---

# 2. Objetivo

Diseñar el módulo Retriever, responsable de recuperar desde el Vector Store los documentos semánticamente más relevantes para una consulta del usuario.

El diseño debe cumplir los principios arquitectónicos definidos para el proyecto:

- Responsabilidad única.
- Bajo acoplamiento.
- Alta cohesión.
- Programación contra interfaces.
- Extensibilidad mediante proveedores.
- Compatibilidad con el pipeline RAG.

---

# 3. Alcance

## Incluye

El módulo deberá permitir:

- Definición de interfaces.
- Diseño del proveedor ChromaRetriever.
- Configuración de búsqueda.
- Integración con Vector Store.
- Definición del flujo de recuperación.
- Contrato de entrada y salida.

## No incluye

- Construcción del contexto.
- Prompt Engineering.
- Invocación del LLM.
- Re-ranking.
- Hybrid Search.
- Multi Query.
- RAG Fusion.

---

# 4. Referencias

ACTUALIZA
Documentos relacionados:

- HANDBOOK
- ROADMAP
- README
- CHANGELOG
- MTR
- SDS-003 Metadata Manager
- SDS-004 Embeddings

---

# 5. Contexto dentro del Pipeline RAG

El Retriever constituye el punto de transición entre el almacenamiento vectorial y la construcción del contexto para el modelo de lenguaje.

```text
Knowledge Base

↓

Document Loader

↓

Text Splitter

↓

Metadata Manager

↓

Embeddings Engine

↓

Vector Store

↓

Retriever

↓

Context Builder

↓

Decision Engine

↓

LLM
```

## Entrada

- Consulta del usuario (query).
- Valor opcional top_k.
- Instancia de VectorStore.

## Procesamiento

Durante el procesamiento el módulo:

- Validar consulta.
- Aplicar configuración (RETRIEVER_TOP_K).
- Delegar la búsqueda a VectorStore.
- Recuperar documentos relevantes.

## Salida

- list[Document] ordenada por relevancia.

---

# 6. Requerimientos funcionales

| ID     | Descripción                           |
| ------ | ------------------------------------- |
| RF-601 | Definir la interfaz `IRetriever`.     |
| RF-602 | Recuperar documentos relevantes.      |
| RF-603 | Delegar la búsqueda al `VectorStore`. |
| RF-604 | Validar consultas.                    |
| RF-605 | Configuración mediante `settings.py`. |
| RF-606 | Implementar `RetrieverFactory`.       |
| RF-607 | Mantener independencia del proveedor. |


---

# 7. Responsabilidades del módulo

El Retriever será responsable exclusivamente de:

Consulta del usuario

↓

Embedding de consulta

↓

Consulta al Vector Store

↓

Recuperación Top-K

↓

Entrega de documentos


No será responsable de:

- interpretar resultados;
- resumir información;
- generar respuestas;
- construir prompts;
- comunicarse con Gemini;
- tomar decisiones de negocio.

Esto garantiza el cumplimiento del principio de Responsabilidad Única (SRP).
---

# 8. Arquitectura del módulo

```text
src/

retriever/

│

├── interfaces.py

├── chroma_retriever.py

├── retriever_factory.py

└── __init__.py
```
| Archivo              | Responsabilidad                |
| -------------------- | ------------------------------ |
| interfaces.py        | Definir contratos del módulo   |
| chroma_retriever.py  | Implementación para ChromaDB   |
| retriever_factory.py | Selección del proveedor        |
| **init**.py          | Exposición pública del paquete |


---

# 9. Flujo de procesamiento

```text
Consulta del usuario

        │

Validar consulta

        │

Aplicar configuración (Top-K)

        │

Delegar búsqueda al VectorStore

        │

Recuperar documentos

        │

Retornar list[Document]
```

---

# 10. Modelo de datos

## Entrada
| Campo | Tipo       | Descripción                             |
| ----- | ---------- | --------------------------------------- |
| query | str        | Consulta del usuario                    |
| top_k | int | None | Número máximo de documentos a recuperar |

## Salida
| Campo        | Tipo | Descripción          |
| ------------ | ---- | -------------------- |
| page_content | str  | Contenido recuperado |
| metadata     | dict | Metadata asociada    |

---

# 11. Diseño de clases

## Relación entre clases

```text
                    IRetriever
                         ▲
                         │
                  ChromaRetriever
                         ▲
                         │
                 RetrieverFactory
```

- IRetriever: contrato del módulo.
- ChromaRetriever: implementación concreta que delega la búsqueda al VectorStore.
- RetrieverFactory: ensambla las dependencias y crea instancias de IRetriever.

---

# 12. Interfaces públicas

```python
retrieve(
    query: str,
    top_k: int | None = None,
) -> list[Document]
```

## Parámetros
| Parámetro | Tipo       | Descripción                   |
| --------- | ---------- | ----------------------------- |
| query     | str        | Consulta del usuario          |
| top_k     | int | None | Cantidad máxima de documentos |

## Retorna
list[Document]

---

```python
load_collection()
```
Carga una colección existente para permitir operaciones posteriores.

---

```python
add_documents()
```
Inserta uno o más objetos VectorDocument dentro de la colección activa

---

```python
similarity_search()
```
Realiza una búsqueda semántica utilizando un embedding y retorna los documentos más similares.

## Parámetros:

- embedding
- k

## Retorna:

SearchResult

---

```python
delete_documents()
```
Elimina uno o más documentos utilizando sus identificadores.

---

```python
count_documents()
```
Obtiene el número total de documentos almacenados.

## Retorna:

int

---


```python
reset()
```
Reinicia completamente la colección eliminando todos sus documentos y dejándola disponible para nuevas inserciones.

---

# 13 Interfaces privadas
.
---

# 14. Reglas de validación

Validaciones mínimas:

- La consulta no debe ser vacía.
- El VectorStore debe estar inicializado.
- top_k debe ser mayor que cero (si se proporciona).
- Debe existir un proveedor configurado.
---

# 15. Configuración del módulo

La configuración se centralizará en settings.py.

Parámetros previstos:

| Parámetro                  | Descripción                                           |
| -------------------------- | ----------------------------------------------------- |
| `RETRIEVER_TOP_K`          | Número máximo de documentos recuperados por defecto.  |
| `RETRIEVER_VALIDATE_QUERY` | Activa o desactiva la validación de consultas vacías. |


---

# 16. Manejo de errores
El Retriever deberá gestionar de forma controlada:

- consulta vacía;
- colección inexistente;
- proveedor no inicializado;
- errores del motor vectorial;
- ausencia de resultados.

No propagará excepciones de bajo nivel sin encapsularlas adecuadamente.

---

# 17. Logging

Registrar como mínimo:

- Inicio del Retriever.
- Consulta recibida.
- Valor de top_k.
- Cantidad de documentos recuperados.
- Errores de validación.
- Excepciones delegadas por el VectorStore.

---

# 18. Consideraciones de rendimiento
Se establecen las siguientes directrices:

minimizar llamadas redundantes al Vector Store;
recuperar únicamente el Top-K requerido;
evitar múltiples consultas para una misma solicitud;
reutilizar la configuración centralizada;
preparar el diseño para búsquedas con filtros y umbrales de similitud.

---

# 19. Extensibilidad
El diseño permite incorporar nuevos proveedores sin modificar el resto del proyecto.

Ejemplos futuros:

ChromaDB
Pinecone
FAISS
Weaviate
Qdrant
Milvus

Solo será necesario implementar una nueva clase que cumpla el contrato IRetriever y registrarla en la RetrieverFactory.

---

# 20. Casos de Prueba
actualizar
La validación del módulo **VectorStore** se realizará mediante pruebas automatizadas utilizando **pytest**.

Cada caso de prueba mantiene trazabilidad con los requisitos funcionales definidos para el módulo.

| Caso   | Objetivo                  |
| ------ | ------------------------- |
| CP-034 | Crear `IRetriever`.       |
| CP-035 | Crear `ChromaRetriever`.  |
| CP-036 | Delegar a `VectorStore`.  |
| CP-037 | Respetar `top_k`.         |
| CP-038 | Validar consulta vacía.   |
| CP-039 | Crear `RetrieverFactory`. |


Todas las pruebas automatizadas fueron ejecutadas satisfactoriamente mediante pytest, validando la totalidad de la interfaz pública del módulo.

## Resultado obtenido 

- 18 pruebas ejecutadas
- 18 exitosas
- 0 fallidas
- Cobertura funcional: 100%

## Validación de integración

La validación manual del módulo se realizó mediante sesiones interactivas de Python y pruebas automatizadas con pytest.

---

## Cobertura de pruebas

La siguiente matriz muestra la relación entre los requisitos funcionales y los casos de prueba.

.
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
python -m pytest tests/test_vector_store.py
```


---

# 21. Trazabilidad

| Artefacto       | Relación                      |
| --------------- | ----------------------------- |
| PLAN-006        | Planificación del Sprint      |
| SDS-006         | Diseño del Retriever          |
| IMP-01 a IMP-06 | Implementación                |
| TST-01          | Pruebas unitarias             |
| MTR-001         | Actualización de trazabilidad |
| Release v0.6.0  | Entrega del Sprint            |


---

# 22. Riesgos identificados


| Riesgo                | Mitigación                 |
| --------------------- | -------------------------- |
| Cambios en LangChain  | Encapsular implementación  |
| Cambio de Vector DB   | Interfaces + Factory       |
| Cambios de parámetros | Configuración centralizada |
| Escalabilidad         | Diseño desacoplado         |


---

# 23. Estado de implementación

| Implementación               | Estado |
| ---------------------------- | :----: |
| IMP-01 Arquitectura          |    ✅   |
| IMP-02 Interfaz `IRetriever` |    ✅   |
| IMP-03 `ChromaRetriever`     |    ✅   |
| IMP-04 Pruebas unitarias     |    ✅   |
| IMP-05 Configuración         |    ✅   |
| IMP-06 `RetrieverFactory`    |    ✅   |



---

# 24. Resultados de implementación

Resultado final


- IRetriever:              ✓ Implementada
- ChromaRetriever:         ✓ Implementado
- RetrieverFactory:        ✓ Implementada
- Configuración:           ✓ Centralizada
- Pruebas automatizadas:   ✓ 18/18
- Cobertura funcional:     ✓ 100%

---

# 25. Registro de Decisiones Arquitectónicas (ADR Resumido) ✅ (Nueva sección)

| ID         | Decisión                                    | Justificación                                                                              |
| ---------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ADR-006-01 | Uso de interfaz `IRetriever`                | Permite desacoplar la implementación del proveedor de búsqueda.                            |
| ADR-006-02 | El Retriever no construye contexto          | Se mantiene el principio de responsabilidad única; el Context Builder asumirá esa función. |
| ADR-006-03 | Encapsular el acceso a LangChain            | Reduce el impacto de cambios futuros en la librería y facilita migraciones.                |
| ADR-006-04 | Configuración centralizada en `settings.py` | Evita valores hardcodeados y simplifica el mantenimiento.                                  |
| ADR-006-05 | Preparar soporte para múltiples proveedores | Facilita la evolución del proyecto sin modificar módulos consumidores.                     |

# 26. Contrato de la Interfaz (API Contract) ✅ (Nueva sección)

## Entrada
- Consulta (str)
- Parámetros opcionales de búsqueda (Top-K, filtros)
## Precondiciones
- El Vector Store debe estar inicializado.
- Debe existir una colección activa.
- La consulta no debe ser vacía.
- El VectorStore debe estar inicializado y disponible.
## Salida
Lista de documentos (list[Document])

Cada documento debe conservar:

page_content
metadata
Postcondiciones
La lista estará ordenada por relevancia.
No se modificarán los documentos originales.
Se respetará el límite Top-K configurado.
Excepciones previstas
Colección inexistente.
Error de conexión con Vector Store.
Error al generar embeddings.
Consulta inválida.
Sin resultados.

# 27. Control de versiones

| Versión | Cambios                                                      |
| ------- | ------------------------------------------------------------ |
| 1.0     | Creación del SDS-006.                                        |
| 1.1     | Implementación completa del Retriever y cierre del Sprint 8. |







