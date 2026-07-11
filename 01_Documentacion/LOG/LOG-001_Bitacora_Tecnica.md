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


## 2026-07-08 -- Cierre del Hito 6

### Sprint 8 - Hito 6

### Registro de avance
Hito 6 – Retriever
v0.6.0

#### Objetivo
Implementar el módulo Retriever, responsable de recuperar los documentos más relevantes desde el Vector Store mediante búsquedas semánticas, manteniendo una arquitectura desacoplada basada en interfaces y preparada para futuras implementaciones de proveedores vectoriales.

####  Actividades realizadas

##### Planificación
- Definición del alcance del módulo Retriever.
- Identificación de los requisitos funcionales RF-601 a RF-607.
- Diseño de la estrategia de recuperación documental.
- Definición del contrato público mediante IRetriever.

##### Diseño
- Elaboración del documento SDS-006 – Retriever.
- Definición de la arquitectura basada en interfaces.
- Diseño del patrón Factory para el ensamblado de dependencias.
- Integración con la configuración centralizada mediante settings.py.

##### Implementación
Se implementaron los siguientes componentes:
- IRetriever
- ChromaRetriever
- RetrieverFactory

Se desarrollaron las siguientes funcionalidades:

- recuperación de documentos mediante consultas semánticas;
- validación de consultas de entrada;
- configuración de top_k desde settings.py;
- integración con VectorStore;
- desacoplamiento entre la lógica del Retriever y el proveedor vectorial.

#### Decisiones de arquitectura
Durante el desarrollo del módulo se adoptaron las siguientes decisiones arquitectónicas:

 - DA-801
Utilizar una interfaz (IRetriever) como contrato único para el módulo.

- DA-802
Mantener el desacoplamiento reutilizando VectorStore como fachada, evitando dependencias directas con ChromaDB.

- DA-803
Centralizar la configuración del Retriever mediante settings.py.

- DA-804
Implementar la primera Factory oficial del proyecto (RetrieverFactory) como punto único de creación de dependencias.

#### Problemas encontrados
Durante el Sprint se identificaron y resolvieron los siguientes inconvenientes:

- diferencias en la convención de imports entre paquetes;
- ausencia inicial de la implementación física de IRetriever;
- ajustes de estructura del paquete retriever;
- eliminación de valores hardcodeados (magic numbers);
- normalización del uso de src. para imports entre paquetes.

Todos los problemas fueron resueltos durante el desarrollo del Sprint.

#### Pruebas
Se implementó la suite automatizada:
tests/
└── test_retriever.py

Resultado obtenido : 18 passed

Se validaron satisfactoriamente:

- implementación de IRetriever;
- funcionamiento de ChromaRetriever;
- integración con VectorStore;
- configuración centralizada;
- funcionamiento de RetrieverFactory;
- compatibilidad con todos los módulos desarrollados previamente.

#### Refactorización
Durante el Sprint se realizaron diversas actividades de mejora del código:

- estandarización de imports utilizando src. entre paquetes;
- adopción de imports relativos dentro del mismo paquete;
- centralización de la configuración del Retriever;
- eliminación de valores fijos mediante settings.py;
- consolidación del patrón Factory.

#### Mejoras metodológicas
Durante este Sprint se consolidaron nuevas prácticas de desarrollo:

- definición del estándar oficial de imports;
- incorporación del patrón Factory como mecanismo oficial de ensamblado;
- validación de la existencia física de archivos antes de avanzar entre microentregas;
- fortalecimiento de la estrategia incremental basada en análisis, implementación, validación y documentación.

#### Archivos creados
- src/retriever/interfaces.py
- src/retriever/chroma_retriever.py
- src/retriever/retriever_factory.py
- tests/test_retriever.py

#### Archivos actualizados
- src/config/settings.py
- README.md
- CHANGELOG.md
- MTR-001_Matriz_Trazabilidad.md
- SDS-006_Retriever.md
- LOG-001_Bitacora_Tecnica.md

#### Resultado
##### Retriever

✔ IRetriever

✔ ChromaRetriever

✔ RetrieverFactory

✔ Configuración centralizada

✔ Integración con VectorStore

✔ Pruebas automatizadas

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
Retriever              ✔
      │
      ▼
Context Builder        ⏳

#### Lecciones aprendidas
- Definir primero las interfaces reduce el acoplamiento entre módulos.
- Centralizar la configuración simplifica la evolución del sistema.
- La validación incremental evita regresiones en módulos ya cerrados.
- El patrón Factory facilita el ensamblado de dependencias y prepara la arquitectura para futuras extensiones.

