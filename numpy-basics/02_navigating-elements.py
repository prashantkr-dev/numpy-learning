# ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC.

import numpy as np

a = np.array([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13,14]
])
print(a)


## Get a specific element [r,c]
print(a[1,5])


## Get a specific row
print(a[0, :])


## Get a specific column
print(a[:, 2])

# a little more fancy - [startindex:endindex:stepsize]
print(a[0, 1:-1:2])



## Changing element value
a[1, 5] = 20
a[:, 2] = [1, 2]
print(a)


# Get a specific element in 2-D array (work outside in)
b = np.array([[
    [1,2], [3,4]],
    [[5,6], [7,8]]
])
print(b)

print(b[:, 0, 0])
print(b[0, 1, 1])

# Replace an element
b[:, 1, :] = [[9,9], [8,8]]
print(b)