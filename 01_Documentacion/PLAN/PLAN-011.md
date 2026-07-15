# PLAN-011
# Sprint 13 – Hito 11
# Interfaz Streamlit

Versión: 1.0
Estado: EN DESARROLLO
Release asociada: v1.1.0

---

## 1. Información General

| Campo   | Valor                |
| ------- | -------------------- |
| Sprint  | Sprint 13            |
| Hito    | Hito 11              |
| Módulo  | Interfaz Streamlit   |
| Release | v1.1.0               |
| Estado  | En desarrollo        |


## 2. Objetivo

Implementar la interfaz gráfica del proyecto Mercado Central AI mediante Streamlit, integrando el pipeline RAG desarrollado en los Sprint anteriores en una aplicación funcional de extremo a extremo.

La interfaz será responsable de capturar consultas del usuario, invocar el pipeline RAG y presentar las respuestas generadas por Google Gemini, manteniendo la arquitectura basada en Interfaces, Factory Pattern y configuración centralizada.

## 3. Alcance

Durante este Sprint se desarrollará:

- Aplicación principal mediante Streamlit.
- Implementación de StreamlitApp.
- Implementación de PromptBuilder.
- Implementación de RAGPipeline.
- Implementación de RAGPipelineFactory.
- Integración completa con:
    - Retriever
    - Context Builder
    - Decision Engine
    - LLM Provider
    - Google Gemini
- Configuración centralizada mediante settings.py.
- Integración mediante cache_resource.
- Validaciones manuales.
- Pruebas de integración.


## 4. Exclusiones

No forman parte del alcance de este Sprint:

- Memoria conversacional.
- Historial de conversaciones.
- Persistencia de chats.
- Autenticación.
- Streaming de respuestas.
- Despliegue en la nube.
- Inicialización automática de la Base Vectorial.

## 5. Entregables

| ID     | Entregable                          |
| ------ | ----------------------------------- |
| IMP-01 | Diseño de la arquitectura Streamlit |
| IMP-02 | Implementación de StreamlitApp      |
| IMP-03 | Integración del pipeline RAG        |
| IMP-04 | Validación funcional de la interfaz |
| IMP-05 | Actualización documental            |



## 6. Microentregas Ejecutadas

### IMP-01 →  Diseño de la arquitectura Streamlit
- Resultado:
    * Definición de la arquitectura de la interfaz.
    * Diseño del flujo completo de interacción.
    * Definición de responsabilidades.
- Estado: ✅ Completado

### IMP-02 → Implementación de StreamlitApp .
- Resultado:
    * Implementación de StreamlitApp.
    * Configuración de la interfaz.
    * Integración de app.py.
- Estado: ✅ Completado

### IMP-03 → Integración del pipeline RAG   .
- Resultado:
    * Implementación de PromptBuilder.
    * Implementación de RAGPipeline.
    * Implementación de RAGPipelineFactory.
    * Integración con el pipeline RAG.
    * Integración con @st.cache_resource.
- Estado: ✅ Completado

### IMP-04 → Validación funcional de la interfaz.
- Resultado:
    * Validación de la interfaz.
    * Integración con el Retriever.
    * Validación del flujo completo.
    * Identificación de la ausencia de una colección vectorial inicializada.
- Estado: ✅ Completado

### IMP-05 → Actualización documental.
- Resultado:
    * Actualización documental.
    * Preparación de la Release v1.1.0.
- Estado: ✅ Completado
---

## 7. Validaciones

Validaciones funcionales realizadas:

- Carga correcta de la interfaz Streamlit.
- Integración con RAGPipeline.
- Integración con RAGPipelineFactory.
- Ejecución del flujo completo hasta Retriever.
- Validación del manejo centralizado de errores.

Resultado final:

43 passed
1 warning

- El warning corresponde a ChromaDB con Python 3.14 y queda fuera del alcance del proyecto

## 8. Riesgos Identificados

Durante el desarrollo se identificaron los siguientes riesgos:

| Riesgo                              | Mitigación                                            |
| ----------------------------------- | ----------------------------------------------------- |
| Cambios en la API de Gemini         | Encapsular la integración en `GoogleGeminiProvider`.  |
| Cambios en LangChain                | Aislar el uso de LangChain dentro del Provider.       |
| Incorporación de nuevos proveedores | Uso de `LLMProviderInterface` + `LLMProviderFactory`. |
| Base vectorial sin inicializar | Implementar un proceso de inicialización en el siguiente Sprint. |


## 9. Métricas

| Indicador                  | Valor |
| -------------------------- | ----: |
| Microentregas planificadas |     5 |
| Microentregas completadas  |     4 |
| Microentregas pendientes   |     1 |
| Pruebas ejecutadas         |    43 |
| Pruebas exitosas           |    43 |
| Fallos                     |     0 |


## 10. Criterios de Cierre

El Sprint se considera finalizado cuando:

✅ Todas las microentregas fueron completadas.
✅ Todas las pruebas unitarias fueron aprobadas.
✅ No existen regresiones respecto a Sprint anteriores.
✅ Se actualiza la documentación oficial.
✅ Se publica la Release v1.0.0.
✅ Se genera el Acta de Cierre.
✅ La interfaz ejecuta correctamente el pipeline RAG.

⏳ La Base Vectorial deberá encontrarse inicializada para obtener respuestas reales.


## 11. Observaciones finales

Durante el Sprint 13 se integró por primera vez todo el pipeline RAG mediante una interfaz gráfica desarrollada con Streamlit.

Como resultado del proceso de integración se identificó la necesidad de incorporar un mecanismo formal de inicialización de la Base Vectorial. Esta funcionalidad no modifica la arquitectura existente y será abordada en el siguiente Sprint para completar el ciclo de ingestión de conocimiento.

La arquitectura mantiene los principios de desacoplamiento, responsabilidad única, Factory Pattern, Interfaces y configuración centralizada consolidados durante los Sprint anteriores.