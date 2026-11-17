# Diagrama Obligatorio 5: Arquitectura de la Aplicación (Python 3.12 · PlantUML)

> **Responsable (Parte 4):** **Mateo Yaguari (`I4`)**  
> **Brecha resuelta:** Este diagrama era obligatorio en el cuestionario del PDF pero estaba ausente en `WORKSHOP-XP.md`. Arquitectura por capas desacopladas implementada en **Python 3.12**.

```plantuml
@startuml
title Arquitectura de la Aplicación — ANTDRON / AntCiberDron (Python 3.12)
skinparam packageStyle rectangle
top to bottom direction

package "Capa de Presentación (Python 3.12)" {
  [Consola Interactiva (python main.py)\nLogin · Team · Loading Utility · Destrucción] as CLI
  [Menús de consola (ant.ui)\nHormiguero Virtual · Crear/Alimentar · Dron · Reportes] as CONSOLE_UI
}

package "Contratos Oficiales (pkAntCiberDronContract · abc.ABC)" {
  [IHormiga\n+comer(a: Alimento) -> bool] as IH
  [IIA\n+buscar(tipoArsenal: str) -> bool] as IIA
  [SistemaRuso\n+readCoord(fileName: str) -> list[CoordenadaUK]] as SR
  [Utility & CoordenadaUK] as UT
}

package "Capa de Dominio (ant.* · Python 3.12)" {
  [ant.hormiguero\nHormiga, HLarva, HSoldado, HZangano, HRastreadora, EvolucionStrategy] as HOR
  [ant.alimento\nAlimento, Nectar, ACarnivoro, AOmnivoro, AHervivoro] as ALI
  [ant.dron\nAntCiberDron, Extremidades, Laser, Metralleta, TurboReactor, FuenteDePoder, ModuloIdioma] as DRON
  [ant.iia\nBombaAutomata A=(Q, Σ, δ, q0, F)] as AFD
}

package "Capa de Datos y Persistencia" {
  database "data/Grupo06.csv\n(Entrada desencriptada)" as CSV
  database "SQLite ./data/antdron.db\n(ant.db DAOs · sqlite3)" as DB
}

package "Empaquetado, Calidad y Despliegue" {
  [pytest (TDD & Aceptación)] as PYTEST
  [GitHub Actions (pytest + docker build)] as CI
  [Docker python:3.12-slim + docker-compose.yml] as DOCKER
}

CLI --> SR
CONSOLE_UI --> HOR
CONSOLE_UI --> DRON
CONSOLE_UI --> DB
SR --> CSV
SR --> UT
SR --> DRON
HOR ..> IH : <<implements>>
HOR --> ALI
DRON ..> IIA : <<implements>>
DRON --> AFD
HOR --> DB
DRON --> DB
PYTEST --> HOR
PYTEST --> DRON
PYTEST --> AFD
CI --> PYTEST
CI --> DOCKER
@enduml
```
