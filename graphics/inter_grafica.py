import graphics.gamelib as gamelib

ANCHO_VENTANA, ALTO_VENTANA = (600, 600)
MARGEN_X, MARGEN_Y = (10, 80)
COLUMNAS_TABLERO, FILAS_TABLERO = (30, 30)
ANCHO_TABLERO, ALTO_TABLERO = ((ANCHO_VENTANA - MARGEN_X * 2), (ALTO_VENTANA - MARGEN_Y * 2))
ANCHO_CELDA, ALTO_CELDA = (ANCHO_TABLERO / COLUMNAS_TABLERO, ALTO_TABLERO / FILAS_TABLERO)

TECLAS_A_MOSTRAR = {
    "Q":(60, ALTO_VENTANA - 60),
    "W":(80, ALTO_VENTANA - 60),
    "E":(100, ALTO_VENTANA - 60),
    "A":(60, ALTO_VENTANA - 40),
    "D":(100, ALTO_VENTANA - 40),
    "Z":(60, ALTO_VENTANA - 20),
    "S":(80, ALTO_VENTANA - 20),
    "C":(100, ALTO_VENTANA - 20),
    "P: PAUSA": (ANCHO_VENTANA / 2 - 20, ALTO_VENTANA - 60),
    "ESPACIO: TELETRANSPORTE":(ANCHO_VENTANA / 2 - 20, ALTO_VENTANA - 40)
    }

def graficar_titulo():
    """..."""

    gamelib.draw_text("CHASE", ANCHO_VENTANA / 2, MARGEN_Y / 2, size=20)

def graficar_nivel(nivel):
    """..."""

    gamelib.draw_text(f"Nivel {nivel}", 40, 70, size = 15)

def graficar_tablero():
    """..."""

    gamelib.draw_rectangle(MARGEN_X, MARGEN_Y, ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA - MARGEN_Y, fill = "#474E4B", outline="#000000")

    posicion_linea_horizontal =  MARGEN_Y + ALTO_CELDA
    for _ in range(FILAS_TABLERO - 1):
        gamelib.draw_line(MARGEN_X, posicion_linea_horizontal, ANCHO_VENTANA - MARGEN_X, posicion_linea_horizontal, fill="black")
        posicion_linea_horizontal += ALTO_CELDA
    
    posicion_linea_vertical = MARGEN_X + ANCHO_CELDA
    for _ in range(COLUMNAS_TABLERO - 1):
        gamelib.draw_line(posicion_linea_vertical, MARGEN_Y, posicion_linea_vertical, ALTO_VENTANA - MARGEN_Y, fill="#000000")
        posicion_linea_vertical += ANCHO_CELDA

def graficar_elemento(tablero, elemento, color):
    """..."""

    for posicion_pixels_x, posicion_pixels_y in convertir_coordenadas_a_pixels(tablero, elemento):
        gamelib.draw_text(elemento, posicion_pixels_x + ANCHO_CELDA / 2, posicion_pixels_y + ALTO_CELDA / 2, fill=color)

def graficar_referencias(jugador, robot, obstaculo):
    """..."""

    referencias = {
    "jugador":(f"JUGADOR: {jugador}", ANCHO_VENTANA - 116, ALTO_VENTANA - 60, "#00FF00"),
    "robot":(f"ROBOT: {robot}", ANCHO_VENTANA - 123, ALTO_VENTANA - 40, "#C0C0C0"),
    "obstaculo":(f"OBSTACULOS: {obstaculo}", ANCHO_VENTANA - 100, ALTO_VENTANA - 20, "#FFFF00")
    }

    for referencia in referencias:
        gamelib.draw_text(referencias[referencia][0], referencias[referencia][1], referencias[referencia][2], fill=referencias[referencia][3])

def graficar_teclas():
    """..."""

    for tecla in TECLAS_A_MOSTRAR.keys():
        gamelib.draw_text(tecla, TECLAS_A_MOSTRAR[tecla][0], TECLAS_A_MOSTRAR[tecla][1])

def graficar_game_over():
    """..."""

    gamelib.draw_text("GAME \nOVER", ANCHO_VENTANA / 2 + MARGEN_X, ALTO_VENTANA / 2 - 40, size=70, fill="#E3E4E5")

def graficar_boton_volver_a_jugar():
    """..."""

    gamelib.draw_rectangle(ANCHO_VENTANA * 1/4, 400, ANCHO_VENTANA * 3/4, 450, fill = "black", outline = "#FFFFFF")
    gamelib.draw_text("Volver a empezar", ANCHO_VENTANA / 2, 425, size = 15)

def convertir_coordenadas_a_pixels(tablero, elemento):
    """
    -Recibe: el tablero y un elemento
    -Devuelve: una lista con las coordenadas en pixeles del elemento
    """

    return [
        [MARGEN_X + ANCHO_CELDA * columna, MARGEN_Y + ALTO_CELDA * fila] 
        for columna in range(len(tablero[0])) 
        for fila in range(len(tablero)) 
        if tablero[fila][columna] == elemento
        ]