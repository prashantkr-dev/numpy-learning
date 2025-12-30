import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([
    [9.0, 8.0, 7.0],
    [6.0, 5.0, 4.0]
])
print(b)


## Get Dimension
# ndim - number of dimensions of an array. it tells how many axes the array has. 
print(a.ndim)
print(b.ndim)

## Get Shape
# array.shape - returns the structure of the array, how many elements exist along each dimension (axis).
print(a.shape)
print(b.shape)

## Get Type
# array.dtype - tells the data type of elements stored in an array.
print(a.dtype)
print(b.dtype)

## Get Size
# array.itemsize - tells how many bytes a single element of the array occupies in memory. It is directly determined by the array’s dtype.
print(a.itemsize)
print(b.itemsize)

## Get Total Size 
# array.size - returns the total number of elements in array.
print(a.size)
print(b.size)

# array.nbytes - tells the total memory (in bytes) consumed by the array.
print(a.nbytes)
print(b.nbytes)


# comparing .size, .itemsize, .nbytes
print(a.size)    # 3 elements
print(a.itemsize)  # 8 bytes per element
print(a.nbytes)  # total memory = 8*3 = 24
# a.nbytes = a.size * a.itemsize

