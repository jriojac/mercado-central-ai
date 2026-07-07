# MTR-001 – Matriz de Trazabilidad

| Campo                | Valor                  |
| -------------------- | ---------------------- |
| Código               | MTR-001                |
| Nombre               | Matriz de Trazabilidad |
| Versión              | 2.1                    |
| Estado               | Activo                 |
| Proyecto             | Mercado Central AI     |
| Responsable          | Jacqueline Rioja       |
| Última actualización | Julio 2026             |

---

# 1. Objetivo

Establecer la trazabilidad entre los módulos funcionales del proyecto, los requisitos asociados, los documentos de diseño, la implementación, las pruebas y las releases.

La matriz permite verificar que cada requisito tenga:

- documentación;
- diseño;
- implementación;
- validación;
- seguimiento.

Con ello se garantiza la consistencia entre la planificación y la implementación del proyecto.

---

# 2. Alcance

La matriz cubre todo el ciclo de vida del proyecto:

```text
Requisito
      ↓
Diseño (SDS)
      ↓
Código
      ↓
Pruebas
      ↓
Release
```

Cada nuevo módulo deberá incorporarse a esta matriz antes de considerarse finalizado.

---

# 3. Metodología

La trazabilidad oficial del proyecto sigue la siguiente estructura:

```text
Sprint
      ↓
Hito
      ↓
Requisito
      ↓
SDS
      ↓
Código
      ↓
Pruebas
      ↓
Release
```

Esta metodología fue aprobada durante la Auditoría Arquitectónica (DOC-014).

---

# 4. Matriz de trazabilidad

| Módulo             |   Sprint  |   Hito  | RF                    | SDS     | Código                          | Validación                                            | Release | Estado |
| ------------------ | :-------: | :-----: | --------------------- | ------- | ------------------------------- | ----------------------------------------------------- | :-----: | :----: |
| Document Loader    |  Sprint 3 |  Hito 1 | **RF-101 – RF-105**   | SDS-001 | `loader.py`                     | `check_loader.py`                                     |  v0.1.1 |    ✅   |
| Text Splitter      |  Sprint 4 |  Hito 2 | **RF-201 – RF-205**   | SDS-002 | `text_splitter.py`              | `check_text_splitter.py` / `check_loader_splitter.py` |  v0.2.0 |    ✅   |
| Metadata Manager   |  Sprint 5 |  Hito 3 | **RF-301 – RF-305**   | SDS-003 | `metadata.py` + `exceptions.py` | `check_metadata.py` / `test_metadata.py`              |  v0.3.0 |    ✅   |
| Embeddings Engine  |  Sprint 6 |  Hito 4 | **RF-401 – RF-405**   | SDS-004 | `embeddings.py`                 | `test_embeddings.py`                                  |  v0.4.0 |    ✅   |
| Vector Store       |  Sprint 7 |  Hito 5 | **RF-501 – RF-506**   | SDS-005 | `vector_store.py`               | `test_vector_store.py`                                |  v0.5.0 |    ✅   |
| Retriever          |  Sprint 8 |  Hito 6 | **RF-601 – RF-605**   | SDS-006 | `retriever.py`                  | `test_retriever.py`                                   |  v0.6.0 |    ⏳   |
| Context Builder    |  Sprint 9 |  Hito 7 | **RF-701 – RF-705**   | SDS-007 | `context_builder.py`            | `test_context_builder.py`                             |  v0.7.0 |    ⏳   |
| Decision Engine    | Sprint 10 |  Hito 8 | **RF-801 – RF-805**   | SDS-008 | `decision_engine.py`            | `test_decision_engine.py`                             |  v0.8.0 |    ⏳   |
| Tools              | Sprint 11 |  Hito 9 | **RF-901 – RF-905**   | SDS-009 | `tools/*.py`                    | `test_tools.py`                                       |  v0.9.0 |    ⏳   |
| Interfaz Streamlit | Sprint 12 | Hito 10 | **RF-1001 – RF-1005** | SDS-010 | `app.py`                        | `test_ui.py`                                          |  v1.0.0 |    ⏳   |


---


# 5. Trazabilidad por Sprint

## 5.1 Sprint 3 – Hito 1

### Módulo

Document Loader

---

### Información general

| Campo   | Valor                     |
| ------- | ------------------------- |
| Sprint  | 3                         |
| Hito    | 1                         |
| Módulo  | Document Loader           |
| Estado  | ✅ Implementado y validado |
| Release | v0.1.1                    |


