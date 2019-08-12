# Value nulls - NaN
import numpy as np
import pandas as pd

# Series
value = ['1', '2', np.nan, '4']
index = list('adcb')
series = pd.Series(value, index=index)
print(series)

print(series.isnull())
print(series.dropna())

# Data Frame
value = np.array([[1, 2, 3], [4, np.nan, 5], [6, 7, np.nan]])
index = list('123')
columns = list('abc')

data_frame = pd.DataFrame(value, index=index, columns=columns)
print(data_frame)

print(data_frame.isnull())
print(data_frame.dropna())
print(data_frame.fillna(0))
