# 1. Tarjetas de Historias de Usuario (Story Cards)

> **Stack de implementación:** **Python 3.12** (POO estricta con `abc.ABC`, consola interactiva, `sqlite3`, `pytest` y Docker) · **Diagramas:** **PlantUML**.  
> **Repartición por Partes:** **Parte 1 (`HU-01`, `HU-02`):** Analy Yepez (`I1`) · **Parte 2 (`HU-03`, `HU-11`):** Ronny Veloz (`I2`) · **Parte 3 (`HU-04`..`HU-08`):** Oscar Tamayo (`I3`) · **Parte 4 (`HU-09`, `HU-10`):** Mateo Yaguari (`I4`).  
> En XP, cada historia se escribe en una tarjeta simple y comprensible para el Cliente (**I1 · Analy Yepez**).  
> **Anverso:** Identificador, Título, Prioridad, Puntos, Iteración y narrativa simple (*Como... quiero... para...*).  
> **Reverso:** Criterios de aceptación verificables por el Tester (**I4**) y aprobados por el Cliente (**I1**).  
> **Escala de estimación:** Fibonacci (`1, 2, 3, 5, 8`). **1 punto ≈ 2–3 horas** de trabajo de la pareja (`I2 + I3`). Total: **52 puntos**.

---

## Tarjeta `HU-01`: Inicio de Sesión Seguro
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-01` · **Iteración:** 1 (`R1`)<br>**Prioridad:** Alta · **Estimación:** `3 pts`<br><br>**Como** usuario de la KGD o docente evaluador,<br>**quiero** iniciar sesión con usuario y clave con un límite de 3 intentos,<br>**para** proteger el acceso al sistema ANTDRON. | - [ ] Acepta credenciales de los **4 integrantes** del grupo y del usuario **`patmic` / `123`**.<br>- [ ] Permite hasta **3 intentos**; ante credencial inválida muestra aviso claro.<br>- [ ] Al **3.er fallo consecutivo**, cierra el sistema de forma controlada sin errores.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-02`: Datos del Equipo y Lectura Animada de `Grupo06.csv`
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-02` · **Iteración:** 1 (`R1`)<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** usuario autorizado,<br>**quiero** ver los datos del grupo y cargar las coordenadas ucranianas desde `Grupo06.csv` con un indicador animado,<br>**para** verificar qué objetivos y horarios fueron desencriptados. | - [ ] Imprime `[+] TEAM [6]: <Metáfora>` y la lista `Cédula \| Nombre` de los **4 integrantes**.<br>- [ ] Lee `data/Grupo06.csv` (con `SistemaRuso.readCoord(...)` devolviendo `list[CoordenadaUK]`).<br>- [ ] Por cada línea leída anima `\ \| / - \|` hasta **`100%`** usando `Utility` antes de mostrar la fila con el formato exacto de tabla del PDF.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-03`: Bomba Inteligente con Autómata (`IIA.buscar`)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-03` · **Iteración:** 2 (`R2`) · **Parte 2 (Ronny Veloz)**<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** operador de la KGD,<br>**quiero** que el `AntCiberDron` analice cada tipo de arsenal usando un autómata construido con nuestras cédulas (`{2, 5, 3, 9}`),<br>**para** detonar únicamente en las coordenadas objetivo autorizadas. | - [ ] El autómata reconoce la unión de los lenguajes asociados al **último dígito de las 4 cédulas (`{2, 5, 3, 9}` $\rightarrow L = \{ab^*, abc, abcdt^+\}$)**.<br>- [ ] `AntCiberDron` implementa `IIA` (`abc.ABC`) en Python y su método `buscar(tipoArsenal: str) -> bool` retorna `True` o `False` según el autómata (sin depender de `re` en producción, validado por tablas/estados $\delta$).<br>- [ ] Imprime la tabla `COORDENADAS UCRANIANAS A DESTRUIR: Geoposición \| Tipo Arsenal \| Acción` solo para las detonaciones (`true`).<br>**Valida:** I1 (Analy) & I4 (Mateo) |

---

## Tarjeta `HU-04`: Nacimiento como `HLarva` y Supervivencia con Néctar
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-04` · **Iteración:** 1 (`R1`)<br>**Prioridad:** Alta · **Estimación:** `3 pts`<br><br>**Como** encargado del hormiguero,<br>**quiero** crear nuevas hormigas que nazcan siempre como `HLarva` y vivan comiendo `Néctar`,<br>**para** iniciar su ciclo de vida biológico dentro del sistema. | - [ ] Toda hormiga nueva se instancia como `HLarva` (subclase de `Hormiga` con `Id: int`, `sexo: str`, `estado: str`).<br>- [ ] Al ejecutar `comer(Nectar())` devuelve `True` y mantiene su estado `"VIVA"`.<br>- [ ] `Hormiga` implementa `IHormiga.comer(a: Alimento) -> bool` en Python.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-05`: Metamorfosis y Supervivencia por Tipo de Alimento
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-05` · **Iteración:** 1 (`R1`)<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** encargado del hormiguero,<br>**quiero** que una larva se transforme en su tipo de hormiga al recibir su alimento correspondiente y muera si recibe otro,<br>**para** obtener hormigas especializadas y cumplir la regla biológica. | - [ ] Al comer el alimento de evolución configurado (estrategia por defecto del Grupo 6: `AHervivoro` $\rightarrow$ `HRastreadora`, parametrizable), la larva evoluciona y retorna `True`.<br>- [ ] La hormiga evolucionada solo sigue viva si come su alimento asignado (`ACarnivoro`/`AOmnivoro`/`AHervivoro`).<br>- [ ] Si una larva o hormiga adulta recibe un alimento incorrecto, cambia su estado a `"MUERTA"` y retorna `False`.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-06`: Ensamblaje del `AntCiberDron` (Extremidades, Armas y Turbo)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-06` · **Iteración:** 2 (`R2`)<br>**Prioridad:** Media · **Estimación:** `5 pts`<br><br>**Como** ingeniero de la KGD,<br>**quiero** armar el `AntCiberDron` con extremidades de hormiga, metralleta, láser y turbo reactor,<br>**para** que pueda volar y ejecutar ataques tierra-aire. | - [ ] Modela extremidades de hormiga (`6 patas`, cabeza/antenas, tórax, abdomen).<br>- [ ] Pata **delantera derecha** equipa `Metralleta`; pata **delantera izquierda** equipa `Laser` cuya potencia varía según la energía de la `FuenteDePoder`.<br>- [ ] Espalda equipa `TurboReactor` que permite `volar()` consumiendo energía de la fuente.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-07`: Recarga y Reemplazo de la Fuente de Poder con `IIA`
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-07` · **Iteración:** 2 (`R2`)<br>**Prioridad:** Media · **Estimación:** `3 pts`<br><br>**Como** operador del dron,<br>**quiero** recargar o reemplazar la fuente de poder bajo asistencia de `IIA`,<br>**para** recuperar la potencia del láser y la capacidad de vuelo del dron. | - [ ] `IIA` asiste la operación de recarga (recupera nivel a 100%) y reemplazo (instala nueva fuente operativa).<br>- [ ] Al cambiar el nivel de energía de la fuente, la potencia reportada por el `Laser` cambia proporcionalmente.<br>- [ ] Con fuente agotada (`0`), no dispara láser ni vuela.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-08`: Aprendizaje de Idiomas Exclusivo por Expertos Parlantes
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-08` · **Iteración:** 2 (`R2`)<br>**Prioridad:** Media · **Estimación:** `5 pts`<br><br>**Como** estratega de la KGD,<br>**quiero** que el `AntCiberDron` aprenda inglés y español únicamente mediante expertos parlantes,<br>**para** garantizar que el léxico, gramática y fonética sean confiables. | - [ ] Soporta entrenamiento de **léxico, gramática y fonética** en **Inglés (EN)** y **Español (ES)**.<br>- [ ] El método de entrenamiento exige un actor/instancia válida de `ExpertoParlante` del idioma correspondiente; rechaza fuentes no expertas.<br>- [ ] Los entrenamientos quedan registrados para consulta en consola/UI y persistencia SQLite.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-09`: Hormiguero Virtual (Pantallas de consola + SQLite)
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-09` · **Iteración:** 3 (`R3`)<br>**Prioridad:** Alta · **Estimación:** `8 pts`<br><br>**Como** usuario de la KGD,<br>**quiero** pantallas de consola con menús para gestionar el hormiguero virtual, crear/alimentar hormigas y ver coordenadas destruidas,<br>**para** operar todo el sistema de manera sencilla. | - [ ] Permite crear hormigas (`HLarva`), seleccionar alimento y ver su evolución o muerte en tiempo real.<br>- [ ] Muestra el `Grupo06.csv`, las coordenadas destruidas por `IIA.buscar`, estado del `AntCiberDron` (fuente, láser, vuelo) y entrenamiento de idiomas.<br>- [ ] Persiste hormigas, alimentaciones, destrucciones y entrenamientos en **SQLite** según el MER.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-10`: Despliegue Dockerizado y Cero Incidentes
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-10` · **Iteración:** 3 (`R3`)<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** usuario y evaluador,<br>**quiero** ejecutar la aplicación mediante Docker y `docker compose` sin configurar dependencias manuales,<br>**para** asegurar portabilidad total y evitar fallos en la entrega (`-0.5`). | - [ ] `docker compose build` y `docker compose run --rm antdron` funcionan en máquina limpia.<br>- [ ] Soporta la consola interactiva (`stdin_open: true`, `tty: true`) mostrando la animación `\ \| / - \|`.<br>- [ ] Pipeline CI (`pytest` + `docker build`) en verde sin errores ni crashes.<br>**Valida:** I1 (Cliente) & I4 (Tester) |

