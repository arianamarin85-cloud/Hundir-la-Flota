import numpy as np
import funciones as f
import variable as v

# Creamos los 4 tableros del juego
t_barco_rival = f.crear_tablero()
t_barco_jugador = f.crear_tablero()
t_disparos_rival = f.crear_tablero()
t_disparos_jugador = f.crear_tablero()

flota_jugador = f.crear_flota()
flota_rival = f.crear_flota()

#Colocamos los barcos en los tableros
t_barco_jugador = f.colocar_barcos(t_barco_jugador)
t_barco_rival = f.colocar_barcos(t_barco_rival)

#Mostramos el tablero del jugador

print("********************************************")
print("************TABLERO BARCO JUGADOR***********")
print("********************************************")
print(t_barco_jugador)
print("********************************************")
print("*********TABLERO DISPAROS JUGADOR***********")
print("********************************************")
print(t_disparos_jugador)


print("Incio Juego"()) 
print("Turno Juego: ",f.crear_turno()) 