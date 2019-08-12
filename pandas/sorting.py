# Sorting Series
import numpy as np
import pandas as pd

# Series
series = pd.Series(range(4), index=list('CABD'))
print(series)

# Sort Index
print(series.sort_index())
# Sort Value
print(series.sort_values())
# Rank position
series2 = pd.Series(np.random.randn(10))
print(series2)
print(series2.rank())
