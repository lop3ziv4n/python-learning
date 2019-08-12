# Histograms
# Install seaborn: pip2 install seaborn
# https://www.tutorialspoint.com/matplotlib/index.htm
import matplotlib.pyplot as pl
import numpy as np
import seaborn as sns

data1 = np.random.randn(100)
data2 = np.random.randn(80)
data3 = np.random.randn(1000)
data4 = np.random.randn(1000)

pl.hist(data1)
pl.show()

sns.distplot(data1)
pl.show()

sns.distplot(data1, color='green')
pl.show()

pl.hist(data1, color='grey', alpha=0.2)
pl.show()


pl.hist(data2, color='yellow', alpha=0.4)
pl.show()

pl.hist(data1, color='green', alpha=0.3, density=True)
pl.hist(data2, color='blue', alpha=0.3, density=True)
pl.show()


sns.jointplot(data3, data4)
pl.show()

sns.jointplot(data3, data4, kind='hex')
pl.show()