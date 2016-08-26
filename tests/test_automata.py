import unittest
import numpy
import hyperca


class TestAutomata(unittest.TestCase):
 
    def test_conway_update(self):
        start_board = [[1, 1, 1, 0],
                       [0, 0, 0, 1],
                       [0, 1, 1, 1],
                       [1, 0, 1, 0]]

        end_board = [[1, 0, 1, 0],
                     [0, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 0]]

        neighborhood = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        rule = [[3, 2], [3]]
        automata = hyperca.Automata(neighborhood, rule)
        automata.init_board(start_board)
        automata.update()
        
        numpy.testing.assert_array_equal(automata.board, end_board)


if __name__ == '__main__':
    unittest.main()