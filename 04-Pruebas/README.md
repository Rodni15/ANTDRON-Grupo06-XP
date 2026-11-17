# Fase IV: Pruebas (Pasos 16 y 17 de XP — Python 3.12)

En la **Fase de Pruebas**, el **Tester (I4)**, el **Gestor (I1)** y el **Cliente interno (I1)** validan la **implantación real en Python 3.12 y Docker** y firman las **Pruebas de Aceptación** frente a todos los requisitos del PDF original para entregar con **0 incidentes**.

## Qué se hizo en cada paso de esta fase

| Paso XP (Diagrama PDF) | Actividad Realizada en el Proyecto | Participantes Clave | Archivo de Evidencia |
| :--- | :--- | :--- | :--- |
| **16. Implantación** *(Despliegue)* | Construcción y prueba de la imagen Docker `python:3.12-slim` y `docker-compose.yml` en un equipo limpio (consola interactiva Python + SQLite). | **I4 (Tester)** + **I1 (Gestor)** + apoyo **I2/I3**. | [`01-implantacion/GUIA_IMPLANTACION_DOCKER.md`](01-implantacion/GUIA_IMPLANTACION_DOCKER.md) |
| **17. Pruebas de Aceptación** | Verificación punto por punto del checklist de aceptación (requisitos funcionales, salidas exactas de consola, 5 diagramas en PlantUML y regla `-0.5` cero incidentes). | **I1 (Cliente)** + **I4 (Tester)**. | [`02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md`](02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md) |
