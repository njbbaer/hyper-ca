import sys
import hyperca
import numpy


shape = (int(sys.argv[1]), int(sys.argv[2]))


if str(sys.argv[3]) == "ltl":
    radius = int(sys.argv[4])
    neighborhood = numpy.ones((radius*2+1, radius*2+1))

    birth_range = [int(sys.argv[5]), int(sys.argv[6])]
    survival_range = [int(sys.argv[7]), int(sys.argv[8])]
    rule = ([survival_range], [birth_range])

    automata = hyperca.automata.Automata(shape, neighborhood, rule)
    automata.populate(float(sys.argv[9]))
    automata.animate()