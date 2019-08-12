# Rename index

import numpy as np
import pandas as pd

values = np.arange(9).reshape(3, 3)
index = list('abc')
data_frame = pd.DataFrame(values, index=index)
print(data_frame)

new_index = data_frame.index.map(str.upper)
print(new_index)

data_frame.index = new_index
print(data_frame)
print(data_frame.rename(index=str.lower))

new_index2 = {'A': 'f', 'B': 'g', 'C': 'h'}
print(data_frame.rename(index=new_index2))

new_index3 = {'A': 'f'}
data_frame.rename(index=new_index3, inplace=True)
print(data_frame)