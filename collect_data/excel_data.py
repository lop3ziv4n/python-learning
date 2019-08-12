# EXCEL con python
import pandas as pd

excel_file = pd.ExcelFile('file_excel.xlsx')

data_frame = excel_file.parse('Hoja1')
print(data_frame)