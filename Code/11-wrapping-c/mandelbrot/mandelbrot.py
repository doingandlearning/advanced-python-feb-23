import ctypes
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

lib = ctypes.CDLL('mandelbrot.so')

mandelbrot = lib.mandelbrot

mandelbrot.restype = None
mandelbrot.argtypes = [
	ctypes.c_int,
	ctypes.c_int,
	np.ctypeslib.ndpointer(ctypes.c_int)
]


def generate_mandelbrot(size, iterations):
	col = np.empty((size,size), dtype=np.int32)
	mandelbrot(size, iterations, col)
	fig, ax = plt.subplots(1,1, figsize=(10,10))
	ax.imshow(np.log(col), cmap=plt.cm.hot)
	ax.set_axis_off()
	plt.show()