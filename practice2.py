# list- [], different data types allowed, append, sort, reverse, insert, remove, pop
# tuple- (), immutable list
x = [1, 2, 3]
y = (4, 5, 6)
print(2 * x)
x.append(5)
x.reverse()
print(x)
x.sort(reverse=True)
print(x)

import numpy as np
a = np.array([1, 2, 3])
print(a)
a = a * 4
print(a)
b = np.zeros((2,2), int)
print(b)
