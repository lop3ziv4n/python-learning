# Operation Arrays (+,-,*,/,**)
import numpy as np

array = np.array([1, 2, 3, 4])

print(array)
print(array * 2)
print(array ** 2)
print(array / 2)
print(array + 4)
print(array - 4)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
double_list = (list1, list2)
double_array = np.array(double_list)
print(double_array)
print(double_array * 2)
print(double_array ** 2)
print(double_array / 2)
print(double_array + 4)
print(double_array - 4)
