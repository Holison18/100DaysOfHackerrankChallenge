import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    # return the reverse of the array
    return np.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
