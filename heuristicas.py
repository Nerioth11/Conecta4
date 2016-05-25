from utils import *


def memoize(f):
    memo = {}

    def helper(state):
        if state not in memo:
            memo[state] = f(state)
        return memo[state]

    return helper


def check_legal_position(x, y):
    return if_(x >= 1 and y >= 1 and x <= 7 and y <= 6, 1, 0)


def count_empty_holes(board, x, y):
    holes = 0
    while y >= 1 and board.get((x, y)) is None:
        holes += 1
        y -= 1
    return holes


# -----------------------------------------------------------------------------------------------------------------------
@memoize
def heuristicaBuena(state):
    if state.utility != 0:
        return state.utility * infinity

    heuristica = 0
    player = state.to_move
    rival = if_(player == 'X', 'O', 'X')
    movimientos_legales = [(x, y) for (x, y) in state.moves
                           if y == 1 or (x, y - 1) in state.board]

    for move in movimientos_legales:
        heuristica += k_in_row_bueno(state.board, move, player, rival, (0, 1))
        heuristica += k_in_row_bueno(state.board, move, player, rival, (1, 0))
        heuristica += k_in_row_bueno(state.board, move, player, rival, (1, -1))
        heuristica += k_in_row_bueno(state.board, move, player, rival, (-1, 1))
        heuristica -= k_in_row_bueno(state.board, move, rival, player, (0, 1))
        heuristica -= k_in_row_bueno(state.board, move, rival, player, (1, 0))
        heuristica -= k_in_row_bueno(state.board, move, rival, player, (1, -1))
        heuristica -= k_in_row_bueno(state.board, move, rival, player, (-1, 1))

    return heuristica


def k_in_row_bueno(board, move, player, rival, (delta_x, delta_y)):
    k = 0
    h = 0

    x, y = move
    while check_legal_position(x, y) and board.get((x, y)) != rival:
        k += 1
        h += if_(board.get((x, y)) == player, 10 + 10 * k, -count_empty_holes(board, x, y) / k)
        x, y = x + delta_x, y + delta_y

    x, y = move
    while check_legal_position(x, y) and board.get((x, y)) != rival:
        k += 1
        h += if_(board.get((x, y)) == player, 10 + 10 * k, -count_empty_holes(board, x, y) / k)
        x, y = x - delta_x, y - delta_y

    k -= 1
    return if_(k >= 4, h, if_(h > 0, -h - 50, h - 50))


# -----------------------------------------------------------------------------------------------------------------------
@memoize
def heuristicaRegular(state):
    if state.utility != 0:
        return state.utility * infinity

    heuristica = 0
    player = state.to_move
    rival = if_(player == 'X', 'O', 'X')
    movimientos_legales = [(x, y) for (x, y) in state.moves
                           if y == 1 or (x, y - 1) in state.board]

    for move in movimientos_legales:
        heuristica += k_in_row_regular(state.board, move, rival, (0, 1))
        heuristica += k_in_row_regular(state.board, move, rival, (1, 0))
        heuristica += k_in_row_regular(state.board, move, rival, (1, -1))
        heuristica += k_in_row_regular(state.board, move, rival, (-1, 1))

    return heuristica


def k_in_row_regular(board, move, rival, (delta_x, delta_y)):
    k = 0
    h = 0

    x, y = move
    while check_legal_position(x, y) and board.get((x, y)) != rival:
        h += if_(board.get((x, y)) is None, 5, 10)
        k += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    while check_legal_position(x, y) and board.get((x, y)) != rival:
        h += if_(board.get((x, y)) is None, 5, 10)
        k += 1
        x, y = x - delta_x, y - delta_y

    k -= 1
    return if_(k >= 4, h, 0)
