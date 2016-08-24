import numpy as np

from .automata import Automata


def moore_neighborhood():
    return [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]


def box_neighborhood(radius, center):
    neighborhood = np.ones((radius*2+1, radius*2+1))
    if not center:
        neighborhood[radius][radius] = 0
    return neighborhood


def amoeba(shape):
    rule = [[1, 3, 5, 8], [3, 5, 7]]
    return Automata(shape, moore_neighborhood(), rule)


def anneal(shape):
    rule = [[3, 5, 6, 7, 8], [4, 6, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def assimilation(shape):
    rule = [[4, 5, 6, 7], [3, 4, 5]]
    return Automata(shape, moore_neighborhood(), rule)


def coagulations(shape):
    rule = [[2, 3, 5, 6, 7, 8], [3, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def conway(shape):
    rule = [[2, 3], [3]]
    return Automata(shape, moore_neighborhood(), rule)


def coral(shape):
    rule = [[4, 5, 6, 7, 8], [3]]
    return Automata(shape, moore_neighborhood(), rule)


def day_and_night(shape):
    rule = [[3, 4, 6, 7, 8], [3, 6, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def diamoeba(shape):
    rule = [[5, 6, 7, 8], [3, 5, 6, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def flakes(shape):
    rule = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [3]]
    return Automata(shape, moore_neighborhood(), rule)


def gnarl(shape):
    rule = [[1], [1]]
    return Automata(shape, moore_neighborhood(), rule)


def high_life(shape):
    rule = [[2, 3], [3, 6]]
    return Automata(shape, moore_neighborhood(), rule)


def inverse_life(shape):
    rule = [[3, 4, 6, 7, 8], [0, 1, 2, 3, 4, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def life_34(shape):
    rule = [[1, 2, 5], [3, 6]]
    return Automata(shape, moore_neighborhood(), rule)


def long_life(shape):
    rule = [[5], [3, 4, 5]]
    return Automata(shape, moore_neighborhood(), rule)


def maze(shape):
    rule = [[1, 2, 3, 4, 5], [3]]
    return Automata(shape, moore_neighborhood(), rule)


def move(shape):
    rule = [[2, 4, 5], [3, 6, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def pseudo_life(shape):
    rule = [[2, 3, 8], [3, 5, 7]]
    return Automata(shape, moore_neighborhood(), rule)


def replicator(shape):
    rule = [[1, 3, 5, 7], [1, 3, 5, 7]]
    return Automata(shape, moore_neighborhood(), rule)


def seeds(shape):
    rule = [[], [2,]]
    return Automata(shape, moore_neighborhood(), rule)


def serviettes(shape):
    rule = [[], [2, 3, 4]]
    return Automata(shape, moore_neighborhood(), rule)


def stains(shape):
    rule = [[2, 3, 5, 6, 7, 8], [3, 6, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def two_by_two(shape):
    rule = [[1, 2, 5], [3, 6]]
    return Automata(shape, moore_neighborhood(), rule)


def walled_cities(shape):
    rule = [[2, 3, 4, 5], [4, 5, 6, 7, 8]]
    return Automata(shape, moore_neighborhood(), rule)


def bugs(shape):
    rule = [[[34, 58]], [[34, 45]]]
    neighborhood = box_neighborhood(radius=5, center=True)
    return Automata(shape, neighborhood, rule)


def bugs_movie(shape):
    rule = [[[123, 212]], [[123, 170]]]
    neighborhood = box_neighborhood(radius=10, center=True)
    return Automata(shape, neighborhood, rule)


def globe(shape):
    rule = [[[163, 223]], [[74, 252]]]
    neighborhood = box_neighborhood(radius=8, center=False)
    return Automata(shape, neighborhood, rule)


def majority(shape):
    rule = [[[41, 81]], [[41, 81]]]
    neighborhood = box_neighborhood(radius=4, center=True)
    return Automata(shape, neighborhood, rule)


def majorly(shape):
    rule = [[[113, 225]], [[113, 225]]]
    neighborhood = box_neighborhood(radius=7, center=True)
    return Automata(shape, neighborhood, rule)


def waffle(shape):
    rule = [[[100, 200]], [[75, 170]]]
    neighborhood = box_neighborhood(radius=7, center=True)
    return Automata(shape, neighborhood, rule)


def ltl59999(shape):
    '''
    LtL rule (5, 9, 9, 9)
    Ideal density: 0.1
    '''
    rule = [[[9, 9]], [[9, 9]]]
    neighborhood = box_neighborhood(radius=5, center=True)
    return Automata(shape, neighborhood, rule)
    