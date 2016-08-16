import time
import numpy as np
from numpy.fft import fft2, ifft2
from matplotlib import pyplot, animation


def fft_convolve2d(board, kernal):
    board_ft = fft2(board)
    kernal_ft = fft2(kernal)
    height, width = board_ft.shape
    convolution = np.real(ifft2(board_ft * kernal_ft))
    convolution = np.roll(convolution, - int(height / 2) + 1, axis=0)
    convolution = np.roll(convolution, - int(width / 2) + 1, axis=1)
    return convolution.round()


class Automata:
    def __init__(self, height, width, density, neighborhood, rule):
        self.board = np.random.uniform(0, 1, (width, height))
        self.board = self.board < density

        k_height, k_width = neighborhood.shape
        self.kernal = np.zeros((height, width))
        self.kernal[(height - k_height - 1) // 2 : (height + k_height) // 2,
                    (width - k_width - 1) // 2 : (width + k_width) // 2] = neighborhood

        self.rule = rule


    def update(self, num_updates=1):
        for i in range(num_updates):
            convolution = fft_convolve2d(self.board, self.kernal)
            shape = convolution.shape
            new_board = np.zeros(shape)
            new_board[np.where(np.in1d(convolution, self.rule[0]).reshape(shape)
                               & (self.board == 1))] = 1
            new_board[np.where(np.in1d(convolution, self.rule[1]).reshape(shape)
                               & (self.board == 0))] = 1
            self.board = new_board


    def benchmark(self, num_updates):
        start = time.process_time()
        self.update(num_updates)
        print("Performed", num_updates, "updates of", self.board.shape, "took",
              time.process_time() - start, "seconds")


class Conway(Automata):
    def __init__(self, height, width, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[2, 3], [3]]
        Automata.__init__(self, height, width, density, neighborhood, rule)


class Life34(Automata):
    def __init__(self, height, width, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[3, 4], [3, 4]]
        Automata.__init__(self, height, width, density, neighborhood, rule)


class Amoeba(Automata):
    def __init__(self, height, width, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[1, 3, 5, 8], [3, 5, 7]]
        Automata.__init__(self, height, width, density, neighborhood, rule)


class Anneal(Automata):
    def __init__(self, height, width, density):
        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        rule = [[3, 5, 6, 7, 8], [4, 6, 7, 8]]
        Automata.__init__(self, height, width, density, neighborhood, rule)


class Bugs(Automata):
    def __init__(self, height, width, density):
        neighborhood = np.ones((11, 11))
        rule = [np.arange(34, 59), np.arange(34, 46)]
        Automata.__init__(self, height, width, density, neighborhood, rule)


class Animation:
    def __init__(self, automata, interval=100):
        self.automata = automata
        fig = pyplot.figure()
        self.image = pyplot.imshow(self.automata.board, interpolation="nearest",
                                   cmap=pyplot.cm.gray)
        ani = animation.FuncAnimation(fig, self.animate, interval=interval)
        pyplot.show()


    def animate(self, *args):
        self.automata.update()
        self.image.set_array(self.automata.board)
        return self.image,


def main():
    # Create automata
    automata = Anneal(512, 512, density=0.5)
    # automata = Conway(512, 512, density=0.5)

    # Benchmark automata
    # ca.benchmark(100)

    # Animate automata
    Animation(automata, 1)


if __name__ == "__main__":
    main()
