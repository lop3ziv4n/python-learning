# Create Arrays - Module Numpy
import numpy as np

print(np.zeros(4))

print(np.ones(4))

print(np.arange(4))

print(np.arange(10))

print(np.arange(2, 20, 3))

lists = [1, 2, 3, 4]
arrays = np.array(lists)
print(arrays)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
double_list = (list1, list2)
print(double_list)

double_array = np.array(double_list)
print(double_array)

print(double_array.shape)  # 2 file 4 columns
print(double_array.dtype)  # type
