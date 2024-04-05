from graphics.inter_grafica import *
from src.chase import *

TIMER = 20
def main():
    """
    Inicializa el estado del juego
    """

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    enemigos = ENEMIGOS_INICIALES
    juego = crear_juego(FILAS_TABLERO, COLUMNAS_TABLERO)
    crear_nivel(juego, enemigos)
    timer = TIMER

    while gamelib.loop(fps=30) and juego["JUGADOR_VIVO"]:

        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key.upper()
                if tecla in MOVIMIENTOS:
                    movimiento_jugador(juego, tecla)
                elif tecla == 'SPACE':
                    teletransportacion(juego)
                elif tecla == "P":
                    gamelib.wait(gamelib.EventType.KeyPress)
                elif tecla == 'ESCAPE':
                    exit()

        timer -= 1
        if timer == 0:
            timer = TIMER
            movimiento_robots(juego)

        estado_juego(juego)

        if nivel_ganado(juego):
            juego = crear_juego(FILAS_TABLERO, COLUMNAS_TABLERO, juego["NIVEL"] + 1)
            enemigos += SIGUIENTE_NIVEL
            crear_nivel(juego, enemigos)
        
        gamelib.draw_begin()
        graficar_titulo()
        graficar_nivel(juego["NIVEL"])
        graficar_tablero()
        graficar_elemento(juego["TABLERO"], JUGADOR, "#00FF00")
        graficar_elemento(juego["TABLERO"], ROBOT, "#C0C0C0")
        graficar_elemento(juego["TABLERO"], OBSTACULO, "#FFFF00")
        graficar_teclas()
        graficar_referencias(JUGADOR, ROBOT, OBSTACULO)
        gamelib.draw_end()
    
    gamelib.draw_begin()
    graficar_game_over()
    graficar_boton_volver_a_jugar()
    gamelib.draw_end()

    event = gamelib.wait(gamelib.EventType.ButtonPress)
    if ANCHO_VENTANA * 1/4 <= event.x <= ANCHO_VENTANA * 3/4 and 400 <= event.y <= 450:
        main()

gamelib.init(main)