# Index Series and Data Frame
import pandas as pd

# Series
value = [1, 2, 3]
index = ['a', 'b', 'c']
series = pd.Series(value, index=index)
print(series)
print(series.index)
print(series.index[0])

# Data Frame
subject = ['Matematicas', 'Historia', 'Fisica', 'Literatura']
notes = [[8, 6, 4, 7], [8, 6, 9, 4], [7, 6, 7, 7], [7, 6, 7, 7]]
persons = ['Antonio', 'Maria', 'Pedro', 'Jose']

data_frame_notes = pd.DataFrame(notes, index=subject, columns=persons)
print(data_frame_notes)
print(data_frame_notes.index)
print(data_frame_notes.index[2])
