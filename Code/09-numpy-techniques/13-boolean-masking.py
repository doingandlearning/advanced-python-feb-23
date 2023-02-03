import numpy as np


def process_marks(m):
	print('Passes?', m[m >= 50])
	print('B marks?', m[(m >= 60) & (m <70)])


my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)


our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 23, 78, 88, 92]])
process_marks(our_exam_marks)
