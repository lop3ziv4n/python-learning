# Index Arrays
import numpy as np

arrays = np.arange(0, 11)
print(arrays)

# position initial and position final
print(arrays[0:3])
print(arrays[2:5])
print(arrays[:])

copy_arrays = arrays.copy()
print(copy_arrays)
print(arrays)

copy_arrays[0:3] = 20
print(copy_arrays)
print(arrays)

arrays2 = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(arrays2)
# position row and column
print(arrays2[1])
print(arrays2[1][2])
print(arrays2[0][0])
