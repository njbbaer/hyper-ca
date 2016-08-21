from automata import *


def moore():
    return [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]


def box(radius, center):
    neighborhood = np.ones((radius*2+1, radius*2+1))
    if not center:
        neighborhood[radius][radius] = 0
    return neighborhood


def amoeba(board):
    rule = [[1, 3, 5, 8], [3, 5, 7]]
    return Automata(board, moore(), rule)


def anneal(board):
    rule = [[3, 5, 6, 7, 8], [4, 6, 7, 8]]
    return Automata(board, moore(), rule)


def assimilation(board):
    rule = [[4, 5, 6, 7], [3, 4, 5]]
    return Automata(board, moore(), rule)


def coagulations(board):
    rule = [[2, 3, 5, 6, 7, 8], [3, 7, 8]]
    return Automata(board, moore(), rule)


def conway(board):
    rule = [[2, 3], [3]]
    return Automata(board, moore(), rule)


def coral(board):
    rule = [[4, 5, 6, 7, 8], [3]]
    return Automata(board, moore(), rule)


def day_and_night(board):
    rule = [[3, 4, 6, 7, 8], [3, 6, 7, 8]]
    return Automata(board, moore(), rule)


def diamoeba(board):
    rule = [[5, 6, 7, 8], [3, 5, 6, 7, 8]]
    return Automata(board, moore(), rule)


def flakes(board):
    rule = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [3]]
    return Automata(board, moore(), rule)


def gnarl(board):
    rule = [[1], [1]]
    return Automata(board, moore(), rule)


def high_life(board):
    rule = [[2, 3], [3, 6]]
    return Automata(board, moore(), rule)


def inverse_life(board):
    rule = [[3, 4, 6, 7, 8], [0, 1, 2, 3, 4, 7, 8]]
    return Automata(board, moore(), rule)


def life_34(board):
    rule = [[1, 2, 5], [3, 6]]
    return Automata(board, moore(), rule)


def long_life(board):
    rule = [[5], [3, 4, 5]]
    return Automata(board, moore(), rule)


def maze(board):
    rule = [[1, 2, 3, 4, 5], [3]]
    return Automata(board, moore(), rule)


def move(board):
    rule = [[2, 4, 5], [3, 6, 8]]
    return Automata(board, moore(), rule)


def pseudo_life(board):
    rule = [[2, 3, 8], [3, 5, 7]]
    return Automata(board, moore(), rule)


def replicator(board):
    rule = [[1, 3, 5, 7], [1, 3, 5, 7]]
    return Automata(board, moore(), rule)


def seeds(board):
    rule = [[], [2,]]
    return Automata(board, moore(), rule)


def serviettes(board):
    rule = [[], [2, 3, 4]]
    return Automata(board, moore(), rule)


def stains(board):
    rule = [[2, 3, 5, 6, 7, 8], [3, 6, 7, 8]]
    return Automata(board, moore(), rule)


def two_by_two(board):
    rule = [[1, 2, 5], [3, 6]]
    return Automata(board, moore(), rule)


def walled_cities(board):
    rule = [[2, 3, 4, 5], [4, 5, 6, 7, 8]]
    return Automata(board, moore(), rule)


def bugs(board):
    rule = [[[34, 58]], [[34, 45]]]
    neighborhood = box(radius=5, center=True)
    return Automata(board, neighborhood, rule)


def bugs_movie(board):
    rule = [[[123, 212]], [[123, 170]]]
    neighborhood = box(radius=10, center=True)
    return Automata(board, neighborhood, rule)


def globe(board):
    rule = [[[163, 223]], [[74, 252]]]
    neighborhood = box(radius=8, center=False)
    return Automata(board, neighborhood, rule)


def majority(board):
    rule = [[[41, 81]], [[41, 81]]]
    neighborhood = box(radius=4, center=True)
    return Automata(board, neighborhood, rule)


def majorly(board):
    rule = [[[113, 225]], [[113, 225]]]
    neighborhood = box(radius=7, center=True)
    return Automata(board, neighborhood, rule)


def waffle(board):
    rule = [[[100, 200]], [[75, 170]]]
    neighborhood = box(radius=7, center=True)
    return Automata(board, neighborhood, rule)