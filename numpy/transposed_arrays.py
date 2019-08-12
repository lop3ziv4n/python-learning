# Arrays o transposed matrix
import numpy as np

# Array 0 - 15 elements / 3 rows and 5 columns
arrays = np.arange(15).reshape((3, 5))
print(arrays)
print(arrays[1][1])

# transposed
trans_arrays = arrays.T
print(trans_arrays)
