# 1. Tarjetas de Historias de Usuario (Story Cards)

> **Stack de implementación:** **Python 3.12** (POO estricta con `abc.ABC`, interfaz web `Flask`, consola alternativa, `sqlite3`, `pytest` y Docker) · **Diagramas:** **PlantUML**.  
> **Repartición por Partes:** **Parte 1 (`HU-01`, `HU-02`):** Analy Yepez (`I3`) · **Parte 2 (`HU-03`, `HU-11`):** Ronny Veloz (`I1`) · **Parte 3 (`HU-04`..`HU-08`):** Oscar Tamayo (`I2`) · **Parte 4 (`HU-09`, `HU-10`):** Mateo Yaguari (`I4`).  
> En XP, cada historia se escribe en una tarjeta simple y comprensible para el Cliente (**I1 · Ronny Veloz**).  
> **Anverso:** Identificador, Título, Prioridad, Puntos, Iteración y narrativa simple (*Como... quiero... para...*).  
> **Reverso:** Criterios de aceptación verificables por el Tester (**I4 · Mateo Yaguari**) y aprobados por el Cliente (**I1 · Ronny Veloz**).  
> **Escala de estimación:** Fibonacci (`1, 2, 3, 5, 8`). **1 punto ≈ 2–3 horas** de trabajo de la pareja (`I2 + I3`). Total: **52 puntos**.

---

