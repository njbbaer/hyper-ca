import sys
import numpy
import argparse

import hyperca


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('height', help='height of board', type=int)
    parser.add_argument('width', help='width of board', type=int)
    parser.add_argument('density', help='inital density', type=float)

    model_parsers = parser.add_subparsers(help='automata model')

    life_parser = model_parsers.add_parser('life', help='life')
    life_parser.add_argument('-b', help='neighbors for birth', nargs='*', type=int)
    life_parser.add_argument('-s', help='neighbors for survival', nargs='*', type=int)
    life_parser.set_defaults(mode='life')

    ltl_parser = model_parsers.add_parser('ltl', help='larger than life')
    ltl_parser.add_argument('radius', help='neighborhood radius', type=int)
    ltl_parser.add_argument('birth_min', help='minimum neighbors for birth', type=int)
    ltl_parser.add_argument('birth_max', help='maximum neighbors for birth', type=int)
    ltl_parser.add_argument('survival_min', help='minimum neighbors for survival', type=int)
    ltl_parser.add_argument('survival_max', help='maximum neighbors for survival', type=int)
    ltl_parser.set_defaults(mode='ltl')

    return parser.parse_args()


args = parse_args()

if args.mode == 'life':
    neighborhood = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    rule = [args.s, args.b]
elif args.mode == 'ltl':
    neighborhood = numpy.ones((args.radius*2+1, args.radius*2+1))
    rule = [[[args.survival_min, args.survival_max]], [[args.birth_min, args.birth_max]]]

shape = (args.height, args.width)

automata = hyperca.automata.Automata(shape, neighborhood, rule)
automata.populate(args.density)
automata.animate()
