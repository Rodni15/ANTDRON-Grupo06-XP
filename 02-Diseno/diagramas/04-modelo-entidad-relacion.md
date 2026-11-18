# Grupo 06 · Modelo entidad-relación

El modelo describe las tablas SQLite implementadas por la Parte 3. La base de datos representa un hormiguero virtual y un registro de entrenamiento para el grupo. La autenticación y las coordenadas siguen usando las fuentes de la Parte 1.

![Modelo entidad-relación de la Parte 3](img/04-modelo-entidad-relacion.png)

```plantuml
@startuml
title ANTDRON · Grupo 06 · Persistencia de la Parte 3
hide circle
skinparam linetype ortho

entity HORMIGA {
  * id : INTEGER <<PK>>
  --
  * tipo : TEXT
  * sexo : TEXT
  * estado : TEXT
}

entity ALIMENTACION {
  * id : INTEGER <<PK>>
  --
  * hormiga_id : INTEGER <<FK>>
  * alimento : TEXT
  * resultado : TEXT
  * fecha : TEXT
}

entity ENTRENAMIENTO_IDIOMA {
  * id : INTEGER <<PK>>
  --
  * experto : TEXT
  * idioma : TEXT
  * area : TEXT
  * contenido : TEXT
  * fecha : TEXT
}

HORMIGA ||--o{ ALIMENTACION : registra

note right of HORMIGA
  Tipo: HLarva o HRastreadora.
  Estado: VIVA o MUERTA.
  La metamorfosis conserva el id.
end note

note right of ENTRENAMIENTO_IDIOMA
  Idioma: EN o ES.
  Experto: nombre registrado tras
  verificar su certificación en el dominio.
end note
@enduml
```
