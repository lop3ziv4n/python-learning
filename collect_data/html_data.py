# HTML con python
import pandas as pd

website = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

data_frame = pd.io.html.read_html(website)
print(data_frame)

data_frame_soccer = data_frame[0]
print(data_frame_soccer)