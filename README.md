# Hundir la Flota

---

## 1. Introducción

* **Objetivo:**  
  En este proyecto he desarrollado la lógica base del juego *Hundir la Flota*, centrándome en la inicialización de los tableros y la colocación automatizada de barcos.

* **Arquitectura:**  
  Para mantener un código limpio y profesional, estructuré el desarrollo en tres archivos independientes: uno para las constantes fijas del juego, otro con las funciones de lógica y un archivo principal de ejecución.

* **Valor técnico:**  
  El mayor reto técnico ha sido el algoritmo de generación de coordenadas, asegurando mediante restricciones que ningún barco se salga de los límites del tablero ni rompa el programa.

---

## 2. Estructura de los Archivos

### `variable.py`
Contiene los datos constantes que definen las reglas del juego:
* Tamaño del tablero: `10x10`.
* Lista de esloras: `[4, 3, 3, 2, 2, 2]`.  
*Tener estos valores centralizados facilita la parametrización y escalabilidad futura del juego.*

### `funciones.py`
Contiene la lógica interna del juego:
* `crear_tablero`: Genera una matriz de `10x10` inicializada con agua (`'~'`).
* `crear_barco`: Determina aleatoriamente la orientación (Horizontal/Vertical) y calcula casillas válidas.
* `colocar_barco` *(singular)*: Imprime un barco individual en el tablero usando `'O'`.
* `colocar_barcos` *(plural)*: Itera sobre la flota completa e invoca `colocar_barco` para cada nave.
* `disparar`: Procesa la entrada del usuario con validación de errores y registra impactos.
* `disparar_rival`: Automatiza los disparos de la IA mediante un bucle de coordenadas aleatorias no repetidas.
* `crear_turno`: Administra el flujo del juego y la alternancia de turnos.

### `main.py`
Punto de entrada de la aplicación. Inicializa los tableros del jugador y del rival, ejecuta la colocación automática de la flota y coordina el ciclo principal de juego.

---

## 3. Puntos Clave y Decisiones Técnicas

### 3.1. Diferencia entre `colocar_barco` y `colocar_barcos`
* **`colocar_barco` (singular):** Pinta un único barco en la matriz a partir de unas coordenadas concretas.
* **`colocar_barcos` (plural):** Recorre la lista de esloras, llama a `crear_barco` para cada una y las va pintando una a una en el tablero.

### 3.2. Restricción de límites (`10 - eslora + 1`)
Para evitar que un barco sobresalga de la matriz (índices válidos del 0 al 9):
* Si un barco mide 4 casillas, el último índice de inicio válido es la fila o columna 6 (`10 - 4 = 6`).
* Se añade `+1` porque `np.random.randint(min, max)` es excluyente en su límite superior, garantizando así que el 6 sea una opción elegible.

### 3.3. Gestión de solapamiento
En esta versión preliminar, si dos barcos coinciden en posición, se sobrescriben las marcas `'O'`. La prioridad de diseño en esta fase fue asegurar que ninguna coordenada exceda los márgenes de la matriz.

### 3.4. Mecánica de Disparo del Jugador
Obtiene fila y columna mediante `input()`. Incorpora un bloque `try / except` para capturar entradas inválidas del usuario sin interrumpir la ejecución. Controla los tiros previos mediante bloques `if / else` para evitar disparar a casillas repetidas y actualiza el tablero correspondiente.

### 3.5. Mecánica de Disparo del Rival
Genera coordenadas automáticas controladas mediante un bucle `while True` que valida que la casilla no haya sido atacada previamente, garantizando disparos únicos por parte de la IA.

```python
def disparar_rival(t_barco_jugador, t_disparos_rival, tiros_rival):
    ...

    ...
```python

def disparar(t_barco_rival, t_disparos_jugador, tiros_realizados, tiros_rival):
    ...
