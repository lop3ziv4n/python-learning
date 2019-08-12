# Replace Series
import pandas as pd

series = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
print(series)

print(series.replace(1, 6))
print(series.replace({2: 8, 3: 9}))
