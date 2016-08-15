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
    def __init__(self, height, width):
        self.board = np.random.random(width*height).reshape((height, width)).round()
        self.kernal = np.zeros((height, width))

    def benchmark(self, iterations):
        start = time.process_time()
        self.update(iterations)
        print(iterations, "iterations of", ca.board.shape, "took", time.process_time()-start, "seconds")

class Conway(Automata):
    def __init__(self, height, width):
        Automata.__init__(self, height, width)
        self.kernal[height//2-2 : height//2+1, width//2-2 : width//2+1] = np.array([[1,1,1],[1,0,1],[1,1,1]])

    def update(self, iterations=1):
        for i in range(iterations):
            convolution = fft_convolve2d(self.board, self.kernal)
            new_board = np.zeros(convolution.shape)
            new_board[np.where((convolution == 2) & (self.board == 1))] = 1
            new_board[np.where(convolution == 3)] = 1
            self.board = new_board

class Bugs(Automata):
    def __init__(self, height, width):
        Automata.__init__(self, height, width)
        self.kernal[height//2-6 : height//2+5, width//2-6 : width//2+5] = np.ones((11, 11))

    def update(self, iterations=1):
        for i in range(iterations):
            convolution = fft_convolve2d(self.board, self.kernal)
            new_board = np.zeros(convolution.shape)
            new_board[np.where((convolution >= 34) & (convolution <= 58) & (self.board == 1))] = 1
            new_board[np.where((convolution >= 34) & (convolution <= 45))] = 1
            self.board = new_board

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
    # ca = Conway(512, 512)
    ca = Bugs(512, 512)

    # Benchmark automata
    # ca.benchmark(100)

    # Animate automata
    Animation(ca)