### Matriz de trazabilidad

| RF     | Descripción                                   | SDS     | Implementación | Código        | Casos de prueba | Estado |
| ------ | --------------------------------------------- | ------- | -------------- | ------------- | --------------- | :----: |
| RF-101 | Configurar la ruta de la Base de Conocimiento | SDS-001 | IMP-01         | `settings.py` | CP-001          |    ✅   |
| RF-102 | Detectar automáticamente documentos PDF       | SDS-001 | IMP-02         | `loader.py`   | CP-002          |    ✅   |
| RF-103 | Cargar documentos mediante LangChain          | SDS-001 | IMP-03         | `loader.py`   | CP-003          |    ✅   |
| RF-104 | Validar la carga de documentos                | SDS-001 | IMP-04         | `loader.py`   | CP-004          |    ✅   |
| RF-105 | Integrar el módulo con el pipeline            | SDS-001 | IMP-05         | `loader.py`   | CP-005          |    ✅   |


### Cobertura de requisitos

| Tipo                   |  Cantidad |
| ---------------------- | --------: |
| Requisitos funcionales |         5 |
| Implementaciones       |         5 |
| Casos de prueba        |         5 |
| Requisitos cubiertos   |         5 |
| Cobertura              | **100 %** |


### Inventario de artefactos

| Categoría              | Artefacto                    | Descripción                                                                             |
| ---------------------- | ---------------------------- | --------------------------------------------------------------------------------------- |
| Código fuente          | `loader.py`                  | Implementa la carga automática de documentos PDF mediante LangChain.                    |
| Configuración          | `settings.py`                | Define la ubicación de la Base de Conocimiento y la configuración inicial del proyecto. |
| Base de conocimiento   | `knowledge_base/`            | Directorio que contiene los documentos PDF utilizados por el proyecto.                  |
| Pruebas automatizadas  | `test_loader.py`             | Valida el correcto funcionamiento del módulo Document Loader.                           |
| Pruebas de integración | `check_loader.py`            | Verifica el flujo completo de carga de documentos desde la Base de Conocimiento.        |
| Documentación          | `SDS-001_Document_Loader.md` | Especificación de Diseño del módulo Document Loader.                                    |
| Release                | `v0.1.1`                     | Primera versión estable del proyecto.                                                   |


### Resultado

El módulo Document Loader fue implementado exitosamente como primer componente del pipeline RAG del proyecto.

Se validó la carga automática de documentos PDF desde la Base de Conocimiento utilizando LangChain, garantizando la correcta lectura y preparación de la información para el siguiente módulo (Text Splitter).

Durante este Sprint se establecieron las bases de la arquitectura del proyecto, incluyendo la estructura inicial del repositorio, la configuración centralizada mediante settings.py y las primeras pruebas funcionales del flujo de carga documental.

El Sprint concluyó con la publicación de la Release v0.1.1, validando el funcionamiento completo del módulo y alcanzando una cobertura funcional del 100 %.

## 5.2 Sprint 4 – Hito 2

### Módulo

Text Splitter

### Información general

| Campo   | Valor                     |
| ------- | ------------------------- |
| Sprint  | 4                         |
| Hito    | 2                         |
| Módulo  | Text Splitter             |
| Estado  | ✅ Implementado y validado |
| Release | v0.2.0                    |

### Matriz de trazabilidad

| RF     | Descripción                                | SDS     | Implementación | Código                           | Casos de prueba | Estado |
| ------ | ------------------------------------------ | ------- | -------------- | -------------------------------- | --------------- | :----: |
| RF-201 | Dividir documentos en fragmentos (chunks)  | SDS-002 | IMP-201        | `text_splitter.py`               | CP-201          |    ✅   |
| RF-202 | Configurar tamaño y solapamiento de chunks | SDS-002 | IMP-202        | `settings.py`                    | CP-202          |    ✅   |
| RF-203 | Enriquecer la metadata de cada chunk       | SDS-002 | IMP-203        | `text_splitter.py`               | CP-203          |    ✅   |
| RF-204 | Integrar Document Loader con Text Splitter | SDS-002 | IMP-204        | `loader.py` + `text_splitter.py` | CP-204          |    ✅   |
| RF-205 | Validar el flujo completo de segmentación  | SDS-002 | IMP-205        | Pipeline                         | CP-205          |    ✅   |

### Cobertura de requisitos

| Tipo                   |  Cantidad |
| ---------------------- | --------: |
| Requisitos funcionales |         5 |
| Implementaciones       |         5 |
| Casos de prueba        |         5 |
| Requisitos cubiertos   |         5 |
| Cobertura              | **100 %** |

