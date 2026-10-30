# Hundir la Flota

---

## 1. Introducción

* **Objetivo:**  
  Este proyecto se ha desarrollado la lógica base del juego *Hundir la Flota*, centrándome en la inicialización de los tableros y la colocación automatizada de barcos.

* **Arquitectura:**  
  Para mantener un código limpio y profesional, estructuré el desarrollo en tres archivos independientes: uno para las constantes fijas del juego, otro con las funciones de lógica y un archivo principal de ejecución.

* **Valor técnico:**  
  El mayor reto técnico ha sido el algoritmo de generación de coordenadas, asegurando mediante restricciones que ningún barco se salga de los límites del tablero ni rompa el programa.

---

## 2. Estructura de los Archivos

* **`variable.py`:**  
  Aquí guardo los datos constantes que definen las reglas: el tamaño `10x10` y la lista de esloras `[4, 3, 3, 2, 2, 2]`. Tenerlo separado hace que sea fácil adaptar el juego en el futuro.

* **`funciones.py`:**  
  * `crear_tablero`: Genera la matriz de 10x10 con agua (`'~'`).
  * `crear_barco`: Decide la orientación (Horizontal/Vertical) y calcula casillas válidas.
  * `colocar_barco` *(singular)*: Estampa un barco concreto con `'O'`.
  * `colocar_barcos` *(plural)*: Coordina la flota completa mediante un bucle.
  * `disparar`: Gestiona los tiros del jugador, validando entradas y actualizando el tablero.
  * `disparar_rival`: Automatiza los disparos de la máquina asegurando tiros no repetidos.
  * `crear_turno`: Coordina la alternancia y el flujo de turnos de la partida.

* **`main.py`:**  
  Inicializa los tableros del jugador y del rival, llama a la colocación automática y muestra el resultado del juego.

---

## 3. Puntos Clave

### 3.1. `colocar_barco` (singular y plural)
* **`colocar_barco` (singular):** Pinta un único barco en la matriz.
* **`colocar_barcos` (plural):** Recorre la lista de esloras, llama a `crear_barco` y luego las va pintando una a una.

### 3.2. Uso de `10 - eslora + 1` en la coordenada inicial
Sirve para evitar que el barco se salga del tablero (índices del 0 al 9):
* Si un barco mide 4, el último inicio válido es la fila 6 (`10 - 4 = 6`).
* Se suma `+1` porque `np.random.randint` excluye el límite superior, y es necesario que el 6 sí pueda salir como resultado válido.

### 3.3. Si dos barcos se solapan
En esta versión actual se sobrescriben las `'O'`. La prioridad técnica fue asegurar que ningún barco se saliera de los márgenes del tablero.

### 3.4. Mecánica de Disparo del Jugador
Obtiene las filas y columnas mediante `input()`. Se implementa un bloque `try / except` en caso de que el usuario introduzca parámetros incorrectos. Asimismo, genera un registro de tiros realizados mediante bloques `if / else` y se encarga de actualizar los tiros una vez efectuados.

```python
def disparar(t_barco_rival, t_disparos_jugador, tiros_realizados, tiros_rival):
    ...
```

### 3.5. Mecánica de Disparo del Rival
Genera coordenadas automáticas controladas mediante un bucle `while True` que valida que la casilla no haya sido atacada previamente, garantizando disparos únicos por parte de la IA.

```python
def disparar_rival(t_barco_jugador, t_disparos_rival, tiros_rival):
    ...
```

### 3.6. Sistema de Turnos
El inicio de la partida se sortea aleatoriamente mediante `np.random.randint(2)`. Posteriormente, a través de un bucle se evalúa el resultado de cada ataque y se actualizan los tableros y listas de impacto en cada iteración.

```python
def crear_turno(t_barco_rival, t_disparos_jugador, tiros_realizados, t_barco_jugador, t_disparos_rival, tiros_rival):
    d = np.random.randint(2)
    ...
```
