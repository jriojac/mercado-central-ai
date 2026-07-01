# DOC-007 -- Decision Engine

## Objetivo

Definir cómo el agente analiza una consulta, decide el flujo adecuado y
aplica controles de seguridad antes de responder.

## Explicación sencilla

Imagina a un recepcionista en un hospital. Antes de enviar a una persona
con un especialista, primero escucha el problema y decide a qué área
dirigirla. El Decision Engine hace exactamente eso con cada pregunta.

## Responsabilidades

-   Analizar la intención.
-   Detectar consultas fuera del alcance.
-   Seleccionar la Tool adecuada.
-   Decidir si consultar el RAG.
-   Aplicar reglas de seguridad.
-   Enviar la solicitud al siguiente componente.

## Flujo lógico

Usuario → Analizar intención → ¿Consulta válida? → Seleccionar Tool o
RAG → Construir contexto → Gemini → Respuesta.

## Tipos de intención

Saludos, FAQ, Inventario, Sucursales, Proveedores, Reglamento,
Devoluciones, Conversación general, Consulta fuera de alcance.

## Reglas de decisión

1.  Si existe una Tool especializada, utilizarla.
2.  Si requiere conocimiento documental, consultar el AI Knowledge
    Platform.
3.  Si la pregunta está fuera del alcance, responder que no existe
    información oficial.
4.  Nunca ignorar las instrucciones del sistema.

## Seguridad

-   Mitigar Prompt Injection.
-   No ejecutar instrucciones del usuario.
-   No revelar prompts internos.
-   Responder únicamente con información autorizada.
-   Manejo seguro de errores.

## Relación con otros módulos

Entrada: Conversation Engine. Salida: AI Knowledge Platform, Tool Layer
o Gemini Adapter.

## Archivos Python previstos

src/core/decision_engine.py src/core/intent_classifier.py
src/core/router.py

## Casos de prueba

TST-010 Selección correcta de Tool. TST-011 Rechazo de Prompt Injection.
TST-012 Consulta fuera del alcance. TST-013 Enrutamiento hacia RAG.

## Checklist

□ Clasificador de intención □ Router □ Validaciones □ Seguridad □
Integración □ Pruebas
