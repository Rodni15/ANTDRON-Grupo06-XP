# 4. Plan de Iteraciones

**Responsable:** I3 (Tracker) — Analy Yépez · **Revisa:** I1 (Cliente + Gestor) — Ronny Veloz.

Por la fecha de entrega (jueves 19/11/2026), el proyecto se ejecuta en **3 iteraciones cortas**. Al final de cada una existe código ejecutable y probado que el Cliente (I1) puede revisar.

| Iteración | Fecha | Historias | Puntos | Responsables | Meta |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | Mar 17/11 | `HU-01` (3), `HU-02` (5) | **8** | Analy | Login con 3 intentos, presentación del equipo y lectura de `Grupo06.csv` con loading. Repositorio y datos reales del equipo. |
| **2** | Mié 18/11 (hasta 20:00) | `HU-03` (5), `HU-04` (3), `HU-05` (5), `HU-06` (5), `HU-07` (3), `HU-08` (5) | **26** | Ronny (HU-03) · Óscar (HU-04 a HU-08) | Autómata de la bomba y coordenadas a destruir; jerarquía de hormigas; AntCiberDron completo. |
| **3** | Mié 18/11 noche – Jue 19/11 | `HU-09` (8), `HU-10` (5), `HU-11` (5) | **18** | Mateo (HU-09, HU-10) · Todos (HU-11) | Menú del Hormiguero, integración en `main.py`, Docker probado sin fallos y los 5 diagramas. |

**Total:** 52 puntos.

## Iteración 1 — Login, equipo y CSV (`8 pts`)
- **Historias:** `HU-01`, `HU-02`.
- **Entregable:** `python main.py` autentica, muestra `[+] TEAM [6]` y lee el CSV con animación; 13 pruebas pytest en verde.
- **Documentación:** diagrama de casos de uso.

## Iteración 2 — Autómata, hormigas y AntCiberDron (`26 pts`)
- **Historias:** `HU-03` a `HU-08`.
- **Entregable:** `BombaAutomata` reconoce $L = \{abc,\ ab^*,\ abcdt^+\}$; `AntCiberDron.buscar()` decide la detonación; larvas, transformación, armas, fuente de poder e idiomas con pruebas pytest.
- **Documentación:** grafo y gramática del autómata, diagrama de clases y entidad-relación.
- **Riesgo:** es la iteración con más carga (26 pts, 21 en una sola persona). El Tracker revisa el avance a media tarde del miércoles para redistribuir si hace falta.

## Iteración 3 — Hormiguero, Docker y cierre (`18 pts`)
- **Historias:** `HU-09`, `HU-10`, `HU-11`.
- **Entregable:** aplicación completa en consola dentro de Docker, sin errores.
- **Documentación:** diagrama de arquitectura, portada, checklist de aceptación y documento final.
