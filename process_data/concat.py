# Concat Arrays, Series, Data Frames
import numpy as np
import pandas as pd

# Array
array = np.arange(9).reshape(3, 3)
print(array)

print(np.concatenate([array, array]))
print(np.concatenate([array, array], axis=1))

# Series
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5, 6], index=['d', 'e', 'f'])
print(series1)
print(series2)

print(pd.concat([series1, series2]))
print(pd.concat([series1, series2], keys=['series1', 'series2']))

# Data Frame
data_frame1 = pd.DataFrame(np.random.rand(3, 3), columns=['a', 'b', 'c'])
data_frame2 = pd.DataFrame(np.random.rand(2, 3), columns=['a', 'b', 'c'])
print(data_frame1)
print(data_frame2)

print(pd.concat([data_frame1, data_frame2]))
print(pd.concat([data_frame1, data_frame2], ignore_index=True))
