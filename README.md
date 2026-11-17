# Proyecto ANTDRON / AntCiberDron — Grupo 06 (Metodología XP)

> **Escuela Politécnica Nacional (EPN) · Facultad de Ingeniería en Informática · Metodologías Ágiles**  
> **Metodología:** Extreme Programming (XP) | **Lenguaje:** Python 3.12 | **Diagramas:** PlantUML | **Equipo:** 4 integrantes (`Analy Yepez`, `Ronny Veloz`, `Oscar Tamayo`, `Mateo Yaguari`) | **Metáfora:** Hormiguero Cibernético

Carpeta completa del proyecto organizada alrededor de las **4 fases y 17 pasos de XP**, incluyendo los **5 diagramas obligatorios en PlantUML**, la configuración **Python 3.12 / Docker / CI** lista y la estructura completa de paquetes Python en `src/` *(lista para que cada integrante desarrolle su parte)*.

---

## Equipo de 4 Integrantes, Roles XP y Repartición por Partes

| Integrante | Cédula · Nombre | Roles XP Asignados | Parte Asignada y Responsabilidad Principal |
| :--- | :--- | :--- | :--- |
| **I1** | `1721396412` · **Analy Yepez** *(último dígito `2`)* | **Cliente (KGD)** + **Gestor (Big Boss)** | **Parte 1 — Login, equipo y CSV:** Login (máx. 3 intentos), presentación del equipo, `Grupo06.csv` con loading animado, **Diagrama de Casos de Uso** y criterios de aceptación. |
| **I2** | `1724490055` · **Ronny Veloz** *(último dígito `5`)* | **Coach XP** + **Programador 1** | **Parte 2 — Autómata y documento:** `BombaAutomata` (`ab* ∪ abc ∪ abcdt+`), Bomba e impresión de coordenadas a destruir, **Grafo y Gramática del Autómata**, portada/roles y documento final. |
| **I3** | `1722578703` · **Oscar Tamayo** *(último dígito `3`)* | **Tracker** + **Programador 2** | **Parte 3 — Hormigas y `AntCiberDron`:** Jerarquía `Hormiga`/`HLarva`/`Alimento`, `IIA`, `AntCiberDron` (armas, turbo, fuente, idiomas), SQLite, **Diagrama de Clases**, **MER** y métricas XP. |
| **I4** | `1726389099` · **Mateo Yaguari** *(último dígito `9`)* | **Tester** *(QA / CI / Docker)* | **Parte 4 — Pantallas y Docker:** Pantallas de consola del Hormiguero Virtual (`ant.ui`), flujo en `main.py`, pruebas `pytest`, Dockerización, CI, **Diagrama de Arquitectura** y `-0.5` cero incidentes. |

> El docente (`patmic`) actúa como evaluador final y usuario administrativo (`patmic` / `123`). Ver detalle completo en [`docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md`](docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md).

---

## Estructura Completa del Proyecto (`ANTDRON-Grupo06-XP/`)

