import time
import numpy as np
from numpy.fft import fft2, ifft2
from matplotlib import pyplot, animation

from rules import *

# 


class Automata:

    def __init__(self, board, neighborhood, rule):
        self.board = board

        neighborhood = np.array(neighborhood)

        n_height, n_width = neighborhood.shape
        kernal = np.zeros(board.shape)
        kernal[(board.shape[0] - n_height - 1) // 2 : (board.shape[0] + n_height) // 2,
               (board.shape[1] - n_width - 1) // 2 : (board.shape[1] + n_width) // 2] = neighborhood
        self.kernal_ft = fft2(kernal)

        get_ints = lambda x: [i for i in x if isinstance(i, int)]
        self.rule_ints = (get_ints(rule[0]), get_ints(rule[1]))
        get_ranges = lambda x: [i for i in x if not isinstance(i, int)]
        self.rule_ranges = (get_ranges(rule[0]), get_ranges(rule[1]))


    def update(self, intervals=1):
        for i in range(intervals):
            convolution = self.fft_convolve2d()
            shape = convolution.shape
            new_board = np.zeros(shape)


            new_board[np.where(np.in1d(convolution, self.rule_ints[0]).reshape(shape)
                           & (self.board == 1))] = 1
            new_board[np.where(np.in1d(convolution, self.rule_ints[1]).reshape(shape)
                           & (self.board == 0))] = 1
            for rule_range in self.rule_ranges[0]:
                new_board[np.where((convolution >= rule_range[0]) & (convolution <= rule_range[1])
                                   & (self.board == 1))] = 1
            for rule_range in self.rule_ranges[1]:
                new_board[np.where((convolution >= rule_range[0]) & (convolution <= rule_range[1])
                                   & (self.board == 0))] = 1



            self.board = new_board



    def benchmark(self, interations):
        """
        XPS-15: Performed 5000 iterations of (256, 256) cells in 109.43707304 seconds
        """
        start = time.process_time()
        self.update(interations)
        print("Performed", interations, "iterations of", self.board.shape, "cells in",
              time.process_time() - start, "seconds")


    def animate(self, interval=100):
        
        def refresh(*args):
            self.update()
            image.set_array(self.board)
            return image,

        figure = pyplot.figure()
        image = pyplot.imshow(self.board, interpolation="nearest",
                              cmap=pyplot.cm.gray)
        ani = animation.FuncAnimation(figure, refresh, interval=interval)
        pyplot.show()


    def fft_convolve2d(self):
        board_ft = fft2(self.board)
        height, width = board_ft.shape
        convolution = np.real(ifft2(board_ft * self.kernal_ft))
        convolution = np.roll(convolution, - int(height / 2) + 1, axis=0)
        convolution = np.roll(convolution, - int(width / 2) + 1, axis=1)
        return convolution.round()


def random_board(shape, density):
    return np.random.uniform(0, 1, shape) < density


def main():
    bugs = Automata(
        board = np.random.uniform(0, 1, (256, 256)) < 0.5,
        neighborhood = np.ones((11, 11)),
        rule = (((34, 58),), ((34, 45),))
    )

    coagulations = Automata(
        board = np.random.uniform(0, 1, (256, 256)) < 0.5,
        neighborhood = ((1, 1, 1), (1, 0, 1), (1, 1, 1)),
        rule = ((2, 3, 5, 6, 7, 8), (3, 7, 8))
    )

    bugs.animate()

    #coagulations.benchmark(interations=1000)


if __name__ == "__main__":
    main()
