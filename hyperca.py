'''
python3 hyperca.py 512 512 0.5 ltl 5 34 45 34 58
'''

import numpy
import argparse
import hyperca


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

weighted_parser = model_parsers.add_parser('weighted', help='life')
weighted_parser.add_argument('nw', help='weight for north west cell', type=int)
weighted_parser.add_argument('nn', help='weight for north cell', type=int)
weighted_parser.add_argument('ne', help='weight for north east cell', type=int)
weighted_parser.add_argument('ww', help='weight for west cell', type=int)
weighted_parser.add_argument('me', help='weight for center cell', type=int)
weighted_parser.add_argument('ee', help='weight for east cell', type=int)
weighted_parser.add_argument('sw', help='weight for south west cell', type=int)
weighted_parser.add_argument('ss', help='weight for south cell', type=int)
weighted_parser.add_argument('se', help='weight for south east cell', type=int)
weighted_parser.add_argument('-b', help='neighbors for birth', nargs='*', type=int)
weighted_parser.add_argument('-s', help='neighbors for survival', nargs='*', type=int)
weighted_parser.set_defaults(mode='weighted')

args = parser.parse_args()

if args.mode == 'life':
    neighborhood = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    rule = [args.s, args.b]

elif args.mode == 'ltl':
    neighborhood = numpy.ones((args.radius*2+1, args.radius*2+1))
    rule = [[[args.survival_min, args.survival_max]], [[args.birth_min, args.birth_max]]]

elif args.mode == 'weighted':
    neighborhood = [[args.nw, args.nn, args.ne],
                    [args.ww, args.me, args.ee],
                    [args.sw, args.ss, args.se]]
    rule = [args.s, args.b]

shape = (args.height, args.width)

automata = hyperca.Automata(neighborhood, rule)
automata.init_board_populate(shape, args.density)
automata.animate()
