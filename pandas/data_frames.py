# Data Frames
import webbrowser

import pandas as pd

website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)

# Read clipboard
data_frame_nba = pd.read_clipboard()

# Copy
# Año 	Campeón del Oeste 	Resultado 	Campeón del Este 	Ref.
# 1951 	Rochester Royals 	4–3 	New York Knicks 	20​
# 1952 	Minneapolis Lakers 	4–3 	New York Knicks 	21​
# 1953 	Minneapolis Lakers† 	4–1 	New York Knicks 	22​
# 1954 	Minneapolis Lakers† 	4–3 	Syracuse Nationals 	23​
# 1955 	Ft. Wayne Pistons 	3–4 	Syracuse Nationals† 	24​
# 1956 	Ft. Wayne Pistons 	1–4 	Philadelphia Warriors† 	25​
# 1957 	St. Louis Hawks 	3–4 	Boston Celtics† 	26​
# 1958 	St. Louis Hawks 	4–2 	Boston Celtics† 	27​
# 1959 	Minneapolis Lakers 	0–4 	Boston Celtics† 	28​
# 1960 	St. Louis Hawks 	3–4 	Boston Celtics† 	29​
# 1961 	St. Louis Hawks 	1–4 	Boston Celtics† 	30​
# 1950 	Minneapolis Lakersn. 2​ 	4–2 	Syracuse Nationals† 	19​18​

print(data_frame_nba)
print(data_frame_nba.columns)
print(data_frame_nba['Campeón del Oeste '])
print(data_frame_nba.loc[5])
print(data_frame_nba.head(6))
print(data_frame_nba.tail(2))

# Data Frame by Dictionary
subject = ['Matematicas', 'Historia', 'Fisica', 'Literatura']
notes = [8, 6, 9, 7]
dictionary = {'Subject': subject, 'Notes': notes}
print(dictionary)

data_frame_notes = pd.DataFrame(dictionary)
print(data_frame_notes)
