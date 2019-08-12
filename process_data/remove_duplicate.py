# Remove duplicate Data Frame
import pandas as pd

values = [[1, 2], [1, 2], [5, 6], [5, 8]]
index = list('mnop')
columns = ['value1', 'value2']

data_frame = pd.DataFrame(values, index=index, columns=columns)
print(data_frame)

print(data_frame.duplicated())
print(data_frame.drop_duplicates())
print(data_frame.drop_duplicates(['value1']))
print(data_frame.drop_duplicates(['value1'], keep='last'))
