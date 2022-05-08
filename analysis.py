# Small Python program to analsyse the variables within the Irish data set for the PandS Project
# The file created in the output of this program will be called analysis.py and contains a basic summary for each variable

# Author: Brendan Heeney

import pandas as pd             
import numpy as np
import matplotlib.pyplot as plt
import sys

# Importing the Data - I have a copy of the iris dataset saved in .csv format in my current directory

df = pd.read_csv('iris.csv')   # read_csv will read in the csv file containing the Iris dataset

original_stdout = sys.stdout   # this is telling Python that it needs to find the stdout using the sys module
 
with open('SummaryOfVariables.txt', 'w') as f:     # this is creating a new file that we can write to and declaring it as the variable f
    sys.stdout = f                                  # changes the standard output to the new file which we have created


    print("Summary of Variables \n\n")          # The \n tells Python to move to next line in the output


    print("Variable = petallength")             
    plc = df["petallength"].count()                 # counting the number of rows of petal length
    print("The number of rows is {}".format(plc))
    typepl = df["petallength"].dtypes               # checking the data type of the variable
    print("This is a {} variable".format(typepl))
    plm = df['petallength'].mean()                  # getting the mean
    print("The mean value of petallength is {}cm".format(round(plm,3)))
    plmin = df['petallength'].min()                 # getting the min
    print("The min value of petallength is {}cm".format(round(plmin,3)))
    plmax = df['petallength'].max()                 # getting the max
    print("The max value of petallength is {}cm \n".format(round(plmax,3)))

    print("Variable = petalwidth")
    pwc = df["petalwidth"].count()
    print("The number of rows is {}".format(plc))
    typepw = df["petalwidth"].dtypes
    print("This is a {} variable".format(typepw))
    pwm = df['petalwidth'].mean()
    print("The mean value of petalwidth is {}cm".format(round(pwm,3)))
    pwmin = df['petalwidth'].min()
    print("The min value of petalwidth is {}cm".format(round(pwmin,3)))
    pwmax = df['petalwidth'].max()
    print("The max value of petalwidth is {}cm \n" .format(round(pwmax,3)))

    print("Variable = sepallength")
    slc = df["sepallength"].count()
    print("The number of rows is {}".format(plc))
    typesl = df["sepallength"].dtypes
    print("This is a {} variable".format(typesl))
    slm = df['sepallength'].mean()
    print("The mean value of sepallength is {}cm".format(round(slm,3)))
    slmin = df['sepallength'].min()
    print("The min value of sepallength is {}cm".format(round(slmin,3)))
    slmax = df['sepallength'].max()
    print("The max value of sepallength is {}cm \n".format(round(slmax,3)))

    print("Variable = sepalwidth")
    swc = df["sepalwidth"].count()
    print("The number of rows is {}".format(plc))
    typesw = df["sepalwidth"].dtypes
    print("This is a {} variable".format(typesw))
    swm = df['sepalwidth'].mean()
    print("The mean value of sepalwidth is {}cm".format(round(swm,3)))
    swmin = df['sepalwidth'].min()
    print("The min value of sepalwidth is {}cm".format(round(swmin,3)))
    swmax = df['sepalwidth'].max()
    print("The max value of sepalwidth is {}cm \n".format(round(swmax,3)))

    print("Variable = class")       
    classc = df["class"].count()
    print("The number of rows is {}".format(plc))
    print("The unique species within the class variable are:")
    listSpecies = pd.unique(df['class'])        # finding the unique values within the class column
    print(listSpecies)
    countsetosa = df["class"].value_counts()['Iris-setosa']     # getting the counts by species
    print("The count of the Iris-setosa species is {}".format(countsetosa))
    countvirginica = df["class"].value_counts()['Iris-virginica']
    print("The count of the Iris-virginica species is {}".format(countsetosa))
    countversicolor = df["class"].value_counts()['Iris-versicolor']
    print("The count of the Iris-versicolor species is {}".format(countsetosa))


    
    sys.stdout = original_stdout                # Resets the standard output
 




plt.hist(df['sepallength'])         # basic Pandas logic for creating a histogram

plt.title('Iris - Sepal Lengths')       # adding a title to the plot

plt.savefig("Hist - SepalLength.png")          # saves to a file of this name in the current directory

plt.clf()               # the plt.clf is required in order to keep the histrograms completely separate when saving them to files 

plt.hist(df['sepalwidth'])

plt.title('Iris - Sepal Widths')

plt.savefig("Hist - SepalWidth.png")

plt.clf()

plt.hist(df['petallength'])

plt.title('Iris - Petal Lengths')

plt.savefig("Hist - PetalLength.png")

plt.clf()

plt.hist(df['petalwidth'])

plt.title('Iris - Petal Widths')

plt.savefig("Hist - PetalWidth.png")

plt.clf()

plt.scatter(df['petallength'],df['petalwidth'])         # scatter plot logic in Pandas using the plt.scatter() function - giving two variables as an input
plt.title('Scatter - Petal Length v Petal Width ')      # plot title
plt.xlabel('Petal Length')                              # a label for x axis
plt.ylabel('Petal Width')                               # a label for y axis
plt.savefig("Scatter-PLvPW.png")                        # saving the image of plot to current directory
plt.clf()                                               

plt.scatter(df['sepallength'],df['sepalwidth'])
plt.title('Scatter - Sepal Length v Sepal Width ')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.savefig("Scatter-SLvSW.png")
plt.clf()

plt.scatter(df['petallength'],df['sepallength'])
plt.title('Scatter - Petal Length v Sepal Length ')
plt.xlabel('Petal Length')
plt.ylabel('Sepal Length')
plt.savefig("Scatter-PLvSL.png")
plt.clf()

plt.scatter(df['petalwidth'],df['sepalwidth'])
plt.title('Scatter - Petal Width v Sepal Width ')
plt.xlabel('Petal Width')
plt.ylabel('Sepal Width')
plt.savefig("Scatter-PWvSW.png")
plt.clf()
