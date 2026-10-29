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


def colocar_flota(flota, tablero):
    for barco in flota:
        tablero = colocar_barco(barco, tablero)

    return tablero


def quedan_barcos(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "O":
                return True

    return False


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

    
def disparar(t_barco_rival,t_disparos_jugador,tiros_realizados,tiros_rival):
     
    try:
        fila = int(input("fila"))
        columna = int(input("columna"))
        
        if (fila, columna) in tiros_realizados:
            return "ya ha sido disparado"   
        
        elif  t_barco_rival[fila,columna] == "O":
              t_disparos_jugador[fila,columna] = "X"
              t_barco_rival[fila, columna] = "X" 
              tiros_realizados.append((fila, columna))
              return "Impacto"
        
        else:
            t_disparos_jugador[fila,columna] = "A"
            tiros_realizados.append((fila, columna))
            return "Fallo"
        
    except:
        print("valor invalido")
        return "vuelva a introducir las coordenadas"
    tiros_realizados = []
    
def disparar_rival(t_barco_jugador, t_disparos_rival, tiros_rival):
    while True:
        fila = np.random.randint(0, 10)
        columna = np.random.randint(0, 10)
        if (fila, columna) not in tiros_rival:
            break
            
    tiros_rival.append((fila, columna))
    if t_barco_jugador[fila, columna] == "O":
        t_disparos_rival[fila, columna] = "X"
        t_barco_jugador[fila, columna] = "X"
        return "Impacto"
    else:
        t_disparos_rival[fila, columna] = "A"
        return "Fallo"
    
def crear_turno(t_barco_rival,t_disparos_jugador,tiros_realizados,t_barco_jugador,t_disparos_rival,tiros_rival):
    d = np.random.randint(2)
    turno_jugador = 0
    
    while True:
        if  turno_jugador == 0:
            print ("Turno Jugador")
            resultado = disparar(t_barco_rival,t_disparos_jugador,tiros_realizados,tiros_rival)

            if resultado == "Fallo":
                turno_jugador = 1
            print("Resultado: ", resultado)
        else:
            print ("Turno Rival")
            resultado = disparar_rival(t_barco_jugador, t_disparos_rival, tiros_rival)
            if resultado == "Fallo":
                turno_jugador = 0
            print("Resultado: ", resultado)

         # Comprobamos resultados del juego

        if not quedan_barcos(t_barco_rival):
            print("Has hundido la flota rival.")
            break

        if not quedan_barcos(t_barco_jugador):
            print("Has perdido.")
            break

        print("Turnos Juego") 
        print("Tablero barcos jugador:")
        print(t_barco_jugador)

        print("Tablero disparos jugador:")
        print(t_disparos_jugador)

        print("Tablero barcos rival:")
        print(t_barco_rival)

        print("Tablero disparos rival:")
        print(t_disparos_rival)