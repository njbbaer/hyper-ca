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
        self.kernal = np.zeros(shape)
        self.kernal[(shape[0] - n_height - 1) // 2 : (shape[0] + n_height) // 2,
                    (shape[1] - n_width - 1) // 2 : (shape[1] + n_width) // 2] = neighborhood

        self.rule = rule


    def update(self, intervals=1):
        for i in range(intervals):
            convolution = Automata.fft_convolve2d(self.board, self.kernal)
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


    @staticmethod
    def fft_convolve2d(board, kernal):
        board_ft = fft2(board)
        kernal_ft = fft2(kernal)
        height, width = board_ft.shape
        convolution = np.real(ifft2(board_ft * kernal_ft))
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

    def __init__(self, shape, density, rule, radius, skip_center):
        neighborhood = np.ones((radius*2+1, radius*2+1))
        if skip_center:
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

    # automata = Conway(shape, 0.2)
    # automata = Life34(shape, 0.12)
    # automata = Amoeba(shape, 0.18)
    # automata = Anneal(shape, 0.5)
    # automata = TwoByTwo(shape, 0.5)
    # automata = Assimilation(shape, 0.16)
    # automata = Coagulations(shape, 0.5)
    # automata = Coral(shape, 0.25)
    # automata = DayAndNight(shape, 0.5)
    # automata = Diamoeba(shape, 0.48)
    # automata = LifeWithoutDeath(shape, 0.02)
    # automata = Gnarl(shape, 0.0001)
    # automata = HighLife(shape, 0.5)
    # automata = InverseLife(shape, 0.5)
    # automata = LongLife(shape, 0.2)
    # automata = Maze(shape, 0.02, False)
    # automata = Move(shape, 0.1)
    # automata = PseudoLife(shape, 0.1)
    # automata = Replicator(shape, 0.00002)
    # automata = Seeds(shape, 0.005)
    # automata = Serviettes(shape, 0.002)
    # automata = Stains(shape, 0.08)
    # automata = WalledCities(shape, 0.19)

    automata = Bugs(shape, 0.5)
    # automata = BugsMovie(shape, 0.5)
    # automata = Globe(shape, 0.4)

    # automata.benchmark(interations=5000)

    automata.animate(interval=100)


if __name__ == "__main__":
    main()
