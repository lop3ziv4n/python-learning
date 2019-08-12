# Group data in category
import pandas as pd

prices = [42, 55, 48, 23, 5, 21, 88, 34, 26]
ranges = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

prices_ranges = pd.cut(prices, ranges)
print(prices_ranges)

# count for range
print(pd.value_counts(prices_ranges))
