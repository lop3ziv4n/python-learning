# Delete Series and Data Frame
import numpy as np
import pandas as pd

# Series
index = ['a', 'b', 'c', 'd']
series = pd.Series(np.arange(4), index=index)
print(series)
print(series.drop('c'))

# Data Frame
print(np.arange(9).reshape(3, 3))
value = np.arange(9).reshape(3, 3)
index = ['a', 'b', 'c']
columns = ['c1', 'c2', 'c3']

data_frame = pd.DataFrame(value, index=index, columns=columns)
print(data_frame)

print(data_frame.drop('b'))
print(data_frame.drop('c2', axis=1))
