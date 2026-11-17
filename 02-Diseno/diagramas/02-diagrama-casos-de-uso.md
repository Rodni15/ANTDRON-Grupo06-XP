# Diagrama Obligatorio 2: Diagrama de Casos de Uso (Python 3.12 · PlantUML)

> **Responsable (Parte 1):** **Analy Yepez (`I1`)**  
> **Brecha resuelta:** Este diagrama era obligatorio en el cuestionario del PDF pero no había sido incluido en `WORKSHOP-XP.md`. Implementado sobre consola interactiva y persistencia SQLite en **Python 3.12**.

```plantuml
@startuml
title Diagrama de Casos de Uso — ANTDRON / Hormiguero Virtual (Python 3.12)
left to right direction
skinparam packageStyle rectangle

actor "Usuario KGD / Docente (patmic)" as U
actor "Experto Parlante (EN / ES)" as E
actor "Sistema AntCiberDron / IIA" as D

rectangle "Sistema ANTDRON / Hormiguero Virtual (Python 3.12)" {
  usecase "UC-01: Autenticarse\n(máx. 3 intentos)" as UC1
  usecase "UC-02: Visualizar equipo y leer\nGrupo06.csv con loading" as UC2
  usecase "UC-03: Buscar y detonar\ncoordenadas con Autómata (IIA)" as UC3
  usecase "UC-04: Crear hormiga\n(nace como HLarva)" as UC4
  usecase "UC-05: Alimentar hormiga\n(vivir / evolucionar / morir)" as UC5
  usecase "UC-06: Operar AntCiberDron\n(volar, metralleta, láser)" as UC6
  usecase "UC-07: Recargar / Reemplazar\nfuente de poder asistida por IIA" as UC7
  usecase "UC-08: Entrenar léxico, gramática\ny fonética (EN/ES)" as UC8
  usecase "UC-09: Consultar coordenadas\ndestruidas y reportes en consola" as UC9
}

U --> UC1
U --> UC2
U --> UC3
U --> UC4
U --> UC5
U --> UC6
U --> UC7
U --> UC9

E --> UC8

D --> UC3
D --> UC7

UC3 ..> UC2 : <<include>>
UC5 ..> UC4 : <<extend>>
@enduml
```

## Especificación Resumida de Actores
- **Usuario KGD / Docente (`patmic`):** Inicia sesión en la consola Python, carga el archivo ucraniano `Grupo06.csv`, opera el Hormiguero Virtual (crea/alimenta hormigas), consulta objetivos destruidos y controla el dron.
- **Experto Parlante (Inglés / Español):** Único actor autorizado (`ExpertoParlante`) para proveer datos de entrenamiento en léxico, gramática y fonética.
- **AntCiberDron / IIA:** Evalúa el autómata en Python (`BombaAutomata`) para decidir detonación y asiste en la recarga o reemplazo de la fuente de poder.
