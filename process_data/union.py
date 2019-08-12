# Union Data Frame
import pandas as pd

data_frame1 = pd.DataFrame({'c1': ['1', '2', '3'], 'c3': ['a', 'b', 'c']})
print(data_frame1)

data_frame2 = pd.DataFrame({'c2': ['4', '5', '6'], 'c3': ['c', 'b', 'e']})
print(data_frame2)

data_frame3 = pd.DataFrame.merge(data_frame1, data_frame2)
print(data_frame3)

data_frame3 = pd.DataFrame.merge(data_frame1, data_frame2, on='c3')
print(data_frame3)

data_frame3 = pd.DataFrame.merge(data_frame1, data_frame2, on='c3', how='left')
print(data_frame3)

data_frame3 = pd.DataFrame.merge(data_frame1, data_frame2, on='c3', how='right')
print(data_frame3)

data_frame3 = pd.DataFrame.merge(data_frame1, data_frame2, on='c3', how='outer')
print(data_frame3)