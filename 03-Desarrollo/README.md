# Fase III: Desarrollo (Pasos 12 al 15 de XP — Python 3.12)

En la **Fase de Desarrollo** en **Python 3.12**, los **2 Programadores (`I2`, `I3`)** trabajan en pareja guiados por pruebas previas (**TDD** con `pytest`), con el **Cliente (`I1`)** disponible en tiempo real, el **Tester (`I4`)** automatizando `pytest` y vigilando la **Integración Continua**.

## Qué se hizo en cada paso de esta fase

| Paso XP (Diagrama PDF) | Actividad Realizada en el Proyecto | Participantes Clave | Archivo de Evidencia |
| :--- | :--- | :--- | :--- |
| **12. Disponibilidad del Cliente** | Bitácora de consultas rápidas resueltas por **I1 (Cliente interno)** y validadas con el docente (`patmic`) sobre reglas ambiguas (Grupo 6, muerte de larva, salida de consola, idiomas). | **I1 (Cliente)** responde; I2/I3/I4 consultan. | [`01-disponibilidad-cliente/CONSULTAS_Y_DECISIONES_CLIENTE.md`](01-disponibilidad-cliente/CONSULTAS_Y_DECISIONES_CLIENTE.md) |
| **13. Unidad de Pruebas** *(TDD)* | Diseño de la matriz de casos de prueba **antes** de escribir el código de producción (`Red -> Green -> Refactor`) para Login, CSV, Autómata, Hormigas, Dron e Idiomas. | **I4 (Tester)** + **I2/I3 (Programadores)**. | [`02-unidad-pruebas-tdd/MATRIZ_CASOS_TDD.md`](02-unidad-pruebas-tdd/MATRIZ_CASOS_TDD.md) |
| **14. Programación por Parejas** | Registro de sesiones Driver/Navigator entre I2 y I3 (rotación cada 30 min) y sesiones de Pair Testing / Pair Review con I4. | **I2 (Prog1)** + **I3 (Prog2)** (+ **I4** en review). | [`03-programacion-parejas/BITACORA_PAIR_PROGRAMMING.md`](03-programacion-parejas/BITACORA_PAIR_PROGRAMMING.md) |
| **15. Integración** *(Integración Continua)* | Estrategia de ramas cortas (`feature/HU-XX`), revisión obligatoria de I4 antes de merge a `main` y ejecución automática de `pytest` + `docker build`. | **I4 (Tester)** + **I1 (Gestor)**. | [`04-integracion-continua/ESTRATEGIA_CI_Y_RAMAS.md`](04-integracion-continua/ESTRATEGIA_CI_Y_RAMAS.md) |