### Inventario de artefactos

| Categoría              | Artefacto                  | Descripción                                                  |
| ---------------------- | -------------------------- | ------------------------------------------------------------ |
| Código fuente          | `text_splitter.py`         | Implementa la segmentación de documentos mediante LangChain. |
| Código fuente          | `loader.py`                | Integración con Document Loader.                             |
| Configuración          | `settings.py`              | Parámetros de tamaño y solapamiento de chunks.               |
| Pruebas automatizadas  | `test_text_splitter.py`    | Validación unitaria del módulo.                              |
| Pruebas de integración | `check_loader_splitter.py` | Validación del flujo Loader → Splitter.                      |
| Pruebas de integración | `check_text_splitter.py`   | Validación manual del proceso de segmentación.               |
| Documentación          | `SDS-002_Text_Splitter.md` | Especificación de diseño del módulo.                         |
| Release                | `v0.2.0`                   | Primera versión estable del módulo.                          |

### Resultado

El módulo Text Splitter fue implementado como el segundo componente del pipeline RAG, permitiendo transformar los documentos cargados por el Document Loader en fragmentos de texto (chunks) adecuados para el procesamiento semántico.

La implementación incorporó el uso de RecursiveCharacterTextSplitter de LangChain, con parámetros configurables para el tamaño y el solapamiento de los fragmentos, preservando la continuidad del contexto entre ellos.

Durante este Sprint también se enriqueció la metadata de cada chunk, facilitando su identificación y trazabilidad en las etapas posteriores del pipeline.

Finalmente, se integró el módulo con el Document Loader, validando el flujo completo de carga y segmentación de documentos.

El Sprint concluyó con la publicación de la Release v0.2.0, alcanzando una cobertura funcional del 100 % y estableciendo la base para el desarrollo del Metadata Manager.

---

## 5.3 Sprint 5 – Hito 3

### Módulo

Metadata Manager

### Información general

| Campo   | Valor                     |
| ------- | ------------------------- |
| Sprint  | 5                         |
| Hito    | 3                         |
| Módulo  | Metadata Manager          |
| Estado  | ✅ Implementado y validado |
| Release | v0.3.0                    |

### Matriz de trazabilidad

| RF     | Descripción                                  | SDS     | Implementación | Código                             | Casos de prueba | Estado |
| ------ | -------------------------------------------- | ------- | -------------- | ---------------------------------- | --------------- | :----: |
| RF-301 | Normalizar la metadata de los documentos     | SDS-003 | IMP-301        | `metadata.py`                      | CP-301          |    ✅   |
| RF-302 | Enriquecer la metadata de los chunks         | SDS-003 | IMP-302        | `metadata.py`                      | CP-302          |    ✅   |
| RF-303 | Validar la estructura de la metadata         | SDS-003 | IMP-303        | `metadata.py`                      | CP-303          |    ✅   |
| RF-304 | Integrar Text Splitter con Metadata Manager  | SDS-003 | IMP-304        | `text_splitter.py` + `metadata.py` | CP-304          |    ✅   |
| RF-305 | Validar el flujo completo de enriquecimiento | SDS-003 | IMP-305        | Pipeline                           | CP-305          |    ✅   |


### Cobertura de requisitos

| Tipo                   |  Cantidad |
| ---------------------- | --------: |
| Requisitos funcionales |         5 |
| Implementaciones       |         5 |
| Casos de prueba        |         5 |
| Requisitos cubiertos   |         5 |
| Cobertura              | **100 %** |


### Inventario de artefactos

| Categoría              | Artefacto                     | Descripción                                                                                          |
| ---------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| Código fuente          | `metadata.py`                 | Implementa la normalización, enriquecimiento y validación de la metadata de los documentos y chunks. |
| Configuración          | `settings.py`                 | Parámetros generales utilizados por el módulo Metadata Manager.                                      |
| Pruebas automatizadas  | `test_metadata.py`            | Validación unitaria de las funciones del módulo.                                                     |
| Pruebas de integración | `check_metadata.py`           | Validación del flujo Text Splitter → Metadata Manager.                                               |
| Documentación          | `SDS-003_Metadata_Manager.md` | Especificación de diseño del módulo.                                                                 |
| Release                | `v0.3.0`                      | Primera versión estable del Metadata Manager.                                                        |

### Resultados

