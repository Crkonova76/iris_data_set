# Martina Crkonova, April 2019
# GMIT, Project Iris Data Set
# libraries panda and numpy

import pandas as pd
import numpy as np
import matplotlib as mt

data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data'
                          '-fa14/gh-pages/data/iris.csv')

# Basic statistics
print(data.describe())

print(data.corr())

# Basic statistics by the species

grouped = data.groupby('species')
grouped.agg([np.mean, np.std, np.min, np.max])
print(grouped.agg([np.mean, np.std, np.min, np.max]))

