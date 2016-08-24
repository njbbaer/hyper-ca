import hyperca

shape = (576, 1024)

automata = hyperca.models.ltl534413458(shape)

automata.populate(0.3)

automata.animate()