El módulo Metadata Manager fue implementado como el tercer componente del pipeline RAG, siendo responsable de normalizar, enriquecer y validar la información descriptiva asociada a cada fragmento de documento antes de la generación de embeddings.

Durante este Sprint se definió un modelo consistente de metadata, incorporando información relevante para la trazabilidad y recuperación posterior de los documentos, tales como el documento de origen, número de página, posición del fragmento y demás atributos necesarios para el procesamiento del pipeline.

El módulo fue integrado exitosamente con Text Splitter, validando el flujo completo de preparación de datos previo a la etapa de generación de embeddings.

El Sprint concluyó con la publicación de la Release v0.3.0, alcanzando una cobertura funcional del 100 % y estableciendo la base para el desarrollo del Embeddings Engine.

---

## 5.4 Sprint 6 – Hito 4

### Módulo

Embeddings Engine

### Información general

| Campo   | Valor                     |
| ------- | ------------------------- |
| Sprint  | 6                         |
| Hito    | 4                         |
| Módulo  | Embeddings Engine         |
| Estado  | ✅ Implementado y validado |
| Release | v0.4.0                    |

### Matriz de trazabilidad

| RF     | Descripción                                     | SDS     | Implementación | Código          | Casos de prueba | Estado |
| ------ | ----------------------------------------------- | ------- | -------------- | --------------- | --------------- | :----: |
| RF-401 | Inicializar el proveedor de embeddings          | SDS-004 | IMP-401        | `embeddings.py` | CP-401          |    ✅   |
| RF-402 | Configurar el proveedor mediante `settings.py`  | SDS-004 | IMP-402        | `settings.py`   | CP-402          |    ✅   |
| RF-403 | Generar embeddings individuales                 | SDS-004 | IMP-403        | `embeddings.py` | CP-403          |    ✅   |
| RF-404 | Generar embeddings por lote                     | SDS-004 | IMP-404        | `embeddings.py` | CP-404          |    ✅   |
| RF-405 | Integrar Metadata Manager con Embeddings Engine | SDS-004 | IMP-405        | Pipeline        | CP-405          |    ✅   |

### Cobertura de requisitos

| Tipo                   |  Cantidad |
| ---------------------- | --------: |
| Requisitos funcionales |         5 |
| Implementaciones       |         5 |
| Casos de prueba        |         5 |
| Requisitos cubiertos   |         5 |
| Cobertura              | **100 %** |

### Inventario de artefactos

| Categoría              | Artefacto                      | Descripción                                                                 |
| ---------------------- | ------------------------------ | --------------------------------------------------------------------------- |
| Código fuente          | `embeddings.py`                | Implementa la generación de embeddings utilizando el proveedor configurado. |
| Configuración          | `settings.py`                  | Define el proveedor, modelo y parámetros de generación de embeddings.       |
| Pruebas automatizadas  | `test_embeddings.py`           | Valida la generación de embeddings y el procesamiento por lote.             |
| Pruebas de integración | `check_pipeline_embeddings.py` | Valida el flujo Metadata Manager → Embeddings Engine.                       |
| Documentación          | `SDS-004_Embeddings_Engine.md` | Especificación de diseño del módulo.                                        |
| Release                | `v0.4.0`                       | Primera versión estable del Embeddings Engine.                              |


### Resultados

El módulo Embeddings Engine fue implementado como el cuarto componente del pipeline RAG, siendo responsable de transformar el contenido textual enriquecido por el Metadata Manager en representaciones vectoriales de alta dimensión (embeddings).

Durante este Sprint se desarrolló una arquitectura desacoplada mediante el patrón Strategy, permitiendo seleccionar el proveedor de embeddings desde la configuración centralizada del proyecto y facilitando la incorporación de nuevos proveedores sin modificar la lógica del pipeline.

Asimismo, se implementó el procesamiento individual y por lotes, optimizando la generación de embeddings para grandes volúmenes de documentos y garantizando la preservación de la metadata asociada a cada fragmento.

El módulo fue integrado satisfactoriamente con el Metadata Manager, validando el flujo completo previo al almacenamiento vectorial.

El Sprint concluyó con la publicación de la Release v0.4.0, alcanzando una cobertura funcional del 100 % y dejando preparado el proyecto para la implementación del Vector Store.

---

## 5.5 Sprint 7 – Hito 5

### Módulo

Vector Store

### Información general

| Campo   | Valor                     |
| ------- | ------------------------- |
| Sprint  | 7                         |
| Hito    | 5                         |
| Módulo  | Vector Store              |
| Estado  | ✅ Implementado y validado |
| Release | **v0.5.0**                |

