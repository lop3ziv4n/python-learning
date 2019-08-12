# Combine elements
import numpy as np
import pandas as pd

values = np.arange(25).reshape(5, 5)

data_frame = pd.DataFrame(values)
print(data_frame)

values_random = np.random.permutation(5)
print(values_random)

print(data_frame.take(values_random))
