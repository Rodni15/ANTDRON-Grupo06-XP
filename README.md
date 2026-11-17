# Proyecto ANTDRON / AntCiberDron — Grupo 06 (Metodología XP)

> **Escuela Politécnica Nacional (EPN) · Facultad de Ingeniería en Informática · Metodologías Ágiles**  
> **Metodología:** Extreme Programming (XP) | **Lenguaje:** Python 3.12 | **Diagramas:** PlantUML | **Equipo:** 4 integrantes (`[PENDIENTE: Nombres y Cédulas]`) | **Metáfora:** Hormiguero Cibernético

Carpeta completa del proyecto organizada alrededor de las **4 fases y 17 pasos de XP**, incluyendo los **5 diagramas obligatorios en PlantUML**, la configuración **Python 3.12 / Docker / CI** lista y la estructura completa de paquetes Python en `src/` *(sin implementar código `.py` todavía hasta contar con las 4 cédulas)*.

---

## Equipo de 4 Integrantes y Roles XP

| Integrante | Cédula / Nombre | Roles XP Asignados | Responsabilidad Principal |
| :--- | :--- | :--- | :--- |
| **I1** | `[Cédula 1]` · `[Nombre 1]` | **Cliente (KGD)** + **Gestor (Big Boss)** | Historias de usuario, prioridad, criterios de aceptación, gestión de releases y entrega. |
| **I2** | `[Cédula 2]` · `[Nombre 2]` | **Coach XP** + **Programador 1** | Disciplina XP (TDD, CRC, Reciclaje, Metáfora) y programación en pareja (`pkAntCiberDronContract`, `IIA`, `AntCiberDron`). |
| **I3** | `[Cédula 3]` · `[Nombre 3]` | **Tracker** + **Programador 2** | Velocidad, burndown, rotaciones y programación en pareja (`SistemaRuso`, `Hormigas`, `SQLite`, menús de consola). |
| **I4** | `[Cédula 4]` · `[Nombre 4]` | **Tester** *(+ Pair Review / QA / Docker)* | Pruebas TDD (pytest), aceptación con I1, pipeline CI y verificación Docker (`-0.5` cero incidentes). |

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

## Cómo continuar cuando tengas las 4 cédulas

1. Abre [`xp-framework.html`](xp-framework.html) para recorrer visualmente las fases XP, los 5 diagramas y qué va en cada archivo.
2. Completa los datos del equipo en [`docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md`](docs-analisis/01-ROLES-EQUIPO-4-INTEGRANTES.md) y copia tu prompt desde [`PROMPT_IMPLEMENTACION.md`](PROMPT_IMPLEMENTACION.md).
3. Con el prompt se generarán automáticamente `data/Grupo06.csv`, las clases Python 3.12 dentro de `src/`, los tests TDD con `pytest` y el grafo PlantUML/gramática final del autómata en [`02-Diseno/diagramas/03-automata-grafo-gramatica.md`](02-Diseno/diagramas/03-automata-grafo-gramatica.md).
