# SDS-005
# Software Design Specification
## Módulo: Vector Store
## Versión: 1.0
## Release objetivo: v0.5.0

---

# 1. Información del documento

| Campo | Valor |
|--------|-------|
| Documento | SDS-005 |
| Título | Software Design Specification – Vector Store |
| Versión | 1.1 |
| Estado | Implementado |
| Sprint | 7 |
| Hito | 5 |
| Módulo | Vector Store |
| Release objetivo | v0.5.0 |
| Autor | Jacqueline Rioja |
| Fecha | 05/07/2026 |
| Última actualización | 05/07/2026 |

---

# 2. Objetivo

Implementar el módulo Vector Store responsable de almacenar de forma persistente los documentos vectoriales (embeddings, contenido y metadatos), permitiendo realizar búsquedas semánticas mediante similitud vectorial y proporcionando la base para el futuro módulo Retriever del pipeline RAG.

La arquitectura deberá desacoplar el proveedor vectorial mediante una interfaz, permitiendo sustituir ChromaDB por otro motor sin afectar el resto del sistema.
---

# 3. Alcance

## Incluye

El módulo deberá permitir:

- Crear colecciones.
- Cargar colecciones existentes.
- Persistir documentos vectoriales.
- Persistir embeddings.
- Persistir metadatos.
- Búsquedas por similitud.
- Eliminación de documentos.
- Conteo de documentos.
- Reinicio de colecciones.
- Desacoplamiento mediante interfaz.
- Integración con Embeddings.

## No incluye

- Retriever.
- Ranking.
- Re-ranking.
- Context Builder.
- Respuesta del LLM.

---

# 4. Referencias

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

El módulo **Vector Store** forma parte de la capa de persistencia del pipeline RAG y es responsable de almacenar de manera permanente los documentos vectoriales generados por el módulo **Embeddings**.

Su propósito es conservar el contenido, los metadatos y los vectores de representación semántica para que puedan recuperarse posteriormente mediante búsquedas de similitud, sirviendo como base para el futuro módulo **Retriever**.

Dentro del flujo del proyecto, el Vector Store actúa como la frontera entre la fase de indexación y la fase de recuperación de información.

```text
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
LLM
```

## Entrada

El módulo recibe una colección de objetos VectorDocument generados por el módulo Embeddings.

- contenido textual (page_content)
- metadata enriquecida
- embedding vectorial

## Procesamiento

Durante el procesamiento el módulo:

- valida la colección destino;
- valida la estructura del documento;
- convierte la información al formato requerido por ChromaDB;
- almacena el contenido y sus embeddings;
- mantiene la persistencia de la colección.

## Salida

Como resultado, el módulo deja disponible una colección vectorial persistente capaz de responder consultas por similitud para el futuro módulo Retriever.



---

# 6. Requerimientos funcionales


| RF     | Descripción                               |
| ------ | ----------------------------------------- |
| RF-501 | Crear el módulo Vector Store              |
| RF-502 | Persistir documentos vectoriales          |
| RF-503 | Persistir embeddings                      |
| RF-504 | Persistir metadatos                       |
| RF-505 | Administrar colecciones                   |
| RF-506 | Ejecutar búsquedas de similitud           |
| RF-507 | Eliminar documentos                       |
| RF-508 | Contar documentos                         |
| RF-509 | Reiniciar colecciones                     |
| RF-510 | Desacoplar el proveedor mediante interfaz |
| RF-511 | Integrarse con Embeddings                 |

---

# 7. Responsabilidades del módulo

El módulo Vector Store será responsable de:

- administrar colecciones;
- almacenar documentos;
- almacenar embeddings;
- almacenar metadatos;
- realizar búsquedas vectoriales;
- eliminar documentos;
- reiniciar colecciones;
- abstraer el proveedor mediante VectorStoreProvider.


No será responsable de:

- generar embeddings;
- construir contexto;
- consultar LLM;
- ranking.

---

# 8. Arquitectura del módulo

```text
Embeddings
        │
        ▼
Vector Store
        │
        ▼
VectorStoreProvider
        │
        ▼
ChromaProvider
        │
        ▼
ChromaDB
```


---

# 9. Flujo de procesamiento

```text
VectorDocument[]

      │

Validar colección

      │

Validar documentos

      │

Convertir formato

      │

Persistir

      │

Confirmar inserción

      │

Retornar resultado
```

---

# 10. Modelo de datos

