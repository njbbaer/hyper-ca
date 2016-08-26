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


    def test_init_board_populate(self):
        neighborhood = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        rule = [[3, 2], [3]]
        automata = hyperca.Automata(neighborhood, rule)
        automata.init_board_populate((16, 16), 0.5)
        self.assertIn(1, automata.board)
        self.assertIn(0, automata.board)


    def test_bugs_benchmark(self):
        neighborhood = numpy.ones((11, 11))
        rule = [[[34, 58]], [[34, 58]]]
        automata = hyperca.Automata(neighborhood, rule)
        automata.init_board_populate((128, 128), 0.5)
        automata.benchmark(iterations=100)


if __name__ == '__main__':
    unittest.main()