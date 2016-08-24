import sys
import numpy
import argparse

import hyperca

parser = argparse.ArgumentParser()
parser.add_argument("height", help="height of board", type=int)
parser.add_argument("width", help="width of board", type=int)
parser.add_argument("density", help="inital density", type=float)
parser.add_argument("radius", help="neighborhood radius", type=int)
parser.add_argument("birth_min", help="minimum neighbors for birth", type=int)
parser.add_argument("birth_max", help="maximum neighbors for birth", type=int)
parser.add_argument("survival_min", help="minimum neighbors for survival", type=int)
parser.add_argument("survival_max", help="maximum neighbors for survival", type=int)
args = parser.parse_args()

shape = (args.height, args.width)
neighborhood = numpy.ones((args.radius*2+1, args.radius*2+1))
rule = [[[args.survival_min, args.survival_max]], [[args.birth_min, args.birth_max]]]

automata = hyperca.automata.Automata(shape, neighborhood, rule)
automata.populate(args.density)
automata.animate()