import numpy as np

# ---------- Q1 ------------
# Print the following array:
#  [1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]


arr = np.ones((5, 5))
print(arr)

z = np.zeros((3, 3))
z[1,1] = 9
print(z)

arr[1:-1, 1:-1] = z
print(arr)