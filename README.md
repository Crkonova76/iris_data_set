# Iris-data-set

## Iris-data set introduction

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936.
The data set consists of 50 samples from each of three species -Iris setosa, Iris virginica and Iris versicolor. 
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 


## Libraries

* Pandas - a data processing and CSV file I/O library
* Seaborn- a Python graphing library
* Matplotlib- a Python 2D plotting library
* Numpy-a fundamental package for scientific computing with Python

## Statistics methods used:

### *Mean*
* The "average" number, found by adding all data points and dividing by by the number of data points
>reference: https://www.khanacademy.org/math/statistics-probability/>summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review

### *Standard Deviation*
* Quantifies the amount of variation or dispersion of a set of data values.A low standard deviation indicates that the data points tend to be close to the mean (also called the expected value) of the set, while a high standard deviation indicates that the data points are spread out over a wider range of values.
>reference: https://en.wikipedia.org/wiki/Standard_deviation

### *Minimum , Maximum , Range*

### *Corelation*

### *Boxplot*
* Interpretation of Boxplot on the picture below:
![boxplot](https://user-images.githubusercontent.com/47481671/56097809-1d1bc800-5ef1-11e9-97ab-1299a0767349.JPG)

## Interpretation of the data set results

1, Iris data set is loaded as csv file from  https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

2, Head() function is used to display first 5 items of the data set.

3, The basic features of the data set is described by using the function describe(). The output can be seen below:

!

4, To get better understanding of the sepal lenght / width and petal lenght / width the mean, standard deviation, minimum and maximum is calculated for each species separatelly. Refer below to the output 3.

!

* **Sepal Lenght** - the average lenght is 5.84 cm, virginica has the longest sepal from all 3 species (average 6.6 cm). Virginica has the highets range (3cm) when the minimum and maximum values are compared (Setosa-1.5cm and Versicolor-2.1cm). This is supported by the standard deviation, which shows that the virginica's values are more spread from the average as the other two species. In overall the standard deviation of sepal lenght is highest from all standard deviations across the atributes of the dataset (regardles of the species).

**Sepal Width** - the average width is 3.05 cm. Out of all species Setosa-the only one with higher mean as mean calculated for all three species- has the longest average sepal width (3.42 cm). Setosa has the highest difference between the maximum and minimum value (2.1 cm), comparing to virginica's range at 1.6 cm and versicolor's range at 1.4 cm. Calculated standard deviations is highest for setosa species which reflects to the range between maximum/minimum values calculation.

**Petal Lenght** - the average lenght is 3.76 cm, with virginica's mean as the highest value out of all three species. Virginica's standard deviation is highest comparing to other two species, which is reflected in the highest range in the values between the maximum and minimum values (2.4 cm)-(versicolor 2.1cm and setosa 0.9 cm)

**Petal Width** - the average width is 1.2 cm. Based on the grouped calculation we can see that setosa is the main driver of lowering the overall average petal width, with the average value significantly below the total average. Versicolor and virnica's average value is above the average of the three species. Virginica's standard deviations is highest comparing the other two species.