#### Observaciones

Con la finalización del módulo **Context Builder**, el proyecto completa la etapa de recuperación documental del pipeline RAG.

El sistema ya es capaz de:

- cargar documentos;
- fragmentarlos;
- enriquecer su metadata;
- generar embeddings;
- almacenarlos en el Vector Store;
- recuperar los documentos más relevantes mediante búsquedas semánticas.

El siguiente Sprint estará orientado al desarrollo del Context Builder, responsable de construir el contexto que será enviado al modelo de lenguaje.


## 2026-07-09 -- Cierre del Hito 7

### Sprint 9 - Hito 7

### Registro de avance
Hito 7 – Context Builder
v0.7.0

#### Objetivo
Implementar el módulo Context Builder, responsable de transformar los documentos recuperados por el Retriever en un contexto textual consolidado, preservando el orden por relevancia y manteniendo independencia respecto al modelo de lenguaje.

####  Actividades realizadas

##### Planificación
- Definición del alcance del Context Builder.
- Identificación de los requisitos funcionales RF-701 a RF-707.
- Definición del contrato público mediante ContextBuilderInterface.
- Diseño de la estrategia inicial de construcción de contexto.

##### Diseño
- Elaboración del documento SDS-007 – Context Builder.
- Definición de la arquitectura basada en interfaces.
- Diseño del patrón Factory para el ensamblado del módulo.
- Integración con la configuración centralizada mediante settings.py.

##### Implementación
Se implementaron los siguientes componentes:
- ContextBuilderInterface
- SimpleContextBuilder
- ContextBuilderFactory

Se desarrollaron las siguientes funcionalidades:

- construcción de contexto textual;
- preservación del orden recibido del Retriever;
- eliminación de documentos sin contenido;
- configuración centralizada;
- desacoplamiento respecto al modelo LLM.

#### Decisiones de arquitectura
Durante el desarrollo del módulo se adoptaron las siguientes decisiones arquitectónicas:

- DA-901
Implementar ContextBuilderInterface como contrato público del módulo.

- DA-902
Mantener el Context Builder independiente del Decision Engine y del modelo Gemini.

- DA-903
Centralizar la configuración del módulo mediante settings.py.

- DA-904
Implementar ContextBuilderFactory como punto único de creación de dependencias.

- DA-905
Preparar la arquitectura para incorporar futuras estrategias de construcción de contexto sin modificar los módulos consumidores.

#### Problemas encontrados
Durante el Sprint se identificaron y resolvieron los siguientes inconvenientes:

- revisión de la estructura del nuevo paquete context_builder;
- eliminación de constantes hardcodeadas;
- normalización del contrato público;
- sincronización de la configuración centralizada;
- alineación con la arquitectura consolidada durante los Sprint anteriores.

Todos los problemas fueron resueltos durante el desarrollo del Sprint.

#### Pruebas
Se implementó la suite automatizada:
tests/
└── test_context_builder.py

Resultado obtenido : 25 passed

Se validaron satisfactoriamente:

- implementación de ContextBuilderInterface;
- funcionamiento de SimpleContextBuilder;
- funcionamiento de ContextBuilderFactory;
- preservación del orden de documentos;
- construcción de contexto con múltiples documentos;
- manejo de documentos vacíos.

#### Refactorización
Durante el Sprint se realizaron diversas actividades de mejora del código:

- eliminación de constantes internas;
- centralización de la configuración;
- estandarización de imports;
- fortalecimiento del tipado fuerte;
- consolidación de la arquitectura desacoplada.

#### Mejoras metodológicas
Durante este Sprint se consolidaron nuevas prácticas de desarrollo:

- documentación incremental mediante microentregas;
- sincronización progresiva entre PLAN, SDS y README;
- consolidación del Context Builder como módulo independiente;
- fortalecimiento de la arquitectura basada en interfaces;
- incorporación de estándares permanentes del proyecto dentro del SDS.

#### Archivos creados
- src/context_builder/interfaces.py
- src/context_builder/simple_context_builder.py
- src/context_builder/context_builder_factory.py
- tests/test_context_builder.py

#### Archivos actualizados
- src/config/settings.py
- README.md
- CHANGELOG.md
- PLAN-007.md
- SDS-007_Context_Builder.md
- LOG-001_Bitacora_Tecnica.md
- ROADMAP.md
- HANDBOOK.md
- MTR-001_Matriz_Trazabilidad.md

