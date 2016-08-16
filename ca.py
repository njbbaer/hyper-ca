import time
import numpy as np
from numpy.fft import fft2, ifft2
from matplotlib import pyplot, animation


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
            shape = convolution.shape
            new_board = np.zeros(shape)
            new_board[np.where(np.in1d(convolution, self.rule[0]).reshape(shape)
                               & (self.board == 1))] = 1
            new_board[np.where(np.in1d(convolution, self.rule[1]).reshape(shape)
                               & (self.board == 0))] = 1
            self.board = new_board


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


    @classmethod
    def conway(cls, shape, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[2, 3], [3]]
        automata = cls(shape, density, neighborhood, rule)
        return automata


    @classmethod
    def life34(cls, shape, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[3, 4], [3, 4]]
        automata = cls(shape, density, neighborhood, rule)
        return automata


    @classmethod
    def amoeba(cls, shape, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[1, 3, 5, 8], [3, 5, 7]]
        automata = cls(shape, density, neighborhood, rule)
        return automata


    @classmethod
    def anneal(cls, shape, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[3, 5, 6, 7, 8], [4, 6, 7, 8]]
        automata = cls(shape, density, neighborhood, rule)
        return automata


    @classmethod
    def bugs(cls, shape, density):
        neighborhood = np.ones((11, 11))
        rule = [np.arange(34, 59), np.arange(34, 46)]
        automata = cls(shape, density, neighborhood, rule)
        return automata


    @classmethod
    def globe(cls, shape, density):
        neighborhood = np.ones((17, 17))
        neighborhood[8][8] = 0
        rule = [np.arange(163, 224), np.arange(74, 253)]
        automata = cls(shape, density, neighborhood, rule)
        return automata


def main():
    # Create automata
    automata = Automata.bugs((256, 256), density=0.5)
    # automata = Automata.conway((256, 256), density=0.5)
    # automata = Automata.life34((256, 256), density=0.12)
    # automata = Automata.amoeba((256, 256), density=0.18)
    # automata = Automata.anneal((256, 256), density=0.5)
    # automata = Automata.globe((256, 256), density=0.4)

    # Benchmark automata
    # automata.benchmark(interations=5000)

    # Animate automata
    automata.animate(interval=100)


if __name__ == "__main__":
    main()
