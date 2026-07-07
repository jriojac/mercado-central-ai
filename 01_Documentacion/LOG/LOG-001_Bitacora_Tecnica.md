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

### Registro de Avances (LOG)

---

### Sprint 4 – Hito 2

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


### Registro de avance

---







### Sprint 5 – Hito 3

## 2026-07-03 -- Cierre del Hito 3 

### Modulo 

Metadata Manager

### Estado

Finalizado

### Actividades realizadas

#### Planificación

- Definición del alcance del Metadata Manager.
- Identificación de los requisitos funcionales RF-011 a RF-015.
- Definición de la estrategia de implementación del módulo.

#### Diseño

- Elaboración del documento **SDS-003 – Software Design Specification**.
- Definición de la arquitectura interna del Metadata Manager.
- Definición de reglas oficiales para la normalización de metadata.
- Incorporación de trazabilidad entre requisitos funcionales, implementaciones y casos de prueba.

#### Implementación

Se implementó la clase:

```text
MetadataManager
```

con las siguientes responsabilidades:

- Validación de metadata obligatoria.
- Normalización de metadata.
- Enriquecimiento automático de metadata.
- Validación de colecciones de documentos.
- Preparación de documentos para el módulo Embeddings.

También se incorporó el archivo:

```text
src/core/exceptions.py
```

para centralizar las excepciones personalizadas del proyecto.

---

#### Pruebas

Se incorporó por primera vez un framework de pruebas automatizadas basado en **pytest**.

Se creó la siguiente estructura:

```text
tests/
│
├── __init__.py
└── test_metadata.py
```

Casos de prueba implementados:

| Caso | Estado |
|------|--------|
| CP-001 | ✅ |
| CP-002 | ✅ |
| CP-003 | ✅ |
| CP-004 | ✅ |
| CP-005 | ✅ |
| CP-006 | ✅ |
| CP-007 | ✅ |
| CP-008 | ✅ |
| CP-009 | ✅ |

### Resultado:

```text
9 passed
```

Se mantiene adicionalmente el script de integración:

```text
temp/check_metadata.py
```

---

### Mejoras metodológicas

Durante este Sprint se incorporaron nuevas prácticas al proyecto:

- Uso oficial de **pytest** para pruebas funcionales.
- Separación entre pruebas de integración (`temp/`) y pruebas automatizadas (`tests/`).
- Incorporación de Casos de Prueba (CP) dentro del SDS.
- Trazabilidad completa:

```text
RF
 ↓
SDS
 ↓
IMP
 ↓
CP
 ↓
Release
```

- Recomendación oficial de utilizar:

```bash
python -m pip
```

en lugar de `pip` para la instalación de dependencias.

---

#### Archivos creados

```text
src/knowledge/metadata.py
src/core/exceptions.py
tests/test_metadata.py
temp/check_metadata.py  | Herramientas y scripts de apoyo para el desarrollo (locales, no forman parte de la Release).
```

---

#### Archivos actualizados

```text
src/config/settings.py

SDS-003_Document_Metadata.md

README.md (pendiente)

LOG-001_Bitacora_Tecnica.md

MTR-001_Matriz_Trazabilidad.md (pendiente)

CHANGELOG.md (pendiente)
```

---

#### Resultado del Sprint

Estado del Metadata Manager:

```text
MetadataManager

✔ Validación

✔ Normalización

✔ Enriquecimiento

✔ Integración

✔ Pruebas automatizadas
```

Estado general del pipeline:

```text
Knowledge Base
      │
      ▼
Document Loader        ✅
      │
      ▼
Text Splitter          ✅
      │
      ▼
Metadata Manager       ✅
      │
      ▼
Embeddings             ⏳
```

---

#### Observaciones

El Sprint permitió consolidar la estrategia de validación automática del proyecto mediante pytest y establecer una metodología reutilizable para los siguientes módulos del pipeline RAG.

---
#### Registro de avance
---








## 2026-07-01 -- Cierre del Hito 4

### Sprint 6 - Hito 4

### Módulo

Embeddings

### Objetivo

Implementar el módulo **Embeddings**, responsable de transformar los documentos enriquecidos por el Metadata Manager en representaciones vectoriales (embeddings) mediante Google Generative AI, preparando la información para el futuro módulo Vector Store.

### Actividades realizadas

#### Planificación

- Definición del alcance del módulo Embeddings.
- Identificación de los requisitos funcionales RF-040 a RF-045.
- Definición de la arquitectura del proveedor de embeddings.

#### Diseño

- Elaboración del documento **SDS-004 – Software Design Specification**.
- Diseño de la arquitectura desacoplada entre el módulo Embeddings y el proveedor de IA.
- Definición de la configuración centralizada mediante `settings.py`.

#### Implementación