#### Resultado
##### Context Builder

✔ ContextBuilderInterface

✔ SimpleContextBuilder

✔ ContextBuilderFactory

✔ Configuración centralizada

✔ Construcción de contexto

✔ Pruebas automatizadas

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
Retriever              ✔
      │
      ▼
Context Builder        ✔
      │
      ▼
Decision Engine        ⏳

#### Lecciones aprendidas
- Definir primero el contrato público simplifica la implementación.
- Separar la construcción del contexto del Decision Engine reduce el acoplamiento.
- La configuración centralizada facilita la evolución del módulo.
- El uso de Factory Pattern mantiene uniforme la arquitectura del proyecto.
- La validación incremental permitió desarrollar el módulo sin afectar los Sprint cerrados.

#### Observaciones

Con la finalización del módulo Retriever, el proyecto completa la etapa de recuperación documental del pipeline RAG.

El sistema ya es capaz de:

- cargar documentos;
- fragmentarlos;
- enriquecer su metadata;
- generar embeddings;
- almacenarlos en el Vector Store;
- recuperar información relevante;
- construir un contexto textual listo para ser consumido por el siguiente módulo.

El próximo Sprint estará orientado al desarrollo del **Decision Engine**, responsable de recibir el contexto generado, construir la solicitud para el modelo Gemini y coordinar la generación de respuestas del agente.


## 2026-07-10 -- Cierre del Hito 8

### Sprint 10 - Hito 8

### Registro de avance
Hito 8 – Decision Engine
v0.8.0

#### Objetivo

Implementar el módulo Decision Engine, responsable de construir una solicitud (`LLMRequest`) a partir de la consulta del usuario y del contexto generado por el Context Builder, manteniendo independencia respecto al proveedor LLM y preparando la arquitectura para soportar múltiples modelos de lenguaje.

####  Actividades realizadas

##### Planificación

- Definición del alcance del Decision Engine.
- Identificación de los requisitos funcionales RF-801 a RF-806.
- Definición del contrato público mediante DecisionEngineInterface.
- Diseño de la estrategia para la construcción de solicitudes LLM independientes del proveedor.

##### Diseño

- Elaboración del documento SDS-008 – Decision Engine.
- Definición de la arquitectura basada en interfaces.
- Diseño del patrón Factory para el ensamblado del módulo.
- Definición del modelo LLMRequest.
- Preparación de la arquitectura para futuros proveedores LLM.

##### Implementación
Se implementaron los siguientes componentes:
- DecisionEngineInterface
- LLMRequest
- DecisionEngine

DecisionEngineFactory
Se desarrollaron las siguientes funcionalidades:

- construcción de LLMRequest;
- recepción de query;
- recepción de context;
- desacoplamiento del proveedor LLM;
- implementación del patrón Factory.

#### Decisiones de arquitectura
Durante el desarrollo del módulo se adoptaron las siguientes decisiones arquitectónicas:

- DA-1001
Utilizar DecisionEngineInterface como contrato público..

- DA-1002
Implementar LLMRequest para desacoplar el pipeline del proveedor LLM.

- DA-1003
Implementar DecisionEngineFactory como punto único de creación del módulo.

- DA-1004
Mantener independencia total respecto a Gemini.



#### Problemas encontrados
Durante el Sprint se identificaron y resolvieron los siguientes inconvenientes:
- definición del alcance del Decision Engine;
- reutilización del paquete llm existente;
- decisión sobre el uso de Factory Pattern;
- ajuste de imports durante las pruebas;
- restauración accidental de __init__.py.

Todos los problemas fueron resueltos durante el desarrollo del Sprint.

#### Pruebas
Se implementó la suite automatizada:
tests/
├── test_models.py
├── test_decision_engine.py
└── test_decision_engine_factory.py

Resultado obtenido : 29 passed

Se validaron satisfactoriamente:

- LLMRequest;
- DecisionEngine;
- DecisionEngineFactory;
- integración con el Context Builder mediante contratos públicos.

#### Refactorización
Durante el Sprint se realizaron diversas actividades de mejora del código:

- fortalecimiento del tipado fuerte;
- separación del contrato público mediante DecisionEngineInterface;
- consolidación del modelo LLMRequest;
- mantenimiento del patrón Factory;
- revisión de imports y estructura del paquete llm.

