# Hyper CA
Hyper CA is a python package for simulating *2d binary totalistic cellular automata*, such as Conway's Game of Life. It uses 2D convolution to perform faster than standard implementations. The performance of this method is not affected by large neighborhood sizes or chaotic patterns.

### Animation of Conway's Game of Life
```
import numpy
from hyperca import Automata, models

board = numpy.random.uniform(size=(256, 256)) < 0.5
Automata(board, *models.conway).animate()
```

# Documentation
An `Automata` object has three parts: a board, neighborhood, and rule.

A **board** is a 2D list of binary states that represent the size and starting state of the simulation. A board of size 256x256 with 50% random starting density may be created with numpy.
```
board = numpy.random.uniform(size=(256, 256)) < 0.5
```

A **neighborhood** is a 2D list of integers that determines which of a cell's neighbors are counted towards its sum. Conway's Game of Life uses the Moore neighborhood.
```
neighborhood = [[1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]]
```

A **rule** is a list of two lists that specifies the numbers of alive neighbors for a cell to survive or be born in the next generation. A cell in Conway's Game of Life survives if it has 2 or 3 neighbors and is born if it has exactly 3 neighbors.
```
rule = [[2, 3], [3]]
```
Rules may also be defined as ranges. A range is a list containing a minimum and maximum value. Ranges may be used alongside individual integers. Cells in the Bugs model survive with between 34 and 58 neighbors and are born with between 34 and 48 neighbors.
```
rule = [[[34, 58]], [[34, 45]]]
```

Finally an `Automata` object may be created with these three parameters.
```
automata = Automata(board, neighborhood, rule)
```

## Built-in Models
Hyper CA contains over 30 built-in models with predefined neighborhoods and rules. The `conway` model returns the neighborhood and rule used for Conway's Game of Life.
```
automata = Automata(board, *models.conway)
```
Each of these models demonstrate an intereseting aspect of cellular automata and are detailed in the [Cellular Automata rules lexicon](http://psoup.math.wisc.edu/mcell/ca_rules.html). Note that you may need to adjust the board's starting density to properly observe the model.
