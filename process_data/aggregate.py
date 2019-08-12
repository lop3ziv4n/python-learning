# Add (operation)
import numpy as np
import pandas as pd

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [np.nan, np.nan, np.nan]]
columns = list('abc')

data_frame = pd.DataFrame(values, columns=columns)
print(data_frame)

print(data_frame.agg(['sum', 'min', 'max']))
print(data_frame.agg('sum', axis=1))
