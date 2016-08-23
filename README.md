# Hyper CA
Hyper CA is a python package for simulating *2d binary totalistic cellular automata*, such as Conway's Game of Life. It uses fast 2D convolution to outperform many other implementations. This method is especially efficient for models with large neighborhood sizes, such as the amazingly lifelike Bugs.

### Animation of the Bugs model
```python
from hyperca import models

automata = models.bugs((256, 256))
automata.populate(0.5)
automata.animate()
```

# Documentation
An `Automata` object is the basic unit of a cellular automata simulation. It is defined by a board size, neighborhood, and rule.

## Built-in Models
Hyper CA contains over 30 built-in models each with a predefined neighborhood and rule. The `conway` model returns an `Automata` object with the parameters for Conway's Game of Life. The `shape` parameter sets the size of the board.
```python
from hyperca import models

automata = models.conway(shape=(256, 256))
```

Each of these models demonstrates an intereseting aspect of cellular automata and are detailed in the [Cellular Automata rules lexicon](http://psoup.math.wisc.edu/mcell/ca_rules.html).

## Custom Models
Defining a custom model requires a board shape, neighborhood, and rule.
```python
from hyperca import Automata

automata = Automata((256, 256), neighborhood, rule)
```

A **neighborhood** is a 2D list of integers that determines which of a cell's neighbors are counted towards its sum. Conway's Game of Life uses the Moore neighborhood.
```python
neighborhood = [[1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]]
```

A **rule** is a list of two lists that specifies the numbers of alive neighbors for a cell to survive or be born in the next generation. A cell in Conway's Game of Life survives if it has 2 or 3 neighbors and is born if it has exactly 3 neighbors.
```python
rule = [[2, 3], [3]]
```

Rules may also be defined as ranges. A range is a list containing a minimum and maximum value. Ranges may be used alongside individual integers. Cells in the Bugs model survive with between 34 and 58 neighbors and are born with between 34 and 48 neighbors.
```python
rule = [[[34, 58]], [[34, 45]]]
```

## Simulation
### Populate
The board of a new `Automata` object is initialized with inactive states. The `populate` method will randomly fill the board with active states at a given density.
```python
automata.populate(density=0.5)
```

### Update
The `update` method will advance the board to its next state. Set the optional `iterations` parameter to perform multiple consecutive updates.
```python
automata.update(iterations=1)
```

### Animate
The `animate` method will graphically display and update the the board using matplotlib. Set the optional `interval` parameter to define the number of milliseconds between each frame. Note that choosing an interval smaller than your computer can compute the update may freeze the animation.
```python
automata.animate(interval=100)
```

### Benchmark
The `benchmark` method will measure the time taken to perform a given number of iterations. Results for an Intel Core i7-4870HQ.
```python
automata.benchmark(iterations=10000)
# 10000 iterations of (256, 256) cells in 61.86 seconds
```

# Contribute
If you enjoy this project show your thanks by starring the repository. Please support it by submitting any bugs, feature requests, or general comments as GitHub issues. Feel free to contribute directly by forking and making changes. I will gladly review pull requests.