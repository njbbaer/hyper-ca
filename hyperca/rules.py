import numpy as np
from collections import namedtuple

from hyperca import Automata

Rule = namedtuple("Rule", "rule neighborhood")

def amoeba():
    return Rule(rule = [[1, 3, 5, 8], [3, 5, 7]],
                neighborhood = _moore_neighborhood())

def anneal():
    return Rule(rule = [[3, 5, 6, 7, 8], [4, 6, 7, 8]],
                neighborhood = _moore_neighborhood())

def assimilation():
    return Rule(rule = [[4, 5, 6, 7], [3, 4, 5]],
                neighborhood = _moore_neighborhood())

def coagulations():
    return Rule(rule = [[2, 3, 5, 6, 7, 8], [3, 7, 8]],
                neighborhood = _moore_neighborhood())

def conway():
    return Rule(rule = [[2, 3], [3]],
                neighborhood = _moore_neighborhood())

def coral():
    return Rule(rule = [[4, 5, 6, 7, 8], [3]],
                neighborhood = _moore_neighborhood())

def day_and_night():
    return Rule(rule = [[3, 4, 6, 7, 8], [3, 6, 7, 8]],
                neighborhood = _moore_neighborhood())

def diamoeba():
    return Rule(rule = [[5, 6, 7, 8], [3, 5, 6, 7, 8]],
                neighborhood = _moore_neighborhood())

def flakes():
    return Rule(rule = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [3]],
                neighborhood = _moore_neighborhood())

def gnarl():
    return Rule(rule = [[1], [1]],
                neighborhood = _moore_neighborhood())

def high_life():
    return Rule(rule = [[2, 3], [3, 6]],
                neighborhood = _moore_neighborhood())

def inverse_life():
    return Rule(rule = [[3, 4, 6, 7, 8], [0, 1, 2, 3, 4, 7, 8]],
                neighborhood = _moore_neighborhood())

def life_34():
    return Rule(rule = [[1, 2, 5], [3, 6]],
                neighborhood = _moore_neighborhood())

def long_life():
    return Rule(rule = [[5], [3, 4, 5]],
                neighborhood = _moore_neighborhood())

def maze():
    return Rule(rule = [[1, 2, 3, 4, 5], [3]],
                neighborhood = _moore_neighborhood())

def move():
    return Rule(rule = [[2, 4, 5], [3, 6, 8]],
                neighborhood = _moore_neighborhood())

def pseudo_life():
    return Rule(rule = [[2, 3, 8], [3, 5, 7]],
                neighborhood = _moore_neighborhood())

def replicator():
    return Rule(rule = [[1, 3, 5, 7], [1, 3, 5, 7]],
                neighborhood = _moore_neighborhood())

def seeds():
    return Rule(rule = [[], [2,]],
                neighborhood = _moore_neighborhood())

def serviettes():
    return Rule(rule = [[], [2, 3, 4]],
                neighborhood = _moore_neighborhood())

def stains():
    return Rule(rule = [[2, 3, 5, 6, 7, 8], [3, 6, 7, 8]],
                neighborhood = _moore_neighborhood())

def two_by_two():
    return Rule(rule = [[1, 2, 5], [3, 6]],
                neighborhood = _moore_neighborhood())

def walled_cities():
    return Rule(rule = [[2, 3, 4, 5], [4, 5, 6, 7, 8]],
                neighborhood = _moore_neighborhood())

def bugs():
    return Rule(rule = [[[34, 58]], [[34, 45]]],
                neighborhood = _box_neighborhood(radius=5))

def bugs_movie():
    return Rule(rule = [[[123, 212]], [[123, 170]]],
                neighborhood = _box_neighborhood(radius=10))

def globe():
    return Rule(rule = [[[163, 223]], [[74, 252]]],
                neighborhood = _box_neighborhood(radius=8, center=False))

def majority():
    return Rule(rule = [[[41, 81]], [[41, 81]]],
                neighborhood = _box_neighborhood(radius=4))

def majorly():
    return Rule(rule = [[[113, 225]], [[113, 225]]],
                neighborhood = _box_neighborhood(radius=7))

def waffle():
    return Rule(rule = [[[100, 200]],[[75, 170]]],
                neighborhood = _box_neighborhood(radius=7))

def ltl59999():
    return Rule(rule = [[[9, 9]], [[9, 9]]],
                neighborhood = _box_neighborhood(radius=5))

def ltl534473460():
    return Rule(rule = [[[34, 60]], [[34, 47]]],
                neighborhood = _box_neighborhood(radius=5))

def ltl534413458():
    return Rule(rule = [[[34, 58]], [[34, 41]]],
                neighborhood = _box_neighborhood(radius=5))

def _moore_neighborhood():
    return [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]

def _box_neighborhood(radius, center=True):
    neighborhood = np.ones((radius*2+1, radius*2+1))
    if not center:
        neighborhood[radius][radius] = 0
    return neighborhood