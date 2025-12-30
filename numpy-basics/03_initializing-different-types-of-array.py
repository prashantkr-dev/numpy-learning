## INITIALIZING DIFFERENT TYPES OF ARRAYS

import numpy as np

# All 0s matrix
a = np.zeros((2, 3, 3, 2))
print(a)

# All 1s matrix 
b = np.ones((4, 2, 2), dtype='int32')
print(b)

# Any other number
c = np.full((2,2), 99)
print(c)

# Any other number (full_like)
d = np.full_like(a, 4)
print(d)



# Random decimal numbers
e = np.random.rand(4, 2)
print(e)

# Random integer numbers
f = np.random.randint(7, size = (3,3)) 
print(f) #3*3 array of random number 0-7



g = np.identity(5)
print(g)

# Repeat an array
h = np.array([1, 2, 3])
r1 = np.repeat(h, 3)
print(r1)
