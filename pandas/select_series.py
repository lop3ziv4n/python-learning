# Select data in the series
import numpy as np
import pandas as pd

# Series
index = ['i1', 'i2', 'i3', 'i4']
series = pd.Series(np.arange(4), index=index)
print(series)

series = series * 2
print(series)

# Value
print(series[2])
print(series[0:2])
# Index
print(series['i2'])
print(series['i1':'i3'])
# Condition
print(series[series > 3])
