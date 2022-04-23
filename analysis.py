# Small Python program to analsyse the variables with the Irish data set for the PandS Project
# The file created in the output of this program will be called analysis.py and contains a basic summary for each variable

# Author: Brendan Heeney

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import sys

# Importing the Data 

df = pd.read_csv('iris.csv')

original_stdout = sys.stdout  
 
with open('SummaryOfVariables.txt', 'w') as f:
    sys.stdout = f 


    print("Summary of Variables \n\n")


    print("Variable is petallength")
    plc = df["petallength"].count()
    print("The number of rows is {}".format(plc))
    typepl = df["petallength"].dtypes
    print("This is a {} variable".format(typepl))
    plm = df['petallength'].mean()
    print("The mean value of petallength is {}cm".format(round(plm,3)))
    plmin = df['petallength'].min()
    print("The min value of petallength is {}cm".format(round(plmin,3)))
    plmax = df['petallength'].max()
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
    listSpecies = pd.unique(df['class'])
    print(listSpecies)
    countsetosa = df["class"].value_counts()['Iris-setosa']
    print("The count of the Iris-setosa species is {}".format(countsetosa))
    countvirginica = df["class"].value_counts()['Iris-virginica']
    print("The count of the Iris-virginica species is {}".format(countsetosa))
    countversicolor = df["class"].value_counts()['Iris-versicolor']
    print("The count of the Iris-versicolor species is {}".format(countsetosa))


    # Reset the standard output
    sys.stdout = original_stdout 
 


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