import numpy as np
import funciones as f
import variable as v

# Creamos los 4 tableros del juego
t_barco_rival = f.crear_tablero()
t_barco_jugador = f.crear_tablero()
t_disparos_rival = f.crear_tablero()
t_disparos_jugador = f.crear_tablero()

# Creamos la flota
flota_jugador = f.crear_flota()
flota_rival = f.crear_flota()

#Colocamos los barcos en los tableros
t_barco_jugador = f.colocar_flota(flota_jugador, t_barco_jugador)
t_barco_rival = f.colocar_flota(flota_rival, t_barco_rival)

#Creamos lista de tiros realizados
tiros_realizados = []
tiros_rival = []

#Mostramos el tablero del jugador
print("********************************************")
print("************TABLERO BARCO JUGADOR***********")
print("********************************************")
print(t_barco_jugador)
print("********************************************")
print("*********TABLERO DISPAROS JUGADOR***********")
print("********************************************")
print(t_disparos_jugador)

#Mostramos el tablero del Rival
print("********************************************")
print("************TABLERO BARCO RIVAL*************")
print("********************************************")
print(t_barco_rival)

print("********************************************")
print("*********TABLERO DISPAROS RIVAL*************")
print("********************************************")
print(t_disparos_rival)

f.crear_turno(t_barco_rival, t_disparos_jugador, tiros_realizados, t_barco_jugador, t_disparos_rival,tiros_rival)