### Matriz de trazabilidad

| RF     | Descripción                                 | SDS     | Implementación | Código                                      | Casos de prueba | Estado |
| ------ | ------------------------------------------- | ------- | -------------- | ------------------------------------------- | --------------- | :----: |
| RF-501 | Crear y administrar colecciones vectoriales | SDS-005 | IMP-501        | `create_collection()` / `load_collection()` | CP-501          |    ✅   |
| RF-502 | Almacenar documentos vectoriales            | SDS-005 | IMP-502        | `add_documents()`                           | CP-502          |    ✅   |
| RF-503 | Contar documentos almacenados               | SDS-005 | IMP-503        | `count_documents()`                         | CP-503          |    ✅   |
| RF-504 | Ejecutar búsquedas por similitud            | SDS-005 | IMP-504        | `similarity_search()`                       | CP-504          |    ✅   |
| RF-505 | Eliminar documentos del Vector Store        | SDS-005 | IMP-505        | `delete_documents()`                        | CP-505          |    ✅   |
| RF-506 | Reiniciar completamente una colección       | SDS-005 | IMP-506        | `reset()`                                   | CP-506          |    ✅   |

### Cobertura de requisitos

| Tipo                   |  Cantidad |
| ---------------------- | --------: |
| Requisitos funcionales |         6 |
| Implementaciones       |         6 |
| Casos de prueba        |         8 |
| Requisitos cubiertos   |         6 |
| Cobertura              | **100 %** |

### Inventario de artefactos

| Categoría             | Artefacto                 | Descripción                                                                                        |
| --------------------- | ------------------------- | -------------------------------------------------------------------------------------------------- |
| Código fuente         | `vector_store.py`         | Define la interfaz pública del módulo Vector Store.                                                |
| Código fuente         | `provider.py`             | Implementa la interfaz abstracta para proveedores de almacenamiento vectorial.                     |
| Código fuente         | `chroma_provider.py`      | Implementación concreta utilizando ChromaDB como motor vectorial.                                  |
| Código fuente         | `types.py`                | Define los modelos `VectorDocument` y `SearchResult`.                                              |
| Código fuente         | `constants.py`            | Centraliza constantes utilizadas por el módulo.                                                    |
| Configuración         | `settings.py`             | Configuración del proveedor, colección y almacenamiento persistente.                               |
| Pruebas automatizadas | `test_vector_store.py`    | Valida la totalidad de la interfaz pública del módulo mediante ocho casos de prueba automatizados. |
| Documentación         | `SDS-005_Vector_Store.md` | Especificación de Diseño del módulo Vector Store.                                                  |
| Release               | `v0.5.0`                  | Primera versión estable del módulo Vector Store.                                                   |

### Arquitectura implementada

El módulo Vector Store fue diseñado siguiendo una arquitectura desacoplada basada en el patrón Strategy, permitiendo abstraer la implementación del motor de almacenamiento vectorial mediante la interfaz VectorStoreProvider.

La implementación concreta fue desarrollada a través de la clase ChromaProvider, responsable de encapsular todas las operaciones específicas de ChromaDB, mientras que el resto del sistema interactúa únicamente con la interfaz pública del módulo.

Esta arquitectura proporciona las siguientes ventajas:

- Separación entre la lógica del dominio y la infraestructura de almacenamiento.
- Posibilidad de incorporar nuevos proveedores vectoriales.
- Mayor mantenibilidad y facilidad para pruebas.
- Configuración centralizada mediante settings.py.
- Cumplimiento de los principios SOLID (DIP y OCP).

### Resultados

El módulo Vector Store fue implementado como el quinto componente del pipeline RAG, proporcionando la persistencia y recuperación eficiente de documentos vectoriales generados por el Embeddings Engine.

Durante este Sprint se desarrolló una arquitectura extensible basada en interfaces y proveedores, permitiendo desacoplar completamente la lógica del sistema de la tecnología utilizada para el almacenamiento vectorial.

La implementación incluyó la administración de colecciones, inserción de documentos, consultas por similitud, conteo de registros, eliminación de documentos y reinicio completo de colecciones, garantizando un conjunto completo de operaciones para la gestión del almacenamiento vectorial.

Asimismo, se incorporó una estrategia de pruebas automatizadas mediante pytest, alcanzando una cobertura funcional del 100 % con ocho casos de prueba independientes que validan la totalidad de la interfaz pública del módulo.

