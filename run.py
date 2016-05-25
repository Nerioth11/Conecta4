import games
import heuristicas
# import heuristicasCompaneros
from utils import *


# -----------------------------------------------------------------------------------------------------------------------
def obtenerTipoPartida():
    input = None
    while (input != "H" and input != "M"):
        input = raw_input("\033[0;34mEscoja un tipo de partida (H=HvM, M=MvM): \033[0;m")
    return input


def obtenerHeuristicaMaquina():
    input = None
    while (input != "0" and input != "1" and input != "2"):
        input = raw_input("\033[0;34mEscoja el nivel de la maquina (0=facil, 1=medio 2=dificil): \033[0;m")

    if input == "0":
        return None
    elif input == "1":
        return heuristicas.heuristicaRegular
    elif input == "2":
        return heuristicas.heuristicaBuena


def obtenerJugadorQueEmpieza():
    input = None
    while (input != "X" and input != "O"):
        input = raw_input("\033[0;34mEscoja que jugador empieza (X=maquina, O=usted|companero): \033[0;m")
    return input


# -----------------------------------------------------------------------------------------------------------------------
game = games.ConnectFour()
state = game.initial
tipo = obtenerTipoPartida()

heuristicaCompanero = None  # AQUI SE INDICA LA HEURISTICA DE OTRO GRUPO
heuristicaMaquina = obtenerHeuristicaMaquina()

game.initial.to_move = obtenerJugadorQueEmpieza()
player = game.initial.to_move
print "-------------------"
# -----------------------------------------------------------------------------------------------------------------------

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        if tipo == "H":
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            move = games.alphabeta_search(state, game, eval_fn=heuristicaCompanero, d=6)
            state = game.make_move(move, state)
            player = 'X'

    else:
        print "Thinking..."
        move = games.alphabeta_search(state, game, eval_fn=heuristicaMaquina)
        state = game.make_move(move, state)
        player = 'O'

    print "-------------------"

    if game.terminal_test(state):
        game.display(state)
        if len(state.moves) == 0:
            print "Final de la partida: Empate"
        else:
            print "Final de la partida: Gana", if_(state.to_move == 'X', 'O', 'X')

        break
