# Fase II: Diseño (Pasos 7 al 11 de XP)

En la **Fase de Diseño** del proyecto en **Python 3.12**, el equipo encabezado por el **Coach XP (I2)** aplica diseño simple y evolutivo: antes de escribir código complejo se acuerda una metáfora común, se modelan responsabilidades en tarjetas CRC, se validan riesgos con soluciones puntuales (spikes), se define el MVP mínimo y se mantiene el código limpio mediante reciclaje (refactorización). Además, aquí residen los **5 diagramas obligatorios en PlantUML** exigidos por el cuestionario del PDF.

## Qué se hizo en cada paso de esta fase

| Paso XP (Diagrama PDF) | Actividad Realizada en el Proyecto | Participantes Clave | Archivo de Evidencia |
| :--- | :--- | :--- | :--- |
| **7. Metáfora del Sistema** | Adopción de la metáfora **"Hormiguero Cibernético"** (`Hormiguero`, `HLarva`, `AntCiberDron`, `IIA`, `SistemaRuso`) y definición del mapa de paquetes Python (`pkAntCiberDronContract` + `ant.*`). | **I2 (Coach)** y todo el equipo. | [`01-metafora-sistema/METAFORA_DEL_SISTEMA.md`](01-metafora-sistema/METAFORA_DEL_SISTEMA.md) |
| **8. Tarjetas CRC** | Sesión de diseño objeto-orientado en Python 3.12 (`abc.ABC`, tipado `bool`/`str`/`int`) para el contrato oficial del PDF. *(Nota: artefacto de diseño XP; **no** forma parte de los 5 diagramas obligatorios).* | **I2 (Coach+Prog1)**, **I3 (Prog2)**, **I4 (Tester)**. | [`02-tarjetas-crc/TARJETAS_CRC.md`](02-tarjetas-crc/TARJETAS_CRC.md) |
| **9. Soluciones Puntuales** *(Spikes)* | Experimentos rápidos desechables en Python para validar: (1) motor AFD del autómata vs módulo `re`, (2) spinner `\ | / - |` en consola y Docker TTY, (3) consola + SQLite (`sqlite3`) en Docker/local. | **I2**, **I3** e **I4**. | [`03-soluciones-puntuales/SPIKES_TECNICOS.md`](03-soluciones-puntuales/SPIKES_TECNICOS.md) |
| **10. Funcionalidad Mínima** *(MVP)* | Definición del producto mínimo viable ejecutable en Release 1 (`HU-01, 02, 04, 05`) en Python 3.12 y dockerizable desde la semana 1. | **I1 (Cliente+Gestor)** e **I2 (Coach)**. | [`04-funcionalidad-minima/MVP_RELEASE_1.md`](04-funcionalidad-minima/MVP_RELEASE_1.md) |
| **11. Reciclaje** *(Refactorización)* | Registro de refactorizaciones aplicadas sin cambiar comportamiento externo: `if/else` $\rightarrow$ `EvolucionStrategy`, retorno `bool` en `IHormiga`, desacoplamiento de `BombaAutomata` y separación menús de consola/DAO. | **I2 (Prog1)** e **I3 (Prog2)** con pruebas de **I4**. | [`05-reciclaje/BITACORA_REFACTORIZACION.md`](05-reciclaje/BITACORA_REFACTORIZACION.md) |

---

## Los 5 Diagramas Obligatorios del Proyecto (Cuestionario PDF · Código PlantUML)

En cuanto a **diagramas obligatorios**, el enunciado exige **exclusivamente estos 5** (todos modelados en **PlantUML** dentro de [`diagramas/`](diagramas/01-diagrama-clases.md)):

| # | Diagrama Obligatorio | Archivo | Estado |
| :---: | :--- | :--- | :--- |
| **1** | **Diagrama de Clases** (`pkAntCiberDronContract` + dominio) | [`diagramas/01-diagrama-clases.md`](diagramas/01-diagrama-clases.md) | Completo |
| **2** | **Diagrama de Casos de Uso** | [`diagramas/02-diagrama-casos-de-uso.md`](diagramas/02-diagrama-casos-de-uso.md) | Completo |
| **3** | **Grafo con Gramática del Autómata** | [`diagramas/03-automata-grafo-gramatica.md`](diagramas/03-automata-grafo-gramatica.md) | Plantilla lista (completar con las 4 cédulas) |
| **4** | **Modelo Entidad-Relación (MER)** | [`diagramas/04-modelo-entidad-relacion.md`](diagramas/04-modelo-entidad-relacion.md) | Completo |
| **5** | **Diagrama de la Arquitectura de la Aplicación** | [`diagramas/05-arquitectura-aplicacion.md`](diagramas/05-arquitectura-aplicacion.md) | Completo |
