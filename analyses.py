, April 2019
# GMIT, Project Iris Data Set

# Imported libraries pandas, numpy, seaborn and matplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris data set from provided url link
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data'
                          '-fa14/gh-pages/data/iris.csv')

# Displaying the the first 5 lines of the data set
print(data.head(5))

# Basic statistics about the whole data set
print(data.describe())

# Basic statistics comparing the sepal length/width and petal length/width
# grouped by the species

grouped = data.groupby('species')
#grouped.agg([np.mean, np.std])
print(grouped.agg([np.mean, np.std, np.min, np.max]))


#Analysing sepal length and width using scaterplot
sns.FacetGrid(data, hue="species", size=5).map(
    plt.scatter, "sepal_length", "sepal_width").add_legend()
plt.show()

#Analysing petal length and width using scaterplot
sns.FacetGrid(data, hue="species", size=5).map(
    plt.scatter, "petal_length", "petal_width").add_legend()
plt.show()



