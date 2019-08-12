# Statistics in data frames
import numpy as np
import pandas as pd

# Data Frame
value = np.array([[1, 8, 3], [5, 6, 7]])
index = list('ab')
columns = list('123')

data_frame = pd.DataFrame(value, index=index, columns=columns)
print(data_frame)

# Columns
print(data_frame.sum())
print(data_frame.min())
print(data_frame.max())
# Index
print(data_frame.sum(axis=1))
print(data_frame.min(axis=1))
print(data_frame.max(axis=1))

# Min - Max for index
data_frame.idxmin()
data_frame.idxman()

# Describe operations
data_frame.describe()