Se implementaron las clases:

```text
Embeddings

EmbeddingProvider
```

Con las siguientes responsabilidades:

- Validación de documentos.
- Inicialización del proveedor de embeddings.
- Generación de embeddings para documentos.
- Generación de embeddings para consultas.
- Manejo centralizado de excepciones.
- Configuración mediante variables de entorno.

También se incorporó la integración con:

```text
Google Generative AI
```

utilizando el modelo:

```text
gemini-embedding-2
```

---

#### Configuración

Durante este Sprint se incorporó la configuración del archivo:

```text
.env
```

con la variable:

```text
GOOGLE_API_KEY
```

La autenticación quedó desacoplada del código fuente, permitiendo mantener las credenciales fuera del repositorio.

---

#### Pruebas

Se implementó el script de integración:

```text
temp/check_pipeline_embeddings.py
```

El script valida el flujo completo del pipeline:

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
```

Resultado obtenido:

```text
Document Loader      ✔

Text Splitter        ✔

Metadata Manager     ✔

Embeddings           ✔

Pipeline completado correctamente
```

La validación se realizó utilizando una muestra reducida de documentos para respetar las restricciones de cuota del servicio gratuito de Google Generative AI.

---

#### Problemas encontrados

Durante el desarrollo se identificaron los siguientes inconvenientes:

- Error por ausencia de `GOOGLE_API_KEY`.
- Error de autenticación al utilizar claves pertenecientes a proyectos antiguos.
- Error `RESOURCE_EXHAUSTED (429)` al procesar la totalidad de los chunks utilizando la cuota gratuita.
- Necesidad de crear un proyecto específico para el Challenge en Google AI Studio.

Todos los problemas fueron resueltos durante el Sprint.

---

#### Mejoras metodológicas

Se incorporaron nuevas prácticas al proyecto:

- Configuración mediante archivo `.env`.
- Validación explícita de credenciales antes de inicializar el proveedor.
- Separación entre lógica de negocio y proveedor de IA.
- Reutilización de una única instancia del proveedor de embeddings.
- Uso de muestras representativas durante las pruebas de integración para optimizar el consumo de cuota.

---

#### Archivos creados

```text
src/llm/embedding_provider.py

src/knowledge/embeddings.py

temp/check_pipeline_embeddings.py
```

---

#### Archivos actualizados

```text
src/config/settings.py

src/core/exceptions.py

SDS-004_Embeddings.md

README.md (pendiente)

CHANGELOG.md (pendiente)

LOG-001_Bitacora_Tecnica.md
```

---

### Resultado

Estado del pipeline:

```text
Knowledge Base         ✔

Document Loader        ✔

Text Splitter          ✔

Metadata Manager       ✔

Embeddings             ✔

