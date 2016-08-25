import unittest
import numpy
import hyperca

class TestAutomata(unittest.TestCase):
 
    def test_conway_update(self):
        start_board = numpy.array([[1, 1, 1, 0],
                                   [0, 0, 0, 1],
                                   [0, 1, 1, 1],
                                   [1, 0, 1, 0]], dtype=int)

        end_board = numpy.array([[1, 0, 1, 0],
                                 [0, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 0, 0]], dtype=int)

        neighborhood = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        rule = [[3, 2], [3]]
        automata = hyperca.Automata((4, 4), neighborhood, rule)
        automata.board = start_board
        automata.update()
        
        numpy.testing.assert_array_equal(automata.board, end_board)


if __name__ == '__main__':
    unittest.main()