# Heat Map
import matplotlib.pyplot as pl
import seaborn as sns

flights = sns.load_dataset('flights')
print(flights.head(10))

flights = flights.pivot('month', 'year', 'passengers')
print(flights.head(10))

sns.heatmap(flights)
pl.show()

sns.heatmap(flights, annot=True, fmt='d')
pl.show()

center_value = flights.loc['May'][1956]
print(center_value)

sns.heatmap(flights, center=center_value, annot=True, fmt='d')
pl.show()

sns.heatmap(flights, center=center_value, annot=True, fmt='d', cbar_kws={'orientation': 'horizontal'})
pl.show()
