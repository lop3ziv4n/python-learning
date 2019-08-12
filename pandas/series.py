# Series
import pandas as pd

# list index
series = pd.Series([3, 5, 7])
print(series)
print(series[1])

subject = ['Matematicas', 'Historia', 'Fisica', 'Literatura']
notes = [8, 6, 9, 7]
series_notes = pd.Series(notes, index=subject)
print(series_notes)
print(series_notes['Fisica'])
print(series_notes[series_notes >= 8])

# Names
series_notes.name = 'Notas por Asignatura'
series_notes.index.name = 'Asignaturas'
print(series_notes)

# convert series to dictionary
dictionary = series_notes.to_dict()
print(dictionary)
# convert dictionary to series
series_convert = pd.Series(dictionary)
print(series_convert)

subject = ['Matematicas', 'Historia', 'Fisica', 'Literatura']
notes = [7, 8, 5, 9]
series_notes2 = pd.Series(notes, index=subject)
print(series_notes2)

series_notes_med = (series_notes + series_notes2) / 2
print(series_notes_med)