Vector Store           ⏳
```

---

### Observaciones

Con la finalización del módulo Embeddings queda concluida la primera etapa del pipeline RAG correspondiente al procesamiento documental.

El proyecto ya es capaz de:

- cargar documentos;
- fragmentarlos;
- enriquecer su metadata;
- generar embeddings utilizando un modelo real de Google Generative AI.

---

### Lecciones aprendidas

- La autenticación debe mantenerse completamente desacoplada del código fuente.
- Las pruebas de integración deben adaptarse a las limitaciones del nivel gratuito del proveedor.
- La reutilización del proveedor reduce la cantidad de inicializaciones innecesarias.
- La separación entre `Embeddings` y `EmbeddingProvider` facilita futuras migraciones hacia otros modelos o proveedores.
- Los scripts ubicados en `temp/` son herramientas de validación para el desarrollo local y no forman parte de la Release del proyecto.
---

## 2026-07-05 -- Cierre del Hito 5

### Sprint 7 - Hito 5

### Registro de avance
Hito 5 – Vector Store
v0.5.0

#### Objetivo
Implementar el módulo Vector Store, responsable de almacenar, administrar y recuperar documentos vectoriales generados por el módulo Embeddings Engine, proporcionando la infraestructura de persistencia necesaria para el pipeline RAG.

####  Actividades realizadas

##### Planificación
- Definición del alcance del módulo Vector Store.
- Identificación de los requisitos funcionales RF-501 a RF-506.
- Definición de la estrategia de almacenamiento vectorial.
- Selección de ChromaDB como proveedor inicial del proyecto.

##### Diseño
- Elaboración del documento SDS-005 – Vector Store.
- Definición de la arquitectura desacoplada mediante interfaces.
- Diseño del proveedor abstracto VectorStoreProvider.
- Definición de los modelos VectorDocument y SearchResult.
- Diseño de la gestión de colecciones vectoriales.
- Integración con la configuración centralizada mediante settings.py.

##### Implementación
Se implementaron los siguientes componentes:
- VectorStore
- VectorStoreProvider
- ChromaProvider
- VectorDocument
- SearchResult

Se desarrollaron las siguientes funcionalidades:

- creación de colecciones;
- carga de colecciones existentes;
- inserción de documentos;
- búsqueda por similitud;
- conteo de documentos;
- eliminación de documentos;
- reinicio completo de colecciones.

#### Decisiones de arquitectura
Durante el desarrollo del módulo se adoptaron las siguientes decisiones arquitectónicas:

 - DA-701
Implementar una arquitectura basada en interfaces para desacoplar el almacenamiento vectorial del resto del pipeline.

- DA-702
Utilizar el patrón Strategy para permitir la incorporación de nuevos proveedores vectoriales sin modificar la lógica del sistema.

- DA-703
Centralizar toda la configuración del proveedor mediante settings.py.

- DA-704
Representar los documentos mediante el modelo VectorDocument y los resultados de búsqueda mediante SearchResult.

#### Problemas encontrados
Durante el Sprint se identificaron y resolvieron los siguientes inconvenientes:

- incompatibilidades de versiones entre ChromaDB y LangChain;
- errores de importación del proveedor;
- ajustes de tipado para VectorDocument;
- errores de identación durante la implementación;
- gestión de colecciones inexistentes;
- diferencias entre las pruebas manuales y automatizadas;
- ajustes en la configuración del proveedor mediante settings.py.

Todos los problemas fueron resueltos durante el desarrollo del Sprint.

#### Pruebas
Se implementó la suite automatizada:
tests/
└── test_vector_store.py

Resultado obtenido : 8 passed

Se validaron satisfactoriamente:

- creación de colecciones;
- inserción de documentos;
- búsqueda por similitud;
- conteo de documentos;
- eliminación de documentos;
- reinicio de colecciones;
- persistencia local mediante ChromaDB;
- validación completa de la interfaz pública.

#### Refactorización
Durante el Sprint se realizaron diversas actividades de mejora del código:

- incorporación de pytest.fixture;
- eliminación de código duplicado;
- centralización de la resolución del nombre de la colección;
- incorporación de métodos privados para reducir duplicidad;
- reorganización de la inicialización del proveedor;
- mejora de la mantenibilidad del módulo;
- simplificación de la suite de pruebas.

#### Mejoras metodológicas
Durante este Sprint se consolidaron nuevas prácticas de desarrollo:

- adopción de una arquitectura basada en interfaces;
- desacoplamiento entre dominio e infraestructura;
- incorporación del patrón Strategy;
- consolidación de pruebas automatizadas mediante pytest;
- actualización de la metodología documental del proyecto (SDS, MTR, README y CHANGELOG).

#### Archivos creados
- src/knowledge/vector_store.py
- src/knowledge/provider.py
- src/knowledge/providers/chroma_provider.py
- src/knowledge/types.py
- src/knowledge/constants.py
- tests/test_vector_store.py

#### Archivos actualizados
- src/config/settings.py
- README.md
- CHANGELOG.md
- MTR-001_Matriz_Trazabilidad.md
- SDS-005_Vector_Store.md
- LOG-001_Bitacora_Tecnica.md

#### Resultado
##### Vector Store

✔ create_collection()

✔ load_collection()

✔ add_documents()

✔ similarity_search()

✔ count_documents()

✔ delete_documents()

✔ reset()

##### Estado pipeline
Knowledge Base
      │
      ▼
Document Loader        ✔
      │
      ▼
Text Splitter          ✔
      │
      ▼
Metadata Manager       ✔
      │
      ▼
Embeddings Engine      ✔
      │
      ▼
Vector Store           ✔
      │
      ▼
Retriever              ⏳

#### Lecciones aprendidas
- Diseñar primero la arquitectura facilita la implementación.
- Definir interfaces reduce el acoplamiento entre módulos.
- La validación incremental simplifica la depuración.
- El uso de pytest.fixture mejora significativamente la mantenibilidad de las pruebas.
- La separación entre interfaz e implementación permitirá incorporar nuevos proveedores vectoriales - con un impacto mínimo sobre el resto del sistema.

#### Observaciones

Con la finalización del módulo Vector Store, el proyecto completa la etapa de preparación e indexación de la información dentro del pipeline RAG.

El sistema es capaz de:

- cargar documentos desde la Base de Conocimiento;
- fragmentar documentos en chunks;
- enriquecer la metadata;
- generar embeddings;
- almacenar documentos vectoriales de forma persistente;
- ejecutar búsquedas semánticas mediante ChromaDB.

El siguiente Sprint estará orientado al desarrollo del módulo Retriever, responsable de recuperar los documentos más relevantes del Vector Store para la construcción del contexto que será utilizado por el modelo de lenguaje.