## Tarjeta `HU-01`: Inicio de Sesión Seguro
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-01` · **Iteración:** 1 (`R1`) · **Parte 1 (Analy Yépez)**<br>**Prioridad:** Alta · **Estimación:** `3 pts`<br><br>**Como** usuario de la KGD o docente evaluador,<br>**quiero** iniciar sesión con usuario y clave con un límite de 3 intentos,<br>**para** proteger el acceso al sistema ANTDRON. | - [x] Acepta credenciales de los **4 integrantes** del grupo (`data/integrantes.json`) y del usuario **`patmic` / `123`**.<br>- [x] Permite hasta **3 intentos**; ante credencial inválida muestra aviso claro (`AuthService` y `web_app.py`).<br>- [x] Al **3.er fallo consecutivo**, cierra/bloquea el acceso de forma controlada sin errores.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-02`: Datos del Equipo y Lectura Animada de `Grupo06.csv`
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-02` · **Iteración:** 1 (`R1`) · **Parte 1 (Analy Yépez)**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** usuario autorizado,<br>**quiero** ver los datos del grupo y cargar las coordenadas ucranianas desde `Grupo06.csv` con un indicador animado,<br>**para** verificar qué objetivos y horarios fueron desencriptados. | - [x] Imprime `[+] TEAM [6]: Hormiguero Cibernético` y la lista `Cédula \| Nombre` de los **4 integrantes** (y panel web).<br>- [x] Lee las 40 filas de `data/Grupo06.csv` (con `SistemaRuso.readCoord(...)` devolviendo `list[CoordenadaUK]`).<br>- [x] Por cada línea leída anima `\ \| / - \|` hasta **`100%`** usando `Utility` (consola) y `app.js` (web) antes de mostrar el resultado.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-03`: Bomba Inteligente con Autómata (`IIA.buscar`)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-03` · **Iteración:** 2 (`R2`) · **Parte 2 (Ronny Veloz)**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** operador de la KGD,<br>**quiero** que el `AntCiberDron` analice cada tipo de arsenal usando un autómata construido con nuestras cédulas (`{2, 5, 3, 9}`),<br>**para** detonar únicamente en las coordenadas objetivo autorizadas. | - [x] El autómata reconoce la unión de los lenguajes asociados al **último dígito de las 4 cédulas (`{2, 5, 3, 9}` $\rightarrow L = \{ab^*, abc, abcdt^+\}$)**.<br>- [x] `AntCiberDron` implementa `IIA` (`abc.ABC`) en Python y su método `buscar(tipoArsenal: str) -> bool` retorna `True` o `False` según `Bomba` / `BombaAutomata` (sin depender de `re` en producción, validado por tabla de transición $\delta$).<br>- [x] Imprime/presenta la tabla `COORDENADAS UCRANIANAS A DESTRUIR: Geoposición \| Tipo Arsenal \| Acción` solo para las 29 detonaciones (`true`).<br>**Valida:** I3 (Analy) & I4 (Mateo) |

---

## Tarjeta `HU-04`: Nacimiento como `HLarva` y Supervivencia con Néctar
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-04` · **Iteración:** 2 (`R2`) · **Parte 3 (Óscar Tamayo)**<br>**Prioridad:** Alta · **Estimación:** `3 pts`<br><br>**Como** encargado del hormiguero,<br>**quiero** crear nuevas hormigas que nazcan siempre como `HLarva` y vivan comiendo `Néctar`,<br>**para** iniciar su ciclo de vida biológico dentro del sistema. | - [x] Toda hormiga nueva se instancia como `HLarva` (subclase de `Hormiga` con `Id: int`, `sexo: str`, `estado: str`).<br>- [x] Al ejecutar `comer(Nectar())` devuelve `True` y mantiene su estado `"VIVA"`.<br>- [x] `Hormiga` implementa `IHormiga.comer(alimento: Alimento) -> bool` en Python.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-05`: Metamorfosis y Supervivencia por Tipo de Alimento
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-05` · **Iteración:** 2 (`R2`) · **Parte 3 (Óscar Tamayo)**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** encargado del hormiguero,<br>**quiero** que una larva se transforme en su tipo de hormiga al recibir su alimento correspondiente y muera si recibe otro,<br>**para** obtener hormigas especializadas y cumplir la regla biológica. | - [x] Al alimentar una larva viva con `AHervivoro()`, `Hormiguero` la sustituye por una `HRastreadora`, conserva su identificador (`Id`) y devuelve `True`.<br>- [x] La rastreadora sigue viva con alimento herbívoro (`AHervivoro`). Con néctar u otro alimento pasa a estado `"MUERTA"` y no puede revivir.<br>- [x] Si una larva o hormiga adulta recibe un alimento incorrecto, cambia su estado a `"MUERTA"` y retorna `False`.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-06`: Ensamblaje del `AntCiberDron` (Extremidades, Armas y Turbo)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-06` · **Iteración:** 2 (`R2`) · **Parte 3 (Óscar Tamayo)**<br>**Prioridad:** Media · **Estimación:** `5 pts`<br><br>**Como** ingeniero de la KGD,<br>**quiero** armar el `AntCiberDron` con extremidades de hormiga, metralleta, láser y turbo reactor,<br>**para** consultar el estado de sus componentes y simular el vuelo con la energía disponible. | - [x] Modela extremidades de hormiga (`6 patas` tipo `Pata`, `cabeza`, `torax`, `abdomen`).<br>- [x] Pata **delantera derecha** equipa `Metralleta`; pata **delantera izquierda** equipa `Laser` cuya potencia varía según la energía de `FuenteDePoder`.<br>- [x] Espalda equipa `TurboReactor` que permite `volar()` consumiendo 1 unidad de energía de la fuente.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-07`: Recarga y Reemplazo de la Fuente de Poder con `IIA`
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-07` · **Iteración:** 2 (`R2`) · **Parte 3 (Óscar Tamayo)**<br>**Prioridad:** Media · **Estimación:** `3 pts`<br><br>**Como** operador del dron,<br>**quiero** recargar o reemplazar la fuente de poder bajo asistencia de `IIA`,<br>**para** recuperar la potencia del láser y la capacidad de vuelo del dron. | - [x] `AntCiberDron(IIA)` implementa `asistirRecargaFuente()` (recupera capacidad inicial) y `asistirReemplazoFuente(nueva)` (instala nueva fuente operativa).<br>- [x] Al cambiar el nivel de energía de la fuente, la potencia reportada por `dispararLaser()` varía en igual proporción.<br>- [x] Con fuente agotada (`0`), `dispararLaser()` devuelve `0` y `volar()` retorna `False`.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-08`: Aprendizaje de Idiomas Exclusivo por Expertos Parlantes
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-08` · **Iteración:** 2 (`R2`) · **Parte 3 (Óscar Tamayo)**<br>**Prioridad:** Media · **Estimación:** `5 pts`<br><br>**Como** estratega de la KGD,<br>**quiero** que el `AntCiberDron` aprenda inglés y español únicamente mediante expertos parlantes,<br>**para** garantizar que el léxico, gramática y fonética sean confiables. | - [x] Soporta entrenamiento de **léxico, gramática y fonética** en **Inglés (EN)** y **Español (ES)** (`Idioma`, `Area` en `modulo_idioma.py`).<br>- [x] `ModuloIdioma.entrenar(...)` exige un `ExpertoParlante` certificado del idioma correspondiente; rechaza fuentes no certificadas o de otro idioma.<br>- [x] Los entrenamientos quedan registrados para consulta en la interfaz web (`dashboard.html`) y persistencia SQLite (`entrenamiento_idioma`).<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-09`: Hormiguero Virtual (Interfaz Web Flask + SQLite)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-09` · **Iteración:** 3 (`R3`) · **Parte 4 (Mateo Yaguari)**<br>**Prioridad:** Alta · **Estimación:** `8 pts`<br><br>**Como** usuario de la KGD,<br>**quiero** pantallas web (Flask) para gestionar el hormiguero virtual, crear/alimentar hormigas, operar el dron y ver coordenadas destruidas,<br>**para** operar todo el sistema de manera sencilla. | - [x] Permite crear hormigas (`HLarva`), seleccionar alimento y ver su evolución o muerte en tiempo real (`web_app.py` + `dashboard.html`).<br>- [x] Muestra `Grupo06.csv` (40 filas con resultado individual), tabla separada con las 29 coordenadas destruidas (`true`), controles de `AntCiberDron` y entrenamiento de idiomas.<br>- [x] Persiste hormigas, alimentaciones y entrenamientos en **SQLite** (`sqlite_connection.py`) y mantiene `main.py` como consola alternativa.<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-10`: Despliegue Dockerizado y Cero Incidentes
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-10` · **Iteración:** 3 (`R3`) · **Parte 4 (Mateo Yaguari)**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** usuario y evaluador,<br>**quiero** ejecutar la aplicación web mediante Docker y `docker compose` sin configurar dependencias manuales,<br>**para** asegurar portabilidad total y evitar fallos en la entrega (`-0.5`). | - [x] `Dockerfile` (`python:3.12-slim`, puerto `5000`, `CMD ["python", "web_app.py"]`) y `docker-compose.yml` (puerto `5000:5000`, volumen `./data:/app/data`) configurados y verificados.<br>- [x] La interfaz web (`http://localhost:5000`) ejecuta la evaluación por fila y animación progresiva de carga sin errores ni crashes.<br>- [x] Suite de pruebas automatizadas en verde (**68 casos** verificados) y workflow CI listo (`.github/workflows/ci.yml`). *(Nota: la ejecución física de `docker compose up` queda pendiente de entorno con Docker Desktop operativo).*<br>**Valida:** I1 (Ronny) & I4 (Mateo) |

