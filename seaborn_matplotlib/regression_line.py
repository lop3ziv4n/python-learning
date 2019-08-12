# Regression Line
import matplotlib.pyplot as pl
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head(10))

sns.lmplot('total_bill', 'tip', tips)
pl.show()

sns.lmplot('total_bill', 'tip', tips, scatter_kws={'color': 'green'}, line_kws={'color': 'blue'})
pl.show()

sns.lmplot('total_bill', 'tip', tips, fit_reg=False)
pl.show()

tips['percent'] = 100 * tips['tip'] / tips['total_bill']
print(tips.head(10))
sns.lmplot('size', 'percent', tips)
pl.show()

sns.lmplot('total_bill', 'percent', tips, hue='sex', markers=['x', 'o'])
pl.show()

sns.lmplot('total_bill', 'percent', tips, hue='day')
pl.show()
