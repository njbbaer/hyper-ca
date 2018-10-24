from hyperca import Automata, rules

automata = Automata(rules.bugs(), [64, 128])
automata.populate_random(0.5)
automata.animate()