```text
ANTDRON-Grupo06-XP/
├── README.md                                  # Guía principal del proyecto
├── xp-framework.html                          # Visualizador interactivo del Framework XP + 5 Diagramas + Tarjetas HU
├── PROMPT_IMPLEMENTACION.md                   # Prompt maestro para generar src/ y Grupo06.csv con las 4 cédulas
├── .gitignore                                 # Exclusiones Python (__pycache__), SQLite (*.db) e IDE
├── requirements.txt                           # Dependencias Python 3.12 (pytest; sqlite3 viene incluido)
├── pytest.ini                                 # Configuración de pytest (testpaths y pythonpath)
├── main.py                                    # Punto de entrada (modo consola)
├── Dockerfile                                 # Imagen python:3.12-slim (consola interactiva TTY)
├── docker-compose.yml                         # Servicio antdron con stdin_open, tty y volumen ./data
├── .github/workflows/ci.yml                   # Pipeline GitHub Actions (pytest + docker build)
├── docs-analisis/
│   ├── 00-BRECHAS-PDF-VS-MD.md                # Todo lo extraído del PDF original que faltaba o difería en el .md
│   └── 01-ROLES-EQUIPO-4-INTEGRANTES.md       # Distribución de los 7 roles XP entre 4 integrantes + reuniones
├── 01-Planificacion/                          # FASE I XP (Pasos 1–6)
│   ├── README.md
│   ├── 01-historias-usuario/TARJETAS_HISTORIAS_USUARIO.md
│   ├── 02-plan-entregas/PLAN_DE_ENTREGAS.md
│   ├── 03-velocidad-proyecto/VELOCIDAD_Y_METRICAS.md
│   ├── 04-iteraciones/PLAN_ITERACIONES.md
│   ├── 05-rotaciones/TABLA_ROTACIONES.md
│   └── 06-reuniones/ACTAS_REUNIONES.md
├── 02-Diseno/                                 # FASE II XP (Pasos 7–11 + Los 5 Diagramas Obligatorios)
│   ├── README.md
│   ├── 01-metafora-sistema/METAFORA_DEL_SISTEMA.md
│   ├── 02-tarjetas-crc/TARJETAS_CRC.md        # Paso XP II.2 (técnica de diseño, no diagrama obligatorio)
│   ├── 03-soluciones-puntuales/SPIKES_TECNICOS.md
│   ├── 04-funcionalidad-minima/MVP_RELEASE_1.md
│   ├── 05-reciclaje/BITACORA_REFACTORIZACION.md
│   └── diagramas/                             # ÚNICAMENTE los 5 diagramas obligatorios del PDF (en PlantUML):
│       ├── 01-diagrama-clases.md
│       ├── 02-diagrama-casos-de-uso.md
│       ├── 03-automata-grafo-gramatica.md
│       ├── 04-modelo-entidad-relacion.md
│       └── 05-arquitectura-aplicacion.md
├── 03-Desarrollo/                             # FASE III XP (Pasos 12–15)
│   ├── README.md
│   ├── 01-disponibilidad-cliente/CONSULTAS_Y_DECISIONES_CLIENTE.md
│   ├── 02-unidad-pruebas-tdd/MATRIZ_CASOS_TDD.md
│   ├── 03-programacion-parejas/BITACORA_PAIR_PROGRAMMING.md
│   └── 04-integracion-continua/ESTRATEGIA_CI_Y_RAMAS.md
├── 04-Pruebas/                                # FASE IV XP (Pasos 16–17)
│   ├── README.md
│   ├── 01-implantacion/GUIA_IMPLANTACION_DOCKER.md
│   └── 02-pruebas-aceptacion/CHECKLIST_ACEPTACION_CLIENTE.md
├── data/
│   ├── README.md                              # Guía de Grupo06.csv y SQLite antdron.db
│   └── Grupo06.csv.template                   # Plantilla oficial pendiente de las 4 cédulas
├── src/                                       # Estructura completa de paquetes Python (sin código aún)
│   ├── pkAntCiberDronContract/                # IHormiga, IIA, CoordenadaUK, Utility, SistemaRuso
│   ├── ant/
│   │   ├── hormiguero/                        # Hormiga, HLarva, HSoldado, HZangano, HRastreadora, Strategy
│   │   ├── alimento/                          # Alimento, Nectar, ACarnivoro, AOmnivoro, AHervivoro
│   │   ├── dron/                              # AntCiberDron, Pata, Metralleta, Laser, TurboReactor, Fuente, Idioma
│   │   ├── iia/                               # BombaAutomata A=(Q, Σ, δ, q0, F)
│   │   ├── ruso/                              # AuthService, Integrante, ArsenalCatalogo
│   │   ├── db/                                # SqliteConnection y DAOs del MER (sqlite3)
│   │   └── ui/                                # Menús de consola del Hormiguero Virtual
│   └── resources/                             # schema.sql y config.py
└── tests/                                     # Pruebas TDD con pytest
    ├── pkAntCiberDronContract/                # test_sistema_ruso.py, test_utility.py
    └── ant/                                   # test_hormiga.py, test_ant_ciber_dron.py, test_bomba_automata.py, test_auth_service.py, test_persistencia_sqlite.py
```

---

## Cómo continuar el desarrollo por partes

1. Abre [`xp-framework.html`](xp-framework.html) para recorrer visualmente las fases XP, los 5 diagramas en PlantUML y la repartición de cada integrante.
2. Revisa la asignación oficial de roles y entregables en [`docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md`](docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md) y el prompt maestro en [`PROMPT_IMPLEMENTACION.md`](PROMPT_IMPLEMENTACION.md).
3. Cada integrante implementa su parte (`Parte 1` Analy, `Parte 2` Ronny, `Parte 3` Oscar, `Parte 4` Mateo) en ramas `feature/...`, pasando pruebas TDD con `pytest` y validación final dentro de Docker.
