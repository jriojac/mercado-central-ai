# MTR-001 -- Matriz de Trazabilidad

## Objetivo

Relacionar necesidades, requisitos, diseño, implementación y pruebas.

  -------------------------------------------------------------------------------------------------------------------------------------------
  ID        Necesidad      Documento         RF       CU       TL       PR       Módulo                     TST       Seguridad      Estado
  --------- -------------- ----------------- -------- -------- -------- -------- -------------------------- --------- -------------- --------
  MTR-001   Responder FAQ  FAQ               RF-002   CU-001   TL-001   PR-002   knowledge/faq_tool.py      TST-001   Solo fuente    🟡
                                                                                                                      oficial        Diseño

  MTR-002   Consultar      Política Atención RF-003   CU-002   TL-002   PR-003   tools/customer_policy.py   TST-002   Validar        🟡
            devoluciones                                                                                              contexto       Diseño

  MTR-003   Consultar      Manual            RF-005   CU-003   TL-004   PR-004   tools/supplier_tool.py     TST-003   Solo           🟡
            proveedores    Proveedores                                                                                documentos     Diseño
                                                                                                                      oficiales      

  MTR-004   Consultar      Inventario.xlsx   RF-006   CU-004   TL-003   PR-005   tools/inventory_tool.py    TST-004   Sin            🟡
            inventario                                                                                                modificación   Diseño
                                                                                                                      de datos       

  MTR-005   Consultar      Directorio        RF-007   CU-005   TL-005   PR-006   tools/branch_tool.py       TST-005   Información    🟡
            sucursales     Sucursales                                                                                 oficial        Diseño
  -------------------------------------------------------------------------------------------------------------------------------------------

## Reglas

-   Cada nueva funcionalidad debe registrarse primero en esta matriz.
-   No se implementará código sin un RF y un CU asociados.
-   Cada Tool debe tener al menos un Prompt y un Caso de Prueba.
-   Todo cambio de estado debe reflejarse en el Dashboard del proyecto.