## VectorDocument
| Campo        | Tipo        | Descripción          |
| ------------ | ----------- | -------------------- |
| id           | str         | Identificador único  |
| page_content | str         | Contenido            |
| metadata     | dict        | Metadata enriquecida |
| embedding    | list[float] | Embedding            |
| source       | str         | Documento origen     |
| page         | int         | Página               |


## SearchResult
| Campo     | Tipo |
| --------- | ---- |
| ids       | list |
| documents | list |
| metadatas | list |
| distances | list |


---

# 11. Diseño de clases

## Relación entre clases

```text
VectorStore
        │
        ▼
VectorStoreProvider
        │
        ▼
ChromaProvider

## Clase principal

```python
class VectorStore
```

### Responsabilidad

Es la fachada del módulo.

Su responsabilidad consiste en exponer una interfaz sencilla para que el resto del proyecto pueda interactuar con el almacenamiento vectorial sin depender de la implementación concreta del proveedor.

La clase delega todas las operaciones al proveedor configurado mediante el patrón Strategy.

### Dependencias

- VectorStoreProvider
- settings.py
---

## Clase abstracta

```python
class VectorStoreProvider
```

### Responsabilidad

Define el contrato que debe cumplir cualquier proveedor de almacenamiento vectorial.

Establece las operaciones públicas del módulo sin depender de una tecnología específica.

Permite reemplazar ChromaDB por otro motor (Pinecone, Weaviate, Qdrant, FAISS, Milvus, etc.) sin modificar el resto del sistema.

- Métodos definidos
- create_collection()
- load_collection()
- add_documents()
- similarity_search()
- delete_documents()
- count_documents()
- reset()

---

## Clase concreta

```python
class ChromaProvider
```

### Responsabilidad

Implementa el contrato definido por VectorStoreProvider utilizando ChromaDB como motor de almacenamiento.

Gestiona la conexión con la base vectorial, administra colecciones, convierte los documentos al formato requerido por ChromaDB y ejecuta todas las operaciones sobre el Vector Store.

- Dependencias
- chromadb
- settings.py
- VectorDocument
- SearchResult

---

# Principios de diseño

El módulo fue diseñado siguiendo los siguientes principios:

- Responsabilidad Única (SRP).
- Inversión de Dependencias (DIP).
- Abierto/Cerrado (OCP).
- Patrón Strategy para proveedores.
- Bajo acoplamiento entre la lógica del dominio y la implementación del almacenamiento.
- Configuración centralizada mediante `settings.py`.

---

# 12. Interfaces públicas

| Método | Descripción |
|--------|-------------|
| create_collection() | Crear colección |
| load_collection() | Cargar colección |
| add_documents() | Insertar documentos |
| similarity_search() | Buscar similitud |
| delete_documents() | Eliminar documentos |
| count_documents() | Contar documentos |
| reset() | Reiniciar colección |

```python
create_collection(
    collection_name: str | None = None
)
```
Crea una nueva colección vectorial.

Si no se especifica un nombre, utilizará la colección configurada en settings.py

## Parámetros

| Parámetro       | Tipo       | Descripción            |
| --------------- | ---------- | ---------------------- |
| collection_name | str | None | Nombre de la colección |

## Retorna

No retorna valor.

## Excepciones
ProviderError
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

```python
_resolve_collection_name()
```

Resuelve el nombre efectivo de la colección utilizando el parámetro recibido o la configuración definida en settings.py


```python
_to_chroma_format()
```
Transformar una colección de VectorDocument al formato requerido por ChromaDB antes de realizar la inserción.

---

# 14. Reglas de validación

Validaciones mínimas:

- colección existente;
- nombre válido;
- VectorDocument válido;
- embedding obligatorio;
- dimensiones compatibles;
- metadata válida.

---

# 15. Configuración del módulo

Toda la configuración deberá mantenerse centralizada en:

```text
src/config/settings.py
```

Configuraciones previstas:

| Variable             | Descripción           |
| -------------------- | --------------------- |
| VECTOR_DB_PROVIDER   | Proveedor vectorial   |
| VECTOR_DB_PATH       | Ruta de persistencia  |
| VECTOR_DB_COLLECTION | Colección por defecto |
| VECTOR_SEARCH_K      | Número de resultados  |


---

# 16. Manejo de errores

Todas las excepciones específicas del proveedor deberán encapsularse mediante ProviderError para desacoplar la implementación concreta del resto del sistema.

---

# 17. Logging

Registrar como mínimo:

- inicio del proveedor;
- creación de colección;
- carga de colección;
- inserción de documentos;
- consultas por similitud;
- eliminación;
- reinicio;
- errores del proveedor.

---

# 18. Consideraciones de rendimiento

Objetivos:

- reutilización del cliente ChromaDB;
- persistencia local;
- operaciones de inserción por lotes;
- consultas eficientes por similitud;
- manejo de colecciones grandes;
- consumo de memoria durante la indexación.

---

# 19. Extensibilidad

La arquitectura deberá permitir incorporar nuevas funcionalidades sin modificar el flujo principal del módulo.

- Pinecone;
- Weaviate;
- Qdrant;
- Milvus;
- FAISS;
- motores remotos.

---

# 20. Casos de Prueba

La validación del módulo **VectorStore** se realizará mediante pruebas automatizadas utilizando **pytest**.

Cada caso de prueba mantiene trazabilidad con los requisitos funcionales definidos para el módulo.

| Caso   | Objetivo           |
| ------ | ------------------ |
| CP-026 | Crear proveedor    |
| CP-027 | Crear colección    |
| CP-028 | Cargar colección   |
| CP-029 | Agregar documentos |
| CP-030 | Contar documentos  |
| CP-031 | Similarity Search  |
| CP-032 | Delete Documents   |
| CP-033 | Reset              |

Todas las pruebas automatizadas fueron ejecutadas satisfactoriamente mediante pytest, validando la totalidad de la interfaz pública del módulo.

## Resultado obtenido 

- 8 pruebas ejecutadas
- 8 exitosas
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

La siguiente matriz establece la relación entre los requisitos funcionales, la implementación y los casos de prueba definidos para el módulo Vector Store.

| RF     | Método            | Caso   |
| ------ | ----------------- | ------ |
| RF-501 | create_collection | CP-027 |
| RF-502 | add_documents     | CP-029 |
| RF-503 | count_documents   | CP-030 |
| RF-504 | similarity_search | CP-031 |
| RF-505 | delete_documents  | CP-032 |
| RF-506 | reset             | CP-033 |


---

# 22. Riesgos identificados

- Corrupción de la colección por cierre inesperado.
- Incompatibilidad entre dimensiones de embeddings.
- Eliminación accidental de colecciones.
- Crecimiento excesivo del almacenamiento local.
- Cambio futuro de proveedor vectorial.

---

# 23. Estado de implementación

| Implementación                       | Estado |
| ------------------------------------ | :----: |
| IMP-01 Arquitectura                  |    ✅   |
| IMP-02 Preparación del entorno       |    ✅   |
| IMP-03 Implementación ChromaProvider |    ✅   |
| IMP-04 create/load_collection        |    ✅   |
| IMP-05 add_documents                 |    ✅   |
| IMP-06 similarity_search             |    ✅   |
| IMP-07 delete_documents              |    ✅   |
| IMP-08 count_documents               |    ✅   |
| IMP-09 reset                         |    ✅   |
| IMP-10 Pruebas automatizadas         |    ✅   |
| IMP-11 Refactorización               |    ✅   |
| IMP-12 Documentación                 |    ✅   |


---

# 24. Resultados de implementación

Resultado final


- Proveedor implementado:       ✓ ChromaDB
- Persistencia:                 ✓ OK
- Inserción:                    ✓ OK
- Consulta:                     ✓ OK
- Eliminación:                  ✓ OK
- Reset:                        ✓ OK
- Pruebas automatizadas:        8/8 exitosas (pytest)
- Cobertura:                    100%

---

# 25. Control de versiones

| Versión | Fecha      | Autor            | Cambios                                                    |
| ------- | ---------- | ---------------- | ---------------------------------------------------------- |
| 1.0     | 05/07/2026 | Jacqueline Rioja | Creación inicial del SDS-005 para el módulo Vector Store.                                                                                                 |
| 1.1     | 05/07/2026 | Jacqueline Rioja | Documento actualizado tras la implementación completa del Vector Store. Se documentan la integración con ChromaDB, la interfaz `VectorStoreProvider`, las operaciones implementadas (`create_collection`, `load_collection`, `add_documents`, `similarity_search`, `delete_documents`, `count_documents`, `reset`), la refactorización de pruebas mediante `pytest.fixture` y la validación final con **8 pruebas automatizadas exitosas**. |



