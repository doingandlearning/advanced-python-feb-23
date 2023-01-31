from functools import partial

multiple = lambda x,y: x*y

times2 = partial(multiple, 2)
times5 = partial(multiple, 5)