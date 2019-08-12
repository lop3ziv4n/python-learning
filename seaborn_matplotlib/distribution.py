# Combination of styles
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import seaborn as sns

data1 = np.random.randn(100)

sns.distplot(data1, color='green')
pl.show()

sns.distplot(data1, color='green', rug=False, hist=False)
pl.show()

arg_curve = {'color': 'black', 'label': 'Curva'}
arg_histogram = {'color': 'grey', 'label': 'Histograma'}
sns.distplot(data1, bins=25, kde_kws=arg_curve, hist_kws=arg_histogram)
pl.show()

# Series
series = pd.Series(data1)
sns.distplot(series, bins=25, color='green')
pl.show()
