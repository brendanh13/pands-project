# This is just an initial Python Program to familiarize myself with the Iris data set

# Author: Brendan Heeney

# I want to start with Pandas as I do know that this is useful for analyzing data

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Importing the Data 

df = pd.read_csv('iris.csv')

# print(df.head(10))    --Top 10 Rows--

# print(df.info())        --Information about the Data--

# print(df.describe())      --Getting more information on the Data--

# print(df[['sepallength','sepalwidth','petallength','petalwidth']].describe())

# print(df.describe(include='all'))

print(df.groupby('class')['sepallength'].describe())
print(df.groupby('class')['sepalwidth'].describe())