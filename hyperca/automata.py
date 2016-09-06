import time
import numpy as np
import png
import reikna.cluda
import reikna.fft
from matplotlib import pyplot, animation


class Automata:

    def __init__(self, neighborhood, rule):
        self.neighborhood = neighborhood

        get_ints = lambda x: [i for i in x if isinstance(i, int)]
        self.rule_ints = (get_ints(rule[0]), get_ints(rule[1]))
        get_ranges = lambda x: [i for i in x if not isinstance(i, int)]
        self.rule_ranges = (get_ranges(rule[0]), get_ranges(rule[1]))


    def init_board(self, board):
        self.board = np.array(board, dtype=np.float32)
        self._calculate_kernal_ft()


    def init_board_populate(self, shape, density):
        self.board = np.random.uniform(size=shape) < density
        self.board = self.board.astype(np.float32)
        self._calculate_kernal_ft()


    def _calculate_kernal_ft(self):
        neighborhood = np.array(self.neighborhood)
        kernal = np.zeros(self.board.shape)

        n_height, n_width = neighborhood.shape
        b_height, b_width = self.board.shape

        kernal[(b_height - n_height - 1) // 2 : (b_height + n_height) // 2,
               (b_width - n_width - 1) // 2 : (b_width + n_width) // 2] = self.neighborhood
        self.kernal_ft = np.fft.fft2(kernal)


    def update(self, iterations=1):
        for i in range(iterations):
            convolution = self._convolve2d()
            shape = convolution.shape
            new_board = np.zeros(shape)

            new_board[np.where(np.in1d(convolution, self.rule_ints[0]).reshape(shape)
                             & (self.board == 1))] = 1
            new_board[np.where(np.in1d(convolution, self.rule_ints[1]).reshape(shape)
                               & (self.board == 0))] = 1
            for rule_range in self.rule_ranges[0]:
                new_board[np.where((self.board == 1)
                                   & (convolution >= rule_range[0]) 
                                   & (convolution <= rule_range[1]))] = 1
            for rule_range in self.rule_ranges[1]:
                new_board[np.where((self.board == 0)
                                   & (convolution >= rule_range[0]) 
                                   & (convolution <= rule_range[1]))] = 1
            self.board = new_board.astype(int)
            
            
    def _convolve2d(self):
        board_ft = np.fft.fft2(self.board)
        convolution = np.fft.ifft2(board_ft * self.kernal_ft)
        height, width = board_ft.shape
        convolution = np.roll(convolution, - int(height / 2) + 1, axis=0)
        convolution = np.roll(convolution, - int(width / 2) + 1, axis=1)
        return convolution.round()


    def benchmark(self, iterations):
        start = time.process_time()
        self.update(iterations)
        delta = time.process_time() - start
        rate = (iterations * self.board.size / delta) * 0.000001
        print(iterations, "iterations of", self.board.shape, "cells in",
              "%.2f"%delta, "seconds at", "%.2f"%rate, "megacells per second")


    def animate(self, fps=10, filename=None):
        
        def refresh(*args):
            self.update()
            image.set_array(self.board)
            return image,

        figure = pyplot.figure()
        image = pyplot.imshow(self.board, interpolation="nearest",
                              cmap=pyplot.cm.gray)
        anim = animation.FuncAnimation(figure, refresh, interval=1000/fps)

        if filename:
            writer = animation.FFMpegWriter()
            anim.save(filename, writer=writer)

        pyplot.show()


    def save_png(self, filename):
        file = open(filename, 'wb')
        writer = png.Writer(self.board.shape[1], self.board.shape[0], greyscale=True)
        writer.write(file, self.board*255)
        file.close()
        

class Automata_GPU(Automata):

    def __init__(self, neighborhood, rule):
        super().__init__(neighborhood, rule)


    def _convolve2d(self):

        def _fft2d_gpu(array, thread, is_inverse=False):
            array_complex = array.astype(np.complex64)

            board_device = thread.to_device(array_complex)
            result_device = thread.array(array.shape, dtype=np.complex64)

            fft = reikna.fft.FFT(array_complex, axes=(0, 1))

            fft_complied = fft.compile(thread)
            fft_complied(result_device, board_device, inverse=is_inverse)

            return result_device.get()


        api = reikna.cluda.any_api()
        thread = api.Thread.create()

        board_ft = _fft2d_gpu(self.board, thread)

        convolution = _fft2d_gpu(board_ft * self.kernal_ft, thread, True)
        height, width = board_ft.shape
        convolution = np.roll(convolution, - int(height / 2) + 1, axis=0)
        convolution = np.roll(convolution, - int(width / 2) + 1, axis=1)
        return convolution.round()