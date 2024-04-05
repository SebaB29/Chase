from random import randint

JUGADOR, ROBOT, OBSTACULO, POSICION_LIBRE = "♥", "☻", "☼", ""
ENEMIGOS_INICIALES, SIGUIENTE_NIVEL = 5, 5

MOVIMIENTOS = {
    "W": [0,-1],
    "A": [-1,0],
    "D": [1,0],
    "S": [0,1],
    "Q": [-1,-1],
    "E": [1,-1],
    "Z": [-1,1],
    "C": [1,1]
    }

def crear_juego(filas_tablero, columnas_tablero, nivel=1):
    """
    Crea un diccionario con los datos iniciales del juego.
    """

    return {
    "TABLERO":[[POSICION_LIBRE for columna in range(columnas_tablero)] for fila in range(filas_tablero)],
    "COORDENADAS_JUGADOR": None,
    "COORDENADAS_ROBOTS": [],
    "COORDENADAS_OBSTACULOS": [],
    "NIVEL": nivel,
    "JUGADOR_VIVO": True
    }

def generar_coordenadas_elemento(tablero):
    """..."""

    return randint(0, len(tablero[0]) - 1), randint(0, len(tablero) - 1)

def colocar_elemento(juego, referencia_elemento, elemento, cantidad=1):
    """
    -Recibe: el diccionario juego, la referencia a un elemento, el elemento y la cantidad,
     en caso de no recibir la cantidad, por defecto es 1.
    -Coloca en el tablero la cantidad del elemento ambos pasado por parámetro y
     guarda las coordenadas de los elementos en un diccionario.
    """

    while cantidad:
        coordenada_x, coordenada_y = generar_coordenadas_elemento(juego["TABLERO"])
        if juego["TABLERO"][coordenada_y][coordenada_x] == POSICION_LIBRE:
            juego["TABLERO"][coordenada_y][coordenada_x] = elemento
            if elemento == JUGADOR:
                juego[referencia_elemento] = [coordenada_x, coordenada_y]
            else:
                juego[f"{referencia_elemento}"].append([coordenada_x, coordenada_y])

            cantidad -= 1

def crear_nivel(juego, cant_nivel):
    """
    -Recibe: el diccionario juego y cant_nivel
     Llama a la funcion colocar_elemento para cada elemento y asi crear el nivel.
    """

    colocar_elemento(juego, "COORDENADAS_JUGADOR", JUGADOR)
    colocar_elemento(juego, "COORDENADAS_ROBOTS", ROBOT, cant_nivel)
    colocar_elemento(juego, "COORDENADAS_OBSTACULOS", OBSTACULO, cant_nivel)

def coordenada_esta_en_rango(tablero, coordenada_x, coordenada_y):
    """
    -Recibe: una coordenada_x y una coordenada_y
    -Devuelve: un booleano que determina si las coordenadas estan dentro del rango del tablero,
     True si lo esta y False en caso contrario.
    """

    return (0 <= coordenada_x < len(tablero[0])) and (0 <= coordenada_y < len(tablero))

def movimiento_jugador(juego, tecla):
    """
    -Recibe: el diccionario juego y la tecla presionada
     Actualiza las coordenadas del jugador y ubica al jugador en sus nuevas coordenadas en el tablero.
    """

    coord_x_jugador, coord_y_jugador = juego["COORDENADAS_JUGADOR"]
    desplazamiento_x, desplazamiento_y = MOVIMIENTOS[tecla]
    nueva_coord_x, nueva_coord_y = coord_x_jugador + desplazamiento_x, coord_y_jugador + desplazamiento_y
    if coordenada_esta_en_rango(juego["TABLERO"], nueva_coord_x, nueva_coord_y):   
        if juego["TABLERO"][nueva_coord_y][nueva_coord_x] == OBSTACULO:
            nueva_coord_x_obstaculo, nueva_coord_y_obstaculo = nueva_coord_x + desplazamiento_x, nueva_coord_y + desplazamiento_y
            if not desplazar_obstaculos(juego, (nueva_coord_x, nueva_coord_y), (nueva_coord_x_obstaculo, nueva_coord_y_obstaculo)):
                return

        juego["TABLERO"][coord_y_jugador][coord_x_jugador] = POSICION_LIBRE
        juego["TABLERO"][nueva_coord_y][nueva_coord_x] = JUGADOR
        juego["COORDENADAS_JUGADOR"] = [nueva_coord_x, nueva_coord_y]

