# DOC-001 – Definición del Proyecto

## 1. Resumen Ejecutivo

Se desarrollará un Agente Inteligente de Atención basado en IA Generativa y RAG para responder consultas utilizando exclusivamente la documentación oficial de Mercado Central 24h.

## 2. Objetivo General

Centralizar el conocimiento de la organización y ofrecer respuestas precisas para clientes, proveedores y colaboradores.

## 3. Objetivos Específicos

- Responder preguntas sobre documentación oficial.
- Consultar inventario.
- Consultar sucursales.
- Atender consultas de proveedores.
- Mantener contexto conversacional.
- Mostrar la fuente documental utilizada.

## 4. Alcance

El MVP incluirá consultas sobre FAQ, políticas de atención, reglamento interno, manual de proveedores, inventario y directorio corporativo de sucursales.

## 5. Fuera de Alcance

- Procesamiento de pedidos.
- Compras en línea.
- Modificación de inventario.
- Integración con ERP real.
- Acciones transaccionales.

## 6. Usuarios

Clientes, Proveedores y Colaboradores.

## 7. Requisitos Funcionales (RF)

RF-001 Responder únicamente con información oficial.
RF-002 Consultar FAQ.
RF-003 Consultar Política de Atención.
RF-004 Consultar Reglamento Interno.
RF-005 Consultar Manual de Proveedores.
RF-006 Consultar Inventario.
RF-007 Consultar Directorio de Sucursales.
RF-008 Mantener contexto.
RF-009 Informar cuando no exista información.
RF-010 Mostrar la fuente documental.

## 8. Requisitos No Funcionales (RNF)

RNF-001 Respuestas en español.
RNF-002 Tiempo de respuesta adecuado para demo.
RNF-003 Arquitectura modular.
RNF-004 Componentes gratuitos cuando sea posible.
RNF-005 Código documentado.

## 9. Casos de Uso Iniciales (CU)

CU-001 Consultar FAQ.
CU-002 Consultar devoluciones.
CU-003 Consultar requisitos para proveedores.
CU-004 Consultar inventario.
CU-005 Consultar sucursales.

## 10. Herramientas del Agente (TL)

TL-001 FAQ Tool
TL-002 Customer Policy Tool
TL-003 Inventory Tool
TL-004 Supplier Tool
TL-005 Branch Tool

## 11. Prompts (PR)

PR-001 System Prompt
PR-002 FAQ Prompt
PR-003 Inventory Prompt
PR-004 Supplier Prompt
PR-005 Branch Prompt

## 12. Arquitectura Funcional

Usuario → Interfaz (Streamlit) → Agente → Herramientas → RAG → Base de Conocimiento → Gemini 2.5 Flash → Respuesta.

## 13. Matriz de Trazabilidad (MTR-001)

Se implementará una matriz que relacionará: Necesidad del negocio → Documento fuente → RF → CU → Tool → Prompt → Caso de prueba → Estado.

## 14. Criterios de Aceptación

- El agente responde consultas sobre todos los documentos oficiales.
- Consulta inventario y sucursales.
- Cita la fuente documental cuando corresponda.
- Indica cuando no existe información.
- Mantiene contexto básico de conversación.

## 15. Roadmap

Finalizar análisis funcional, diseñar arquitectura, implementar RAG, desarrollar herramientas, construir interfaz, ejecutar pruebas y preparar la entrega final.

