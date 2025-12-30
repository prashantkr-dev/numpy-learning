## MATHEMATICS

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)

b = np.array([1,0,1,0]) 
print(a+b)
print(a**b)

# Take the sin
print(np.sin(a))


## Linear Algebra
a = np.ones((2,3))
print(a)
b = np.full((3,2), 2)
print(b)

# print(a*b) #Error

print(np.matmul(a,b))
# np.matmul() performs matrix multiplication following the rules of linear algebra, not element-wise multiplication.


# Find the determinant
c = np.identity(3)
print(c)
print(np.linalg.det(c))




## Statistics

stats = np.array([[1,2,3], [4,5,6]])
print(np.min(stats))
print(np.min(stats, axis=1))
print(np.max(stats, axis=1))

print(np.sum(stats, axis=0))