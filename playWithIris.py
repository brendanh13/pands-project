# This is just an initial Python Program to familiarize myself with the Iris data set

# Author: Brendan Heeney

# I want to start with Pandas as I do know that this is useful for analyzing data

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import sys

# Importing the Data 

df = pd.read_csv('iris.csv')

# print(df.head(10))    --Top 10 Rows--

# print(df.info())        --Information about the Data--

# print(df.describe())      --Getting more information on the Data--

# print(df[['sepallength','sepalwidth','petallength','petalwidth']].describe())

# print(df.describe(include='all'))

# print(df.groupby('class')['sepallength'].describe())
# print(df.groupby('class')['sepalwidth'].describe())

# print(df.tail())

# print(df.isnull().sum())

# print(df[['sepallength','sepalwidth','petallength','petalwidth']].isnull().sum())

# print(df[['sepallength','sepalwidth','petallength','petalwidth']].dtypes())

# print(df.info())

# print(df.columns)

# print(df.assign(SepalArea=df.sepallength*df.sepalwidth))
# print(df.head())

# df.insert(5,'sepalarea',df.sepalwidth*df.sepallength)
# print(df.head())

# df["sepalarea"] = (df.sepallength*df.sepalwidth)
# print(df.head())

# summary = df.describe()
# print(summary)


# with open("python.txt", "a") as file:
    # summary = df.describe()
    # file.writelines(summary)
    # file.close()

# numpy_array = summary.to_numpy()
# np.savetxt("testfile.txt",numpy_array, fmt = "%d")

""""
print("Summary of Variables \n\n")
print("petallength")
plm = df['petallength'].mean()
print("The mean value of petallength is {}cm".format(round(plm,3)))
plmin = df['petallength'].min()
print("The min value of petallength is {}cm".format(round(plmin,3)))
plmax = df['petallength'].max()
print("The max value of petallength is {}cm \n".format(round(plmax,3)))

print("petalwidth")
pwm = df['petalwidth'].mean()
print("The mean value of petalwidth is {}cm".format(round(pwm,3)))
pwmin = df['petalwidth'].min()
print("The min value of petalwidth is {}cm".format(round(pwmin,3)))
pwmax = df['petalwidth'].max()
print("The max value of petalwidth is {}cm \n" .format(round(pwmax,3)))

print("sepallength")
slm = df['sepallength'].mean()
print("The mean value of sepallength is {}cm".format(round(slm,3)))
slmin = df['sepallength'].min()
print("The min value of sepallength is {}cm".format(round(slmin,3)))
slmax = df['sepallength'].max()
print("The max value of sepallength is {}cm \n".format(round(slmax,3)))

print("sepalwidth")
swm = df['sepalwidth'].mean()
print("The mean value of sepalwidth is {}cm".format(round(swm,3)))
swmin = df['sepalwidth'].min()
print("The min value of sepalwidth is {}cm".format(round(swmin,3)))
swmax = df['sepalwidth'].max()
print("The max value of sepalwidth is {}cm".format(round(swmax,3)))
"""

#plc = df["petallength"].count()
#print(plc)

#listSpecies = pd.unique(df['class'])
#print(listSpecies)

# countsetosa = df["class"].value_counts()['Iris-setosa']
# print("The number of the Iris-setosa species is {}".format(countsetosa))

#countvirginica = df["class"].value_counts()['Iris-virginica']
#print("The number of the Iris-virginica species is {}".format(countsetosa))

#countversicolor = df["class"].value_counts()['Iris-versicolor']
#print("The number of the Iris-versicolor species is {}".format(countsetosa))

"""
original_stdout = sys.stdout  
 
with open('summary_test.txt', 'w') as f:
    sys.stdout = f 
    listSpecies = pd.unique(df['class'])
    print(listSpecies)

    countsetosa = df["class"].value_counts()['Iris-setosa']
    print("The number of the Iris-setosa species is {}".format(countsetosa))

    countvirginica = df["class"].value_counts()['Iris-virginica']
    print("The number of the Iris-virginica species is {}".format(countsetosa))

    countversicolor = df["class"].value_counts()['Iris-versicolor']
    print("The number of the Iris-versicolor species is {}".format(countsetosa))
    # Reset the standard output
    sys.stdout = original_stdout 
 
print('This message will be written to the screen.')
"""
'''
sl = df["sepallength"]
  
plt.hist(sl, color = "green")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Count")
plt.savefig('test1.png')
'''
"""
plt.hist(df['sepallength'], bins = 15)

plt.title('Iris - Sepal Lengths')

plt.savefig("SepalLength.png")

plt.subplot(2,2,1)

plt.hist(df['sepallength'], bins = 15)

plt.title('Iris - Sepal Lengths')

plt.subplot(2,2,2)

plt.hist(df['sepalwidth'], bins = 15, color = 'red')

plt.title('Iris - Sepal Widths')

plt.subplot(2,2,3)

plt.hist(df['petallength'], bins = 15, color = 'orange')

plt.title('Iris - Petal Lengths')

plt.subplot(2,2,4)

plt.hist(df['petalwidth'], bins = 15, color = 'green')

plt.title('Iris - Petal Widths')

plt.savefig("HistogramsOfVariables.png")

"""