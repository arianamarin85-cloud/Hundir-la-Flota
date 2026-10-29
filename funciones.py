import numpy as np
import variable as v

def crear_tablero():
    tablero = np.full((v.tamanio,v.tamanio), "~")
    return tablero

def crear_barco(eslora):
    d = np.random.randint(2)
    
    barco = []  # lista vacia donde guardare todas las coordenadas del barco
    
    if d == 0:  # si la posicion es igual a cero construyo hacia abajo
        # Dejo fija las columnas y sumo +1 en filas
        coor_ini = (np.random.randint(0, 10 - eslora + 1), np.random.randint(0, 10))  # creo coor inicial
        print(coor_ini)
        barco.append(coor_ini)  # añado primera coordenada a la lista del barco
        pos = 1
        for i in np.arange(eslora - 1):  # itero por la eslora 
            barco.append((coor_ini[0] + pos, coor_ini[1]))
            pos = pos + 1

    elif d==1:
         coor_ini = (np.random.randint(0, 10), np.random.randint(0, 10 - eslora + 1))  
         barco.append(coor_ini)  # añado primera coordenada a la lista del barco
         pos = 1
         for i in np.arange(eslora - 1):  # itero por la eslora 
            # Dejo fija las filas y sumo una posicion en la columna
            barco.append((coor_ini[0], coor_ini[1] + pos))
            pos = pos + 1  
    else:
         print("Calculando barco de nuevo")
         barco = crear_barco(eslora)

    return barco

def crear_flota():
    flota = []
    esloras = [4, 3, 3, 2, 2, 2]
    
    for eslora in esloras:
     flota.append(crear_barco(eslora))
     
     lista_posiciones = []
    for barco in flota:
        for pos in barco:
            lista_posiciones.append(pos)
    if len(lista_posiciones)  != len(set(lista_posiciones)):
        flota = crear_flota()
    return flota

def colocar_barco(barco, tablero):
    for elemento in barco:
        tablero[elemento] = "O"
    return tablero

def colocar_barcos(tablero):
    esloras = [4, 3, 3, 2, 2, 2]

    for eslora in esloras:
        barco = crear_barco(eslora)
        colocar_barco(barco, tablero)  
    return tablero

def crear_turno():
    d = np.random.randint(2)

    if d == 0:
        return "Inicio Jugador"
    else:
        return "Inicio Rival"
    
    tiros_realizados = []
def disparar(t_barco_rival,t_disparos_jugador,tiros_realizados):
     
    try:
        fila = int(input("fila"))
        columna = int(input("columna"))
        
        if (fila, columna) in tiros_realizados:
            return "ya ha sido disparado"   
        
        elif  t_barco_rival[fila,columna] == "O":
              t_disparos_jugador[fila,columna] = "X"
              tiros_realizados.append((fila, columna))
              return "Impacto"
        
        else:
            t_disparos_jugador[fila,columna] = "A"
            tiros_realizados.append((fila, columna))
            return "Fallo"
        
    except:
        print("valor invalido")
        return "vuelva a introducir las coordenadas"

def crear_turno(t_barco_rival,t_disparos_jugador,tiros_realizados,t_barco_jugador,t_disparos_rival):
    turno_jugador = 0
    d = np.random.randint(2)
    while True:
        if  turno_jugador == 0:
            print ("Turno Jugador")
            resultado = f.disparar(t_barco_rival,t_disparos_jugador,tiros_realizados)
            if resultado == "Fallo":
                turno_jugador = 1
            print("Resultado: ", resultado)
        else:
            print ("Turno Rival")
            resultado = disparar(t_barco_jugador,t_disparos_rival,tiros_realizados)
            if resultado == "Fallo":
                turno_jugador = 0
            print("Resultado: ", resultado)

print("Turnos Juego") 
print("Turno Juego: ",crear_turno())
        
