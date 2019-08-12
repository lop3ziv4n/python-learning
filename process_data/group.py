# Group in Data Frames
import numpy as np
import pandas as pd

values = {'key1': ['x', 'x', 'y', 'y', 'z'], 'key2': ['a', 'b', 'a', 'b', 'a'], 'data1': np.random.rand(5),
          'data2': np.random.rand(5)}

data_frame = pd.DataFrame(values)
print(data_frame)

group = data_frame['data1'].groupby(data_frame['key1'])
print(group.mean())
print(group.max())
