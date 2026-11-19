# Revisión de cumplimiento del enunciado

Revisión del 18 de noviembre de 2026 contra el archivo PROYECTO XP.pdf y la versión web publicada en la Parte 4. Cambios de revisión aplicados localmente sobre feature/parte4-web-docker.

| Requisito | Resultado verificado |
| --- | --- |
| Autenticación de integrantes y profesor, máximo tres intentos | Cubierto por pruebas HTTP y de dominio. El bloqueo web corresponde a la sesión del navegador. |
| Presentar equipo, nombres y cédulas | Corregida la plantilla para presentar las cédulas completas. |
| Grupo06.csv generado según las cédulas | Verificadas las 40 filas contra el generador y los cuatro números de cédula. Repeticiones conservadas intencionalmente. |
| Loading por coordenada | Añadida presentación progresiva de filas con indicador y porcentaje hasta 100%. La animación representa la presentación de filas ya procesadas por el servidor. Pendiente revisión visual del navegador. |
| Autómata con últimos dígitos 2, 3, 5, 9 | Evaluación y pruebas de dominio aprobadas. Lenguaje ab* unido con abc y abcdt+. |
| Búsqueda mediante IIA y bomba | Integración probada con las 40 filas y sus 29 palabras aceptadas. |
| Mostrar coordenadas aceptadas | Corregido resultado por fila. Añadida tabla separada con geoposición, palabra y acción true. |
| Larva con néctar, evolución y supervivencia con alimento de su tipo | Probada la evolución a rastreadora con herbívoro y la persistencia de identidad y estado. El grupo confirmó expresamente rastreadora para el grupo 6; la tabla del PDF llega al grupo 5. |
| Extremidades, metralleta derecha, láser izquierdo y potencia según energía | Modelados los componentes virtuales y comprobados por pruebas de dominio. |
| Turbo en espalda, fuente recargable y reemplazable con IIA | Modelados y accesibles desde la web. El consumo de una unidad por vuelo y la potencia numérica igual a la energía son decisiones de la simulación, sin fórmula fijada en el PDF. |
| Aprendizaje EN/ES, léxico, gramática y fonética por expertos | Añadido formulario web e historial persistente. El servidor selecciona entre expertos de simulación con idioma y certificación definidos. Se rechazan especialidades incorrectas y expertos desconocidos. |
| Pantallas del hormiguero | Probados login, carga CSV, creación, alimentación y operaciones mediante el cliente HTTP de Flask. Revisión visual pendiente. |
| Cinco diagramas | Existen los cinco Markdown. Cuatro incluyen PlantUML en el documento; casos de uso tiene su fuente en img/02-casos-de-uso.puml. La pantalla de idiomas añade un punto de entrada web que debe reflejarse en arquitectura al consolidar el documento final. |
| Portada | Documento final contiene fecha 19/11/2026, grupo 06, metáfora, integrantes y roles. |
| XP y evidencias | Historias, planificación y PR disponibles. Videos y capturas de trabajo real pendientes de grabación por el equipo. El framework tiene contenido que debe sincronizarse con la entrega final. |
| Aplicación dockerizada | Dockerfile y Compose disponibles. Ejecución real pendiente porque Docker no está disponible en este entorno. |

## Pruebas de esta revisión

68 pruebas de pytest aprobadas en Python 3.14. Se agregaron regresiones que comprueban el resultado de cada fila HTML y la selección del experto de idioma. Falta ejecutar Python 3.12 dentro de Docker y verificar la apariencia, navegación y animación en navegador.

## Origen de las coordenadas

tools/generar_csv.py recorre los diez dígitos de cada una de las cuatro cédulas. Cada dígito genera una fila de catálogo mediante ArsenalCatalogo.filaCSV. Un dígito repetido produce otra fila con la misma geoposición; las palabras de ejemplo rotan. La pertenencia al lenguaje se evalúa por palabra y por fila, incluso si una geoposición ya apareció.

El alfabeto del ejercicio asocia a con avión, b con barco, c con convoy, d con dron y t con tanque. El autómata recibe esa secuencia de letras y devuelve un booleano. Coord-03 es la etiqueta del catálogo para el dígito 3.

## Cómo verificar la versión corregida

Detener el proceso web anterior con Ctrl+C y volver a ejecutar python web_app.py. Acceder a http://localhost:5000, iniciar sesión y cargar el CSV de nuevo. Comprobar 40 filas, 29 aceptadas y 11 rechazadas. Revisar la tabla separada, el spinner por fila y el registro de entrenamiento EN/ES. Los cambios locales requieren reiniciar Flask porque debug está desactivado.