---

## Tarjeta `HU-11`: Los 5 Diagramas Obligatorios y Bitácoras XP
| **ANVERSO (Frente de la Tarjeta)** | **REVERSO (Criterios de Aceptación)** |
| :--- | :--- |
| **ID:** `HU-11` · **Iteración:** 3 (`R3`)<br>**Prioridad:** Alta · **Estimación:** `5 pts`<br><br>**Como** equipo del Proyecto 6,<br>**quiero** entregar los 5 diagramas obligatorios del cuestionario en código PlantUML y los registros completos de XP,<br>**para** documentar la arquitectura y aprobar la evaluación sin observaciones. | - [ ] Entregados en **código PlantUML** únicamente los **5 diagramas obligatorios del PDF**:<br>  1. Diagrama de Clases (`pkAntCiberDronContract`)<br>  2. Diagrama de Casos de Uso<br>  3. Grafo con Gramática del Autómata (con cédulas reales)<br>  4. Modelo Entidad-Relación (MER)<br>  5. Diagrama de la Arquitectura de la Aplicación<br>- [ ] Actualizadas las bitácoras XP de las 4 fases (alineadas a Python 3.12) y checklist firmado por I1 (Cliente) e I4 (Tester).<br>**Valida:** I1 (Cliente) & I4 (Tester) |
