# Filter data in Data Frames
import numpy as np
import pandas as pd

values = np.random.rand(10, 3)

data_frame = pd.DataFrame(values)
print(data_frame)

column = data_frame[0]
print(column)
print(column[column > 0.40])

print(data_frame[data_frame > 0.40])
