# Select data in Data Frame
import numpy as np
import pandas as pd

# Data Frame
print(np.arange(25).reshape(5, 5))
value = np.arange(25).reshape(5, 5)
index = ['i1', 'i2', 'i3', 'i4', 'i5']
columns = ['c1', 'c2', 'c3', 'c4', 'c5']

data_frame = pd.DataFrame(value, index=index, columns=columns)
print(data_frame)

# Columns
print(data_frame['c2'])
print(data_frame[['c2', 'c4']])
print(data_frame[['c2', 'c3', 'c4']])
# Columns - Index
print(data_frame['c2']['i2'])
# Condition
print(data_frame[data_frame['c2'] > 15])
print(data_frame > 20)
# Index
print(data_frame.loc['i2'])
print(data_frame.loc['i2']['c4'])
