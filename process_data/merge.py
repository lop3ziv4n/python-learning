# Merge Series and Data Frame
import numpy as np
import pandas as pd

# Series
series1 = pd.Series([1, 2, np.nan])
series2 = pd.Series([4, 5, 6])
print(series1)
print(series2)

print(series1.combine_first(series2))

# Data Frame
data_frame1 = pd.DataFrame([1, 2, np.nan])
data_frame2 = pd.DataFrame([4, 5, 6, 7])
print(data_frame1)
print(data_frame2)

print(data_frame1.combine_first(data_frame2))
