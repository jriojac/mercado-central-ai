

# PLAN-006
# Sprint 8 – Hito 6
# Retriever

# Versión: 1.1
# Estado: CERRADO
# Release asociada: v0.6.0
---

## 1. Información General

| Campo    | Valor                    |
| -------- | ------------------------ |
| Proyecto | Mercado Central AI       |
| Sprint   | Sprint 8                 |
| Hito     | Hito 6                   |
| Módulo   | Retriever                |
| Release  | v0.6.0                   |
| Estado   | Finalizado               |
| Fecha    | *(Actualizar al cierre)* |


## 2. Objetivo

Implementar el módulo Retriever del pipeline RAG, responsable de recuperar los documentos más relevantes desde el Vector Store mediante una arquitectura desacoplada basada en interfaces, permitiendo que los módulos superiores consuman un contrato independiente de la tecnología utilizada para el almacenamiento vectorial.

## 3. Alcance

Durante este Sprint se desarrolló:

- Diseño de la interfaz IRetriever.
- Implementación de ChromaRetriever.
- Integración con VectorStore.
- Configuración centralizada del Retriever.
- Implementación de RetrieverFactory.
- Pruebas unitarias del módulo.
- Validación técnica mediante pytest.

## 4. Exclusiones

No forman parte del alcance de este Sprint:

- Context Builder.
- Decision Engine.
- Integración con Gemini.
- Construcción del Prompt.
- Respuesta final del Agente.
- Interfaz Streamlit.

Estos componentes serán desarrollados en Sprint posteriores.

## 5. Entregables

| ID      | Entregable                               | Estado |
| ------- | ---------------------------------------- | :----: |
| RET-001 | Planificación del Sprint                 |    ✅   |
| SDS-006 | Diseño Técnico                           |    ✅   |
| IMP-01  | Estructura del módulo Retriever          |    ✅   |
| IMP-02  | Interfaz `IRetriever`                    |    ✅   |
| IMP-03  | Implementación `ChromaRetriever`         |    ✅   |
| IMP-04  | Validación funcional y pruebas unitarias |    ✅   |
| IMP-05  | Configuración centralizada               |    ✅   |
| IMP-06  | `RetrieverFactory`                       |    ✅   |
| CVT     | Validación técnica                       |    ✅   |


## 6. Microentregas Ejecutadas

### IMP-01 

- Objetivo : Crear la estructura base del módulo Retriever.

- Resultado: Se creó el paquete retriever con los archivos iniciales:

```Text
retriever/
│
├── __init__.py
├── interfaces.py
├── chroma_retriever.py
└── retriever_factory.py
```
- Estado: ✅ Completado

### IMP-02

- Objetivo: Definir el contrato del módulo mediante la interfaz IRetriever.

- Resultado: Se implementó una interfaz abstracta que define el método principal:

```Text
retrieve(query, top_k)
```

estableciendo el contrato común para futuras implementaciones.

- Estado : ✅ Completado

### IMP-03

- Objetivo: Implementar ChromaRetriever.

- Resultado: Se implementó el Retriever reutilizando la API pública de VectorStore, evitando el acceso directo a ChromaDB y manteniendo la encapsulación del Sprint 7.

- Estado: ✅ Completado

### IMP-04

- Objetivo: Validar funcionalmente el Retriever.

- Resultado: Se implementó la primera batería de pruebas unitarias utilizando pytest y Mock, verificando la correcta delegación de llamadas al VectorStore.

- Estado: ✅ Completado

### IMP-05

- Objetivo: Centralizar la configuración del Retriever.

- Resultado: Se incorporaron los parámetros:

RETRIEVER_TOP_K
RETRIEVER_VALIDATE_QUERY

en settings.py, eliminando valores fijos del código.

- Estado: ✅ Completado

### IMP-06

- Objetivo: Implementar la RetrieverFactory.

- Resultado: Se desarrolló la primera Factory oficial del proyecto, responsable de ensamblar las dependencias del módulo Retriever mediante un punto único de creación de objetos.

- Estado: ✅ Completado

## 7. Validaciones

Se realizaron las siguientes validaciones:

- Implementación incremental.
- Validaciones arquitectónicas previas.
- Revisión de estructura del proyecto.
- Validación de imports.
- Refactorización controlada.
- Ejecución completa de pruebas unitarias.

Resultado final: 
18 passed
1 warning


## 8. Riesgos Identificados

Durante el desarrollo se identificaron los siguientes riesgos:

| Riesgo                               | Resolución                                                                                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Estandarización de imports           | Se adoptó el uso de `src.` para imports entre paquetes y relativos dentro del mismo paquete.                      |
| Interfaz no implementada físicamente | Se incorporó la validación de existencia de archivos antes de continuar con una nueva microentrega.               |
| Acoplamiento con ChromaDB            | Se reutilizó `VectorStore` como fachada, evitando dependencias directas del Retriever con el proveedor vectorial. |


## 9. Métricas

| Indicador                  | Valor |
| -------------------------- | ----: |
| Microentregas planificadas |     6 |
| Microentregas completadas  |     6 |
| Entregables completados    | 100 % |
| Pruebas ejecutadas         |    18 |
| Pruebas exitosas           |    18 |
| Fallos                     |     0 |


## 10. Criterios de Cierre

El Sprint se considera finalizado cuando:

✅ Todas las microentregas fueron completadas.
✅ Todas las pruebas unitarias fueron aprobadas.
✅ No existen regresiones respecto a Sprint anteriores.
✅ Se actualiza la documentación oficial.
⏳ Se publica la Release v0.6.0.
⏳ Se genera el Acta de Cierre.

## 11. Observaciones finales

Durante este Sprint se consolidaron varios estándares de arquitectura que servirán como base para el resto del proyecto:

Arquitectura basada en interfaces.
Uso de Factories como punto único de creación de dependencias.
Configuración centralizada mediante settings.py.
Convención oficial de imports (src. entre paquetes e imports relativos dentro del mismo paquete).
Pruebas unitarias aisladas mediante pytest y Mock.
Eliminación de magic numbers mediante configuración.

Estos lineamientos permitirán mantener una arquitectura consistente y escalable durante los Sprint restantes.

