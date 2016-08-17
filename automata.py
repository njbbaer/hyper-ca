import time
import numpy as np
from numpy.fft import fft2, ifft2
from matplotlib import pyplot, animation

from rules import *


class Automata:

    def __init__(self, shape, density, neighborhood, rule):
        self.board = np.random.uniform(0, 1, shape)
        self.board = self.board < density

        n_height, n_width = neighborhood.shape
        kernal = np.zeros(shape)
        kernal[(shape[0] - n_height - 1) // 2 : (shape[0] + n_height) // 2,
               (shape[1] - n_width - 1) // 2 : (shape[1] + n_width) // 2] = neighborhood
        self.kernal_ft = fft2(kernal)

        self.rule = rule


    def update(self, intervals=1):
        for i in range(intervals):
            convolution = self.fft_convolve2d()
            self.apply_rule(convolution)


    def benchmark(self, interations):
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


class Life(Automata):

    def __init__(self, shape, density, rule):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        super().__init__(shape, density, neighborhood, rule)


    def apply_rule(self, convolution):
        shape = convolution.shape
        new_board = np.zeros(shape)
        new_board[np.where(np.in1d(convolution, self.rule[0]).reshape(shape)
                           & (self.board == 1))] = 1
        new_board[np.where(np.in1d(convolution, self.rule[1]).reshape(shape)
                           & (self.board == 0))] = 1
        self.board = new_board


class LargerThanLife(Automata):

    def __init__(self, shape, density, rule, radius, include_center):
        neighborhood = np.ones((radius*2+1, radius*2+1))
        if not include_center:
            neighborhood[radius][radius] = 0
        super().__init__(shape, density, neighborhood, rule)


    def apply_rule(self, convolution):
        shape = convolution.shape
        new_board = np.zeros(shape)
        new_board[np.where((convolution >= self.rule[0][0]) & (convolution <= self.rule[0][1])
                           & (self.board == 1))] = 1
        new_board[np.where((convolution >= self.rule[1][0]) & (convolution <= self.rule[1][1])
                           & (self.board == 0))] = 1
        self.board = new_board


def main():
    shape = (256, 256)

    # Bugs(shape).benchmark(interations=10000)

    Bugs(shape).animate(interval=100)


if __name__ == "__main__":
    main()