def desplazar_obstaculos(juego, coordenadas_obstaculo, nuevas_coordenadas_obstaculo):
    """
    -Recibe: el diccionario juego, las coordenadas del obstaculo y las nuevas coordenadas del obstaculo, 
     Si el desplazamiento se puede realizar (si la posición de desplazamiento está libre, si está dentro del tablero de juego), 
     actualiza las coordenada del obstáculo y lo ubica con sus nuevas coordenadas en el tablero,
     guarda las nuevas coordenadas del obstáculo y devuelve True. 
    """

    coord_x_obstaculo, coord_y_obstaculo = coordenadas_obstaculo
    nueva_coord_x_obstaculo, nueva_coord_y_obstaculo = nuevas_coordenadas_obstaculo
    if coordenada_esta_en_rango(juego["TABLERO"], nueva_coord_x_obstaculo, nueva_coord_y_obstaculo) and juego["TABLERO"][nueva_coord_y_obstaculo][nueva_coord_x_obstaculo] == POSICION_LIBRE:
        juego["TABLERO"][nueva_coord_y_obstaculo][nueva_coord_x_obstaculo] = OBSTACULO
        viejas_coord_obstaculo = juego["COORDENADAS_OBSTACULOS"].index([coord_x_obstaculo, coord_y_obstaculo])
        juego["COORDENADAS_OBSTACULOS"][viejas_coord_obstaculo] = [nueva_coord_x_obstaculo, nueva_coord_y_obstaculo]
        return True

def movimiento_robots(juego):
    """
    -Recibe: el diccionario juego
     Al mover al jugador, se realizan los movimientos de los robots.
    """

    coord_x_jugador, coord_y_jugador = juego["COORDENADAS_JUGADOR"]
    for i, coordenadas_robot in enumerate(juego["COORDENADAS_ROBOTS"]):
        coord_x_robot, coord_y_robot = coordenadas_robot
        coordenada_x, coordenada_y = coordenadas_robot

        if coord_x_robot < coord_x_jugador:
            coordenada_x += 1
        elif coord_x_robot > coord_x_jugador:
            coordenada_x -= 1
        if coord_y_robot < coord_y_jugador:
            coordenada_y += 1
        elif coord_y_robot > coord_y_jugador:
            coordenada_y -= 1

        juego["TABLERO"][coord_y_robot][coord_x_robot] = POSICION_LIBRE 
        juego["COORDENADAS_ROBOTS"][i] = [coordenada_x, coordenada_y]
        juego["TABLERO"][coordenada_y][coordenada_x] = ROBOT

def estado_juego(juego):
    """
    -Recibe: el diccionario juego
     Verifica las posiciones y el estado de los robots para actualizar el estado del juego
    """

    coord_robot_a_eliminar = []

    for i_robot_1, coordenadas_robot in enumerate(juego["COORDENADAS_ROBOTS"]):
        if coordenadas_robot == juego["COORDENADAS_JUGADOR"]:
                juego["JUGADOR_VIVO"] = False
        else:
            coord_x_robot, coord_y_robot = coordenadas_robot
            if coordenadas_robot in juego["COORDENADAS_OBSTACULOS"]:
                juego["TABLERO"][coord_y_robot][coord_x_robot] = OBSTACULO
                coord_robot_a_eliminar.append(coordenadas_robot)

            for i_robot_2, coordenadas_robot_2 in enumerate(juego["COORDENADAS_ROBOTS"]):
                if (coordenadas_robot == coordenadas_robot_2) and (i_robot_1 != i_robot_2):
                    juego["COORDENADAS_OBSTACULOS"].append([coord_x_robot, coord_y_robot])
                    juego["TABLERO"][coord_y_robot][coord_x_robot] = OBSTACULO
                    coord_robot_a_eliminar.append(coordenadas_robot)

    for coordenadas in coord_robot_a_eliminar:
        while coordenadas in juego["COORDENADAS_ROBOTS"]:
            juego["COORDENADAS_ROBOTS"].remove(coordenadas)

def teletransportacion(juego):
    """
    -Recibe: el diccionario juego
     Teletransporta al jugador a una posición aleatoria
    """

    nueva_coord_y, nueva_coord_x = randint(0, len(juego["TABLERO"]) - 1), randint(0, len(juego["TABLERO"][0]) - 1)
    coord_x_jugador, coord_y_jugador = juego["COORDENADAS_JUGADOR"]
    juego["TABLERO"][coord_y_jugador][coord_x_jugador] = POSICION_LIBRE
    juego["COORDENADAS_JUGADOR"] = [nueva_coord_x, nueva_coord_y]
    juego["TABLERO"][nueva_coord_y][nueva_coord_x] = JUGADOR

def nivel_ganado(juego):
    """
    -Recibe: el diccionario juego
     Verifica si ganó el nivel
    """
 
    return len(juego["COORDENADAS_ROBOTS"]) == 0