import numpy as np

def process_marks(m):
	print('\nExam marks\n',  m)
	print('All passes?',  np.all(m >= 50))
	print('ANy passes?',  np.any(m >= 50))
	print('Count of passes?',  np.count_nonzero(m >= 50))
	print('Count of B?',  np.count_nonzero((m >= 60) & (m<70)))

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)