# Iris-data-set

This repository contains my solution to the Project _IRIS DATA SET_ for the module Programming and Scripting, at GMIT.

Refer here for the instructions https://github.com/ianmcloughlin/project-pands/blob/master/project.pdf

## Iris-data set introduction

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936.
The data set consists of 50 samples from each of three species -Iris setosa, Iris virginica and Iris versicolor. 

![irises](https://user-images.githubusercontent.com/47481671/56443288-e62c2480-62eb-11e9-9ad4-a4dc907a81b4.png)

Four features were measured (in cm) from each sample:

Petal length
Petal width 
Sepal length 
Sepal width 

![Sepal and petal](https://user-images.githubusercontent.com/47481671/56443313-08be3d80-62ec-11e9-933b-0810c5c33051.jpg)

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
*In statistics, the range is a measure of spread. It’s defined as the difference between the highest value (Maximum)  and the lowest value (Minimum) in a data set.
>refernce: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/statistics-definitions/range-statistics/

### *Boxplot*
* A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”).
reference: https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51

* Interpretation of Boxplot on the picture below:
![boxplot](https://user-images.githubusercontent.com/47481671/56097809-1d1bc800-5ef1-11e9-97ab-1299a0767349.JPG)

## Interpretation of the data set results

1, Iris data set is loaded as csv file from  https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

2, Head() function is used to display first 5 items of the data set.

3, The basic features of the data set is described by using the function describe(). The output can be seen below:

![output2](https://user-images.githubusercontent.com/47481671/56411071-66647280-6277-11e9-903d-c165fda1f98f.JPG)

4, To get better understanding of the sepal lenght / width and petal lenght / width the mean, standard deviation, minimum and maximum is calculated for each species separatelly. Refer below to the output 3.

![Output3](https://user-images.githubusercontent.com/47481671/56443403-6e122e80-62ec-11e9-880c-58ee3daa40c4.JPG)

* **Sepal Lenght** - the average lenght is 5.84 cm, virginica has the longest sepal from all 3 species (average 6.6 cm). Virginica has the highets range (3cm) when the minimum and maximum values are compared (Setosa-1.5cm and Versicolor-2.1cm). This is supported by the standard deviation, which shows that the virginica's values are more spread from the average as the other two species. In overall the standard deviation of sepal lenght is highest from all standard deviations across the atributes of the dataset (regardles of the species).

* **Sepal Width** - the average width is 3.05 cm. Out of all species Setosa-the only one with higher mean as mean calculated for all three species- has the longest average sepal width (3.42 cm). Setosa has the highest difference between the maximum and minimum value (2.1 cm), comparing to virginica's range at 1.6 cm and versicolor's range at 1.4 cm. Calculated standard deviations is highest for setosa species which reflects to the range between maximum/minimum values calculation.

* **Petal Lenght** - the average lenght is 3.76 cm, with virginica's mean as the highest value out of all three species. Virginica's standard deviation is highest comparing to other two species, which is reflected in the highest range in the values between the maximum and minimum values (2.4 cm)-(versicolor 2.1cm and setosa 0.9 cm)

* **Petal Width** - the average width is 1.2 cm. Based on the grouped calculation we can see that setosa is the main driver of lowering the overall average petal width, with the average value significantly below the total average. Versicolor and virnica's average value is above the average of the three species. Virginica's standard deviations is highest comparing the other two species.

5, To support the calculations in the point 4, the scaterplot is used as a tool to identify the relationship between variables. In first ocassion the plot group the sepal lenght and sepal width by species, and petal lenght and petal width by species in the second plot. 

* The sepal width/lenght of setosa is distinguished from other two species by having wider but shorter sepals.This is supported by the calculation when the average lenght in cm is smallest value but the average widht of setosa is highest value in comparison to other two species.

![Plot 1](https://user-images.githubusercontent.com/47481671/56443473-bcbfc880-62ec-11e9-8476-87436815820f.png)

* The scaterplot of petal lenght and width is manifesting that species setosa lenght and width is not related to the lenght and width of other two species.


![Plot 2 Petal_1](https://user-images.githubusercontent.com/47481671/56443481-cb0de480-62ec-11e9-9477-010be3003425.png)

6, Seaborn pairplot helps to visualize the relationship between pairs of features.The Iris Setosa species are very easily separable from rest of data (species versicolor and virginica), which is supporting the findings above.

![Plot 3 both variables](https://user-images.githubusercontent.com/47481671/56443503-e0830e80-62ec-11e9-8f07-e072d454e5b3.png)

7, Boxplot is used to display how the values are spread out. The values in petal lenght and width are more represented in lower quartel. This anomaly is caused by species setosa as the values are have lower value of both variables (width and length) compared to other two species. 

![Boxplot overall](https://user-images.githubusercontent.com/47481671/56443549-1627f780-62ed-11e9-9b2f-d0ab52b5c0de.png)

Boxplot used for each of the species is displayed below:

![Boxplot by species](https://user-images.githubusercontent.com/47481671/56443568-2c35b800-62ed-11e9-966e-c2a14df309ea.png)
