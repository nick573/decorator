# Filename: decorator.py

import time

def timeit(f):
	def wrap(*args):
		time_start = time.time()
		ret = f(*args)
		time_end = time.time()
		print('%s %0.3f ms' % (f.__name__, (time_end - time_start) * 1000.0))
		return ret
	return wrap

# sum -- функция, время которой измеряется
@timeit
def sum(arr):
	total = 0
	for x in arr:
		total += x
	return total
print(sum([1, 2, 3, 4]))	