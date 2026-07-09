
# PLAN-007
# Sprint 9 – Hito 7
# Context Builder

Versión: 1.0
Estado: EN DESARROLLO
Release asociada: v0.7.0

---

## 1. Información General

| Campo   | Valor           |
| ------- | --------------- |
| Sprint  | Sprint 9        |
| Hito    | Hito 7          |
| Módulo  | Context Builder |
| Release | v0.7.0          |
| Estado  | En desarrollo   |


## 2. Objetivo

Implementar el módulo Context Builder del pipeline RAG, responsable de transformar los documentos recuperados por el Retriever en un contexto textual único, preservando el orden por relevancia, respetando los límites de longitud definidos por la configuración y manteniendo independencia respecto al modelo de lenguaje utilizado por el sistema.

## 3. Alcance

Durante este Sprint se desarrolló:

- Diseño de la interfaz ContextBuilderInterface.
- Implementación de SimpleContextBuilder.
- Implementación de ContextBuilderFactory.
- Configuración centralizada del Context Builder.
- Construcción del contexto textual.
- Pruebas unitarias.
- Validación mediante pytest.

## 4. Exclusiones

No forman parte del alcance de este Sprint:

- Decision Engine.
- Prompt Builder.
- Integración con Gemini.
- Herramientas (Tools).
- Interfaz Streamlit.
- Respuesta final del Agente.

Estos componentes serán desarrollados en Sprint posteriores.

## 5. Entregables

| ID      | Entregable                             |
| ------- | -------------------------------------- |
| RET-001 | Planificación del Sprint               |
| SDS-007 | Diseño Técnico                         |
| IMP-01  | Estructura del módulo Context Builder  |
| IMP-02  | Interfaz `ContextBuilderInterface`     |
| IMP-03  | Implementación `SimpleContextBuilder`  |
| IMP-04  | Implementación `ContextBuilderFactory` |
| IMP-05  | Configuración centralizada             |
| IMP-06  | Pruebas unitarias                      |
| CVT     | Validación técnica                     |


## 6. Microentregas Ejecutadas

### IMP-01 – Creación de la estructura del paquete context_builder.

- Objetivo : Crear la estructura base del módulo Context Builder.

- Resultado: Se creó el paquete retriever con los archivos iniciales:

```Text
context_builder/
    ├── __init__.py
    ├── interfaces.py
    ├── simple_context_builder.py
    └── context_builder_factory.py
```
- Estado: ✅ Completado

### IMP-02 – Implementación de ContextBuilderInterface

- Objetivo: Definir el contrato público del módulo mediante ContextBuilderInterface.

- Resultado: Se implementó una interfaz abstracta que define el método:

```python
build_context(
    documents: list[Document]
) -> str
```

estableciendo el contrato común para futuras implementaciones.

- Estado : ✅ Completado

### IMP-03 – Desarrollo de SimpleContextBuilder.

- Objetivo: Implementar SimpleContextBuilder.

- Resultado: Se implementó la primera estrategia de construcción de contexto.

- Artefactos generados :  simple_context_builder.py

- Estado: ✅ Completado

### IMP-04 – Implementación de ContextBuilderFactory.

- Objetivo: Implementar ContextBuilderFactory

- Resultado: Se desarrolló la Factory responsable de ensamblar la implementación concreta del Context Builder mediante un punto único de creación de dependencias.

- Estado: ✅ Completado

### IMP-05 – Centralización de la configuración en settings.py.

- Objetivo: Centralizar la configuración del Context Builder.

- Resultado: Se incorporaron los parámetros:

    * CONTEXT_SEPARATOR
    * MAX_CONTEXT_CHARS
    * INCLUDE_METADATA

en settings.py, eliminando valores fijos del código.

- Estado: ✅ Completado

### IMP-06 – Implementación de test_context_builder.py.

- Objetivo: Implementar las pruebas unitarias del Context Builder.

- Resultado: Se desarrolló la batería inicial de pruebas automatizadas utilizando pytest, validando:

    * contexto vacío;
    * documento único;
    * múltiples documentos;
    * preservación del orden;
    * documentos vacíos;
    * funcionamiento de ContextBuilderFactory.

- Estado: ✅ Completado

## 7. Validaciones
Actualizar contenido
Se realizaron las siguientes validaciones:

- Implementación incremental.
- Validaciones arquitectónicas previas.
- Revisión de estructura del proyecto.
- Validación de imports.
- Refactorización controlada.
- Ejecución completa de pruebas unitarias.

Resultado final: 
25 passed
0  warning

## 8. Riesgos Identificados

Durante el desarrollo se identificaron los siguientes riesgos:

| Riesgo                              | Resolución                                                                                               |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Acoplamiento con el LLM             | El Context Builder no invoca directamente a Gemini.                                                      |
| Crecimiento del contexto            | Se definió configuración centralizada para controlar la longitud máxima.                                 |
| Futuras estrategias de construcción | Se utilizó una interfaz y una Factory para permitir nuevas implementaciones sin modificar el consumidor. |



## 9. Métricas

| Indicador                  | Valor |
| -------------------------- | ----: |
| Microentregas planificadas |     6 |
| Microentregas completadas  |     6 |
| Entregables completados    | 100 % |
| Pruebas ejecutadas         |    25 |
| Pruebas exitosas           |    25 |
| Fallos                     |     0 |



## 10. Criterios de Cierre

El Sprint se considera finalizado cuando:

✅ Todas las microentregas fueron completadas.
✅ Todas las pruebas unitarias fueron aprobadas.
✅ No existen regresiones respecto a Sprint anteriores.
✅ Se actualiza la documentación oficial.
✅ Se publica la Release v0.7.0.
✅ Se genera el Acta de Cierre.


## 11. Observaciones finales

Durante este Sprint se consolidaron varios estándares de arquitectura que servirán como base para el resto del proyecto:

- Separación clara entre Retriever y Context Builder.
- Independencia del modelo LLM.
- Construcción desacoplada del contexto mediante interfaces y Factory.
- Configuración centralizada del Context Builder.
- Preservación del orden de relevancia entregado por el Retriever.
- Base preparada para futuras estrategias de construcción de contexto.

Estos lineamientos permitirán mantener una arquitectura consistente y escalable durante los Sprint restantes.

