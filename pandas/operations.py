# Operations Series and Data Frame
import numpy as np
import pandas as pd

# Series
series1 = pd.Series(np.arange(3), index=['a', 'b', 'c'])
print(series1)
series2 = pd.Series(np.arange(3, 7), index=['a', 'b', 'c', 'd'])
print(series2)

print(series1 + series2)

# Data Frame
value = np.arange(4).reshape(2, 2)
index = list('ab')
columns = list('12')

data_frame1 = pd.DataFrame(value, index=index, columns=columns)
print(data_frame1)

value = np.arange(9).reshape(3, 3)
index = list('abc')
columns = list('123')

data_frame2 = pd.DataFrame(value, index=index, columns=columns)
print(data_frame2)

print(data_frame1 + data_frame2)
# Replace 0 columns null
print(data_frame1.add(data_frame2, fill_value=0))
