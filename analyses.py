# Martina Crkonova, April 2019
# GMIT, Project Iris Data Set
# libraries panda and numpy

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')

# Basic statistics
print(data.describe())

print(data.corr())

