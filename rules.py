from automata import *


class TwoByTwo(Life):
    def __init__(self, shape, density):
        rule = ((1, 2, 5), (3, 6))
        super().__init__(shape, density, rule)


class Life34(Life):
    def __init__(self, shape, density):
        rule = ((3, 4), (3, 4))
        super().__init__(shape, density, rule)


class Amoeba(Life):
    def __init__(self, shape, density):
        rule = ((1, 3, 5, 8), (3, 5, 7))
        super().__init__(shape, density, rule)


class Anneal(Life):
    def __init__(self, shape, density):
        rule = ((3, 5, 6, 7, 8), (4, 6, 7, 8))
        super().__init__(shape, density, rule)


class Assimilation(Life):
    def __init__(self, shape, density):
        rule = ((4, 5, 6, 7), (3, 4, 5))
        super().__init__(shape, density, rule)


class Coagulations(Life):
    def __init__(self, shape, density):
        rule = ((2, 3, 5, 6, 7, 8), (3, 7, 8))
        super().__init__(shape, density, rule)


class Conway(Life):
    def __init__(self, shape, density):
        rule = ((2, 3), (3))
        super().__init__(shape, density, rule)


class Coral(Life):
    def __init__(self, shape, density):
        rule = ((4, 5, 6, 7, 8), (3))
        super().__init__(shape, density, rule)


class DayAndNight(Life):
    def __init__(self, shape, density):
        rule = ((3, 4, 6, 7, 8), (3, 6, 7, 8))
        super().__init__(shape, density, rule)


class Diamoeba(Life):
    def __init__(self, shape, density):
        rule = ((5, 6, 7, 8), (3, 5, 6, 7, 8))
        super().__init__(shape, density, rule)


class Flakes(Life):
    def __init__(self, shape, density):
        rule = ((0, 1, 2, 3, 4, 5, 6, 7, 8), (3))
        super().__init__(shape, density, rule)


class Gnarl(Life):
    def __init__(self, shape, density):
        rule = ((1), (1))
        super().__init__(shape, density, rule)


class HighLife(Life):
    def __init__(self, shape, density):
        rule = ((2, 3), (3, 6))
        super().__init__(shape, density, rule)


class InverseLife(Life):
    def __init__(self, shape, density):
        rule = ((3, 4, 6, 7, 8), (0, 1, 2, 3, 4, 7, 8))
        super().__init__(shape, density, rule)


class LongLife(Life):
    def __init__(self, shape, density):
        rule = ((5), (3, 4, 5))
        super().__init__(shape, density, rule)


class Maze(Life):
    def __init__(self, shape, density, has_runners):
        rule = [[1, 2, 3, 4, 5], [3]]
        if has_runners:
        	rule[1].append(7)
        super().__init__(shape, density, rule)


class Move(Life):
    def __init__(self, shape, density):
        rule = ((2, 4, 5), (3, 6, 8))
        super().__init__(shape, density, rule)


class PseudoLife(Life):
    def __init__(self, shape, density):
        rule = ((2, 3, 8), (3, 5, 7))
        super().__init__(shape, density, rule)


class Replicator(Life):
    def __init__(self, shape, density):
        rule = ((1, 3, 5, 7), (1, 3, 5, 7))
        super().__init__(shape, density, rule)


class Seeds(Life):
    def __init__(self, shape, density):
        rule = ((), (2))
        super().__init__(shape, density, rule)


class Serviettes(Life):
    def __init__(self, shape, density):
        rule = ((), (2, 3, 4))
        super().__init__(shape, density, rule)


class Stains(Life):
    def __init__(self, shape, density):
        rule = ((2, 3, 5, 6, 7, 8), (3, 6, 7, 8))
        super().__init__(shape, density, rule)


class WalledCities(Life):
    def __init__(self, shape, density):
        rule = ((2, 3, 4, 5), (4, 5, 6, 7, 8))
        super().__init__(shape, density, rule)


class Bugs(LargerThanLife):
    def __init__(self, shape, density):
        radius = 5
        rule = ((34, 58), (34, 45))
        super().__init__(shape, density, rule, radius, False)


class Globe(LargerThanLife):
    def __init__(self, shape, density):
        radius = 8
        rule = ((163, 223), (74, 252))
        super().__init__(shape, density, rule, radius, True)