#### Mejoras metodológicas
Durante este Sprint se consolidaron nuevas prácticas de desarrollo:

- inicio de la integración entre módulos del pipeline RAG;
- incorporación de un modelo de intercambio (LLMRequest) entre componentes;
- consolidación de la arquitectura desacoplada del proveedor LLM;
- validación incremental mediante microentregas;
- fortalecimiento de la trazabilidad documental.

#### Archivos creados
- src/llm/interfaces.py
- src/llm/models.py
- src/llm/decision_engine.py
- src/llm/decision_engine_factory.py

- tests/test_models.py
- tests/test_decision_engine.py
- tests/test_decision_engine_factory.py

#### Archivos actualizados
- README.md
- PLAN-008.md
- SDS-008_Decision_Engine.md
- CHANGELOG.md
- LOG-001_Bitacora_Tecnica.md
- ROADMAP.md
- HANDBOOK.md
- MTR-001_Matriz_Trazabilidad.md

#### Resultado
##### Decision Engine

✔ DecisionEngineInterface

✔ LLMRequest

✔ DecisionEngine

✔ DecisionEngineFactory

✔ Pruebas automatizadas

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
Retriever              ✔
      │
      ▼
Context Builder        ✔
      │
      ▼
Decision Engine        ✔
      │
      ▼
LLM Provider           ⏳

#### Lecciones aprendidas
- Definir primero el contrato público facilita la evolución del módulo.
- El uso de LLMRequest desacopla el pipeline del proveedor LLM.
- Mantener el patrón Factory proporciona uniformidad arquitectónica.
- Las microentregas reducen el riesgo de regresiones.
- La validación continua mediante pytest mantiene la estabilidad del proyecto.

#### Observaciones

Con la finalización del **Decision Engine**, el proyecto completa la etapa de preparación de solicitudes para modelos de lenguaje dentro del pipeline RAG.

El sistema ya es capaz de:

- cargar documentos;
- fragmentarlos;
- enriquecer su metadata;
- generar embeddings;
- almacenar información vectorial;
- recuperar documentos relevantes;
- construir el contexto;
- generar una solicitud (LLMRequest) preparada para un proveedor LLM.

El próximo Sprint estará orientado al desarrollo del **LLM Provider**, responsable de consumir las solicitudes generadas por el Decision Engine e integrar Google Gemini mediante una arquitectura desacoplada y extensible.




## 2026-07-11 -- Cierre del Hito 9

### Sprint 11 - Hito 9

### Registro de avance

Hito 9 – Tools
v0.9.0

#### Objetivo

Implementar la infraestructura base del módulo **Tools**, responsable de administrar herramientas especializadas mediante una arquitectura desacoplada basada en interfaces y Factory Pattern, preparando el pipeline RAG para incorporar capacidades adicionales sin modificar el núcleo del sistema.

---

#### Actividades realizadas

##### Planificación

- Definición del alcance del módulo Tools.
- Identificación de los requisitos funcionales RF-901 a RF-908.
- Diseño de la estrategia de administración de herramientas.
- Definición de los contratos públicos del módulo.

##### Diseño

- Elaboración del documento **SDS-009 – Tools**.
- Definición de la arquitectura basada en interfaces.
- Diseño de `ToolInterface`.
- Diseño de `ToolManagerInterface`.
- Diseño del patrón Factory para el ensamblado del módulo.
- Definición de la estrategia de extensibilidad para futuras herramientas.

##### Implementación

Se implementaron los siguientes componentes:

- ToolInterface
- ToolManagerInterface
- ToolManager
- ToolFactory
- DuplicateToolError

También se incorporó:

- DummyTool para pruebas unitarias.

Se desarrollaron las siguientes funcionalidades:

- registro de herramientas;
- validación de implementaciones;
- detección de registros duplicados;
- búsqueda de herramientas;
- ejecución desacoplada;
- preservación del encapsulamiento mediante `has_tool()`.

---

#### Decisiones de arquitectura

Durante el desarrollo del módulo se adoptaron las siguientes decisiones arquitectónicas:

- DA-1101

Implementar `ToolInterface` como contrato público para todas las herramientas.

- DA-1102

Implementar `ToolManagerInterface` para desacoplar la administración de herramientas de su implementación.

- DA-1103

Implementar `ToolFactory` como punto único de ensamblado del módulo.

- DA-1104

Mantener el `DecisionEngine` independiente de cualquier herramienta concreta.