---

## Tarjeta `HU-11`: Los 5 Diagramas Obligatorios y Bitácoras XP
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-11` · **Iteración:** 3 (`R3`) · **Parte 2 (Ronny Veloz) + Equipo**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** equipo del Proyecto 6,<br>**quiero** entregar los 5 diagramas obligatorios del cuestionario en código PlantUML, los registros XP y el documento final consolidado,<br>**para** documentar la arquitectura y aprobar la evaluación sin observaciones. | - [x] Entregados en **código PlantUML** únicamente los **5 diagramas obligatorios del PDF**:<br>  1. Diagrama de Clases (`01-diagrama-clases.md` + `img/01-diagrama-clases.png`)<br>  2. Diagrama de Casos de Uso (`02-diagrama-casos-de-uso.md` + `img/02-casos-de-uso.png`)<br>  3. Grafo con Gramática del Autómata (`03-automata-grafo-gramatica.md` + `img/03-automata.puml`)<br>  4. Modelo Entidad-Relación (`04-modelo-entidad-relacion.md` + `img/04-modelo-entidad-relacion.png`)<br>  5. Diagrama de la Arquitectura de la Aplicación (`05-arquitectura-aplicacion.md`)<br>- [x] Actualizadas las bitácoras XP, documento final ([DOCUMENTO_FINAL_GRUPO06.md](../../docs-analisis/DOCUMENTO_FINAL_GRUPO06.md)) y checklist firmado por I1 (Ronny) e I4 (Mateo).<br>**Valida:** I1 (Ronny) & I4 (Mateo) |
