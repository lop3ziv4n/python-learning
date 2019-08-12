# Index hierarchy
import numpy as np
import pandas as pd

# Series
value = np.random.randn(6)
# double index
index = [[1, 1, 1, 2, 2, 2], ['a', 'b', 'c', 'a', 'b', 'c']]
series = pd.Series(value, index=index)
print(series)

print(series[1])
print(series[1]['b'])

# Series to Data Frame
data_frame = series.unstack()
print(data_frame)

# Data Frame
value = np.arange(16).reshape(4, 4)
index = list('1234')
columns = list('abcd')

data_frame = pd.DataFrame(value, index=index, columns=columns)
print(data_frame)

# Data Frame to Series
series = data_frame.stack()
print(series)
