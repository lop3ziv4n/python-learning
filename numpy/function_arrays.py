# Function in Arrays
import numpy as np

arrays = np.arange(5)
print(np.sqrt(arrays))

arrays_random = np.random.rand(5)
print(arrays_random)
print(np.random.rand(5))

arrays1 = np.arange(5)
arrays2 = np.array([5, 6, 7, 8, 9])
print(np.add(arrays1, arrays2))
print(np.subtract(arrays1, arrays2))
print(np.maximum(arrays1, arrays2))
