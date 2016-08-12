from numpy.fft import fft2, ifft2, fftshift
from matplotlib import pyplot
import numpy as np
import time

pyplot.ion()

def fft_convolve2d(x,y):
    fr = fft2(x)
    fr2 = fft2(np.flipud(np.fliplr(y)))
    m,n = fr.shape
    cc = np.real(ifft2(fr*fr2))
    cc = np.roll(cc, - int(m / 2) + 1, axis=0)
    cc = np.roll(cc, - int(n / 2) + 1, axis=1)
    return cc

class Conway:
    def __init__(self, width, height):
        self.board = np.random.random(width*height).reshape((width, height)).round()
        self.kernal = np.zeros((width, height))
        self.kernal[width/2-1 : width/2+2, height/2-1 : height/2+2] = np.array([[1,1,1],[1,0,1],[1,1,1]])

    def update(self):
        convolution = fft_convolve2d(self.board, self.kernal).round()
        new_board = np.zeros(convolution.shape)

        new_board[np.where((convolution == 2) & (self.board == 1))] = 1
        new_board[np.where((convolution == 3) & (self.board == 1))] = 1
        new_board[np.where((convolution == 3) & (self.board == 0))] = 1
        self.board = new_board

if __name__ == "__main__":
    conway = Conway(1024, 1024)
    pyplot.figure()
    img_plot = pyplot.imshow(conway.board, interpolation="nearest", cmap = pyplot.cm.gray)
    while True:
        conway.update()
        img_plot.set_data(conway.board)
        pyplot.pause(0.0001)