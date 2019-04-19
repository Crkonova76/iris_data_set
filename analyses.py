# April 2019
# GMIT, Project Iris Data Set

# Imported libraries pandas, numpy, seaborn and matplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris data set from provided url link
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')

# Displaying the the first 5 lines of the data set
with open("output1.txt", 'w') as the_file:
    the_file.write(str(data.head(5)))

print(data.head(5))

# Basic statistics about the whole data set
print(data.describe())
with open("output2.txt", 'wt') as the_file:
    the_file.write(str(data.describe()))

# Basic statistics comparing the sepal length/width and petal length/width
# grouped by the species

grouped = data.groupby('species')
print(grouped.agg([np.mean, np.std, np.min, np.max]))

with open("output3.txt", 'wt') as the_file:
    the_file.write(str(grouped.agg([np.mean])))

with open("output3.txt", 'a') as the_file:
    the_file.write('\n\n' + str(grouped.agg([np.std])))

with open("output3.txt", 'a') as the_file:
    the_file.write('\n\n' + str(grouped.agg([np.min])))

with open("output3.txt", 'a') as the_file:
    the_file.write('\n\n' + str(grouped.agg([np.max])))
'''
# Analyses of Variables-sepal length
# Sepal lenght histogram on the basis of species
#
# data.plot.hist(by = 'petal_length', bins=50)
# plt.show()
'''


#Analysing sepal length and width using scaterplot
#Purpose- to identify the type of relationship between sepal lenght and width
sns.FacetGrid(data, hue="species", height=5).map(plt.scatter, "sepal_length", "sepal_width").add_legend()
plt.show()

#Analysing petal length and width using scaterplot
#Purpose- to identify the type of relationship between petal lenght and width
sns.FacetGrid(data, hue="species", height=5).map(plt.scatter, "petal_length", "petal_width").add_legend()
plt.show()

#corelation between sepal/petal length and width based on species

#plot showing the correlation between species
sns.pairplot(data, hue='species')
plt.show()

#Boxplot used to estimate the distribution of values for each attribute
boxplot = data.boxplot (column=['sepal_length','sepal_width','petal_length','petal_width'])
plt.show()

#Boxplot -distribution of the values considering each species

boxplot = data.boxplot(column=['sepal_length','sepal_width','petal_length','petal_width'],by = 'species')
plt.show()

