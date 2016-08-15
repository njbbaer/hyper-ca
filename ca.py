from matplotlib import pyplot, animation
from numpy.fft import fft2, ifft2
import numpy as np
import time

def fft_convolve2d(board, kernal):
    fr = fft2(board)
    fr2 = fft2(kernal)
    m,n = fr.shape
    cc = np.real(ifft2(fr*fr2))
    cc = np.roll(cc, - int(m / 2) + 1, axis=0)
    cc = np.roll(cc, - int(n / 2) + 1, axis=1)
    return cc.round()

class Automata:
    def __init__(self, height, width, neighborhood, rule):
        self.board = np.random.random(width*height).reshape((height, width)).round()

        k_height, k_width = neighborhood.shape
        self.kernal = np.zeros((height, width))
        self.kernal[(height - k_height - 1) // 2 : (height + k_height) // 2, 
                (width - k_width - 1) // 2 : (width + k_width) // 2] = neighborhood

        self.rule = rule

    def update(self, iterations=1):
        for i in range(iterations):
            convolution = fft_convolve2d(self.board, self.kernal)
            shape = convolution.shape
            new_board = np.zeros(shape)
            new_board[np.where(np.in1d(convolution, self.rule[0]).reshape(shape) & (self.board == 0))] = 1
            new_board[np.where(np.in1d(convolution, self.rule[1]).reshape(shape) & (self.board == 1))] = 1
            self.board = new_board

    def benchmark(self, iterations):
        start = time.process_time()
        self.update(iterations)
        print(iterations, "iterations of", ca.board.shape, "took", time.process_time()-start, "seconds")

class Conway(Automata):
    def __init__(self, height, width):
        neighborhood = np.array([[1,1,1],[1,0,1],[1,1,1]])
        rule = [[3], [2, 3]]
        Automata.__init__(self, height, width, neighborhood, rule)

class Bugs(Automata):
    def __init__(self, height, width):
        neighborhood = np.ones((11, 11))
        rule = [np.arange(34, 46), np.arange(34, 59)]
        Automata.__init__(self, height, width, neighborhood, rule)

class Animation:
    def __init__(self, ca, interval=100):
        self.ca = ca
        fig = pyplot.figure()
        self.image = pyplot.imshow(self.ca.board, interpolation="nearest", cmap=pyplot.cm.gray)
        ani = animation.FuncAnimation(fig, self.animate, interval=interval)
        pyplot.show()

    def animate(self, *args):
        self.ca.update()
        self.image.set_array(self.ca.board)
        return self.image,

if __name__ == "__main__":
    # Create automata
    ca = Bugs(512, 512)
    # ca = Conway(512, 512)

    # Benchmark automata
    # ca.benchmark(100)

    # Animate automata
    Animation(ca)