- DA-1105

Aplicar el principio **YAGNI**, evitando incorporar modelos (`ToolRequest` y `ToolResponse`) hasta que exista una necesidad funcional real.

- DA-1106

Incorporar `has_tool()` para preservar el encapsulamiento y eliminar el acceso directo al estado interno del `ToolManager`.

---

#### Problemas encontrados

Durante el Sprint se identificaron y resolvieron los siguientes inconvenientes:

- definición del alcance del módulo Tools;
- ubicación definitiva de las interfaces;
- reutilización del archivo centralizado `exceptions.py`;
- definición del punto correcto para el ensamblado mediante Factory;
- eliminación del acceso directo a `_tools` desde las pruebas;
- organización de `DummyTool` para reutilización.

Todos los problemas fueron resueltos durante el desarrollo del Sprint.

---

#### Pruebas

Se implementó la suite automatizada:

```text
tests/
├── test_tools_interface.py
├── test_tool_manager.py
└── test_tool_factory.py
```

Resultado obtenido:

```text
40 passed
1 warning
```

Se validaron satisfactoriamente:

- ToolInterface;
- ToolManagerInterface;
- ToolManager;
- ToolFactory;
- DuplicateToolError;
- registro de herramientas;
- ejecución desacoplada;
- comportamiento cuando ninguna herramienta puede atender una consulta.

El warning corresponde a ChromaDB con Python 3.14 y queda fuera del alcance del proyecto.

---

#### Refactorización

Durante el Sprint se realizaron diversas actividades de mejora del código:

- incorporación de `ToolManagerInterface`;
- fortalecimiento del encapsulamiento mediante `has_tool()`;
- centralización del ensamblado mediante `ToolFactory`;
- reutilización del archivo `exceptions.py`;
- consolidación del patrón Factory;
- fortalecimiento de las pruebas unitarias.

---

#### Mejoras metodológicas

Durante este Sprint se consolidaron nuevas prácticas de desarrollo:

- documentación independiente por Sprint/Hito;
- incorporación de ADR para registrar decisiones arquitectónicas relevantes;
- validación de contratos antes de implementar componentes;
- revisión arquitectónica previa a la ejecución de pruebas;
- fortalecimiento de la estrategia incremental basada en análisis, implementación, validación y documentación.

---

#### Archivos creados

- src/tools/interfaces.py
- src/tools/tool_manager.py
- src/tools/tool_factory.py
- tests/fixtures/dummy_tool.py
- tests/test_tools_interface.py
- tests/test_tool_manager.py
- tests/test_tool_factory.py

---

#### Archivos actualizados

- src/core/exceptions.py
- README.md
- PLAN-009.md
- SDS-009_Tools.md
- CHANGELOG.md
- LOG-001_Bitacora_Tecnica.md
- ROADMAP.md
- HANDBOOK.md
- MTR-001_Matriz_Trazabilidad.md

---

#### Resultado

##### Tools

✔ ToolInterface

✔ ToolManagerInterface

✔ ToolManager

✔ ToolFactory

✔ Pruebas automatizadas

##### Estado pipeline

```text
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
Retriever              ✔
      │
      ▼
Context Builder        ✔
      │
      ▼
Decision Engine        ✔
      │
      ▼
Tools                  ✔
      │
      ▼
LLM Provider           ⏳
```

---

#### Lecciones aprendidas

- Diseñar primero las interfaces simplifica la evolución del módulo.
- Mantener el ensamblado mediante Factory favorece el desacoplamiento.
- Las decisiones arquitectónicas deben documentarse mediante ADR.
- Las pruebas deben validar la API pública y no el estado interno de las clases.
- La documentación sincronizada reduce inconsistencias entre artefactos del proyecto.

---

#### Observaciones

Con la finalización del módulo **Tools**, el proyecto completa la infraestructura necesaria para incorporar herramientas especializadas al pipeline RAG.

El sistema ya es capaz de:

- cargar documentos;
- fragmentarlos;
- enriquecer su metadata;
- generar embeddings;
- almacenar información vectorial;
- recuperar documentos relevantes;
- construir el contexto;
- generar solicitudes para el modelo de lenguaje;
- administrar herramientas mediante una arquitectura desacoplada.

El próximo Sprint estará orientado al desarrollo del **LLM Provider**, responsable de consumir las solicitudes generadas por el Decision Engine e integrar Google Gemini manteniendo la arquitectura basada en interfaces y Factory Pattern.