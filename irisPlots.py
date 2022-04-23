# Playing with Iris Plots

# Author: Brendan Heeney

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')


plt.subplot(2,2,1)

plt.hist(iris_data['sepallength'], bins = 15)

plt.title('Iris - Sepal Lengths')

plt.subplot(2,2,2)

plt.hist(iris_data['sepalwidth'], bins = 15, color = 'red')

plt.title('Iris - Sepal Widths')

plt.subplot(2,2,3)

plt.hist(iris_data['petallength'], bins = 15, color = 'orange')

plt.title('Iris - Petal Lengths')

plt.subplot(2,2,4)

plt.hist(iris_data['petalwidth'], bins = 15, color = 'green')

plt.title('Iris - Petal Widths')

plt.savefig("HistogramsOfVariables.png")