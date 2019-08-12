# Input and output of Arrays
import numpy as np

arrays = np.arange(6)
print(arrays)

# Save arrays
np.save('arrays', arrays)

load_arrays = np.load('arrays.npy')
print(load_arrays)

arrays1 = np.arange(6)
arrays2 = np.arange(8)
np.savez('arrays', x=arrays1, y=arrays2)

load_arrays = np.load('arrays.npz')
print(load_arrays)
print(load_arrays['x'])
print(load_arrays['y'])

np.savetxt('file_array.txt', arrays, delimiter=',')
load_arrays = np.loadtxt('file_array.txt', delimiter=',')
print(load_arrays)