El Sprint concluyó con la publicación de la Release v0.5.0, consolidando la infraestructura de almacenamiento semántico del proyecto y dejando preparado el pipeline para la implementación del módulo Retriever, responsable de recuperar los documentos más relevantes para la generación de contexto.

---

## 5.6 Sprint Y – Hito Z

### Módulo

### Información general

### Matriz de trazabilidad

### Cobertura de requisitos

### Inventario de artefactos

### Resultados

---

## 5.X Sprint Y – Hito Z

### Módulo

### Información general

### Matriz de trazabilidad

### Cobertura de requisitos

### Inventario de artefactos

### Resultados

---

## 5.X Sprint Y – Hito Z

### Módulo

### Información general

### Matriz de trazabilidad

### Cobertura de requisitos

### Inventario de artefactos

### Resultados

---



------------

# 6. Convenciones

## Identificación de artefactos

| Prefijo | Descripción                   |
| ------- | ----------------------------- |
| RF      | Requisito Funcional           |
| IMP     | Implementación                |
| CP      | Caso de Prueba                |
| SDS     | Software Design Specification |
| DOC     | Documento técnico             |
| PLAN    | Documento de planificación    |
| LOG     | Bitácora técnica              |
| MTR     | Matriz de Trazabilidad        |
| REL     | Release del proyecto          |

## Convención de numeración

La numeración se reinicia por Sprint utilizando centenas para facilitar la identificación del origen de cada requisito, implementación y caso de prueba.

| Sprint   | RF     | IMP     | CP     |
| -------- | ------ | ------- | ------ |
| Sprint 3 | RF-101 | IMP-101 | CP-101 |
| Sprint 4 | RF-201 | IMP-201 | CP-201 |
| Sprint 5 | RF-301 | IMP-301 | CP-301 |
| Sprint 6 | RF-401 | IMP-401 | CP-401 |
| Sprint 7 | RF-501 | IMP-501 | CP-501 |


## Estados

| Estado | Significado             |
| ------ | ----------------------- |
| ✅      | Implementado y validado |
| ⏳      | Planificado             |
| 🔄     | En desarrollo           |
| ❌      | No implementado         |

## Cobertura

La cobertura mostrada en este documento representa la relación entre los requisitos funcionales implementados y los casos de prueba ejecutados satisfactoriamente.

Cada requisito funcional debe estar asociado al menos a un caso de prueba y a una implementación específica.

## Artefactos

Para cada Sprint se registra el inventario de artefactos generados durante el desarrollo.

Los artefactos pueden pertenecer a las siguientes categorías:

- Código fuente
- Configuración
- Pruebas automatizadas
- Pruebas de integración
- Documentación técnica
- Releases

---

# 7. Observaciones

## Evolución del proyecto

La matriz de trazabilidad se actualiza al cierre de cada Sprint, registrando la relación entre los requisitos funcionales, las implementaciones realizadas, los casos de prueba ejecutados y los artefactos generados durante el desarrollo.

Este documento constituye el principal mecanismo de seguimiento del avance técnico del proyecto.

## Estrategía de calidad

A partir del Sprint 6 se consolidó el uso de pruebas automatizadas mediante pytest, complementadas con pruebas de integración y validaciones manuales durante el desarrollo.

Esta estrategia garantiza la validación continua de cada módulo antes de su incorporación al pipeline RAG

## Evolución arquitectónica

El proyecto evoluciona mediante una arquitectura modular basada en componentes desacoplados, donde cada Sprint incorpora un nuevo módulo funcional al pipeline.

Cada componente mantiene responsabilidades claramente definidas y se integra progresivamente con los módulos desarrollados en Sprint anteriores

## Trazabilidad

Cada requisito funcional documentado en este MTR mantiene correspondencia con:

- Su especificación de diseño (SDS).
- La implementación realizada.
- El código fuente asociado.
- Los casos de prueba ejecutados.
- La Release donde fue incorporado.

Esta trazabilidad permite auditar el ciclo completo de desarrollo de cada funcionalidad.

## Estado actual del proyecto

Al cierre del Sprint 7 – Hito 5, el proyecto cuenta con cinco módulos funcionales implementados y validados:

- ✅ Document Loader
- ✅ Text Splitter
- ✅ Metadata Manager
- ✅ Embeddings Engine
- ✅ Vector Store

Estos componentes constituyen la infraestructura base del pipeline RAG y preparan el proyecto para el desarrollo del módulo Retriever, correspondiente al Sprint 8 – Hito 6.