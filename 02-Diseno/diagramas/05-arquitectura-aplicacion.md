# Diagrama Obligatorio 5: Arquitectura de la Aplicación (Python 3.12 · PlantUML)

![05-arquitectura-aplicacion](img/05-arquitectura-aplicacion.png)

> **Responsable (Parte 4):** **Mateo Yaguari (`I4`)**  
> **Brecha resuelta:** La Parte 4 incorpora una interfaz Flask que reutiliza los contratos y servicios del dominio. La consola `main.py` se conserva como alternativa.

```plantuml
@startuml
!pragma layout smetana
title Arquitectura de la Aplicación — ANTDRON / AntCiberDron (Python 3.12)
skinparam packageStyle rectangle
top to bottom direction

package "Capa de Presentación (Python 3.12)" {
  component "Flask web_app.py\nLogin · Panel · Sesión" as WEB
  component "Plantillas HTML5 + CSS3\nDiseño responsive" as TEMPLATES
  component "Consola alternativa\npython main.py" as CLI
}

package "Contratos Oficiales (pkAntCiberDronContract · abc.ABC)" {
  component "IHormiga\n+comer(a: Alimento) -> bool" as IH
  component "IIA\n+buscar(tipoArsenal: str) -> bool" as IIA
  component "SistemaRuso\n+readCoord(fileName: str) -> list[CoordenadaUK]" as SR
  component "Utility & CoordenadaUK" as UT
}

package "Capa de Dominio (ant.* · Python 3.12)" {
  component "ant.hormiguero\nHormiga, HLarva, HSoldado, HZangano, HRastreadora" as HOR
  component "ant.alimento\nAlimento, Nectar, ACarnivoro, AOmnivoro, AHervivoro" as ALI
  component "ant.dron\nAntCiberDron, Extremidades, Laser, Metralleta, TurboReactor, FuenteDePoder, ModuloIdioma" as DRON
  component "ant.iia\nBombaAutomata A=(Q, Σ, δ, q0, F)" as AFD
}

package "Capa de Datos y Persistencia" {
  database "data/Grupo06.csv\n(Entrada desencriptada)" as CSV
  database "SQLite ./data/antdron.db\n(SqliteConnection · sqlite3)" as DB
}

package "Empaquetado, Calidad y Despliegue" {
  component "pytest (TDD & Aceptación)" as PYTEST
  component "GitHub Actions (pytest + docker build)" as CI
  component "Docker python:3.12-slim + docker-compose.yml" as DOCKER
}

WEB --> TEMPLATES
WEB --> SR
WEB --> HOR
WEB --> DRON
CLI --> SR
WEB --> DB
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
