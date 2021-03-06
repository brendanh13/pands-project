# pands-project
# Author: Brendan Heeney

# This is the README file for the Programming and Scripting Module Final Project for 2022
# Note  - most of the discussion and referencing can be found in the Jupyter Notebook

Summary of the Project and what needs to be done:

i.      Based on well-known data set called "Iris data set"
ii.     Research the data set
iii.    Investigate the data set by creating documentation and writing code in Python
iv.     Present all output as the project for review / assessment

The key takeaway from the problem statment provided that I want to try follow;

"Imagine that you are to give a presentation on the data set in a few weeks’ time, where you explain what investigating a data set entails and how 
Python can be used to do it.......present your code and it's output to them."


Section 1 - Research

Online investigation of this data set has directed me to a large array of prior research and analysis of the Iris data set which has been already completed.
One such location outlined what the dataset is in simple terms - "It describes particular biological characteristics of various types of Iris flowers, specifically, the length and width of both pedals and the sepals, which are part of the flower’s reproductive system" [1] Upon further reading - it has become clear that the Iris data set has become a fundamental part of the computing world and has been used extensively - even going as far as describing it as "perhaps the best known database to be found in the pattern recognition literature" [2]

The UCI Machine Learning Repository [2] gives us a more precise indication of what is included in the data set:

- The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. 
- The attributes contains information as below:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

Given the information I have gathered so far - I now believe I am in a position to begin assesing the data set.

Section 2 - Initial Analysis / Thoughts

Before I start; I am asking myself what types of things do I want to or could could I find out about the data set and what learnings will I be able to state?

I will jot down these below and use them as I proceed through the analysis (I am keen to do this as I want to try put my own stamp on this instead of potentially being directed too much by the research / analysis available across the internet)

1. What are the data types?
2. Is there any missing data?
3. Confirm there are 50 of each of the 3 species of Iris
4. What are the basic characteristics of each Iris and can I make a simple determination of them...e.g are the petal lengths or width of one species much smaller than the other(s)?
5. Are any of the classes very similar or dissimilar? e.g if I chose a random Iris - would I be able to state with any certainty which species it may or may not be.

Section 3 - Tools / Methods

Which tools / methods will I use for this project?

Firstly - I will start to take a look at the data using a Python program in Visual Studio (I will create a separate program for trial and error called playWithIris.py)

Secondly - I am going to try a Juypter Notebook as I feel this might be a better way to present the Project for submission as code can be run in smaller chunks.

Section 4 - Analysis

The analsys I am presenting will be primarily presented within a Jupyter Notebook while I will also have a small Python programme called analysis.py that will be used to supplement the Jupyter Notebook by creating further data and visual outputs.

The primary location for the analysis is within the Jupyter Notebook called pands-project-iris where I go through step by step all the work I have completed on the dataset.

1) Confirming the layout and size of the data
2) Renaming columns to make them more relevant
3) Data Integrity - checking for null values
4) Understanding the datatypes (e.g floats, objects etc)
5) Drilling down on the species - are there the same amount of each?
6) Basic attributes of the Data; mean, min, max etc
7) Attributes then divided up by species (e.g min of iris-setosa etc)
8) Deriving some new data; creating a new column similar to area by multiplying a length value by a width value
9) Hisotgrams of the variables
10) Scatter Plots of the variables by species

The supplementary analysis.py creates some outputs for us which also inlcude analysis of the dataset

1) A Summary of the Variables in a file called SummaryOfVariables.txt
   This summary includes;
    Count, DataType, Mean, Min, Max
2) A Histogram of each variable saved to separate .png files beginning with "Hist - xxxxx"
3) A set of scatter plots of 4 pairs of variables to examine the relationship between Petals / Sepal and Lengths / Widths.
   These are also in separate files beginning with "Scatter - xxxxxx"


References

[1] https://www.techopedia.com/definition/32880/iris-flower-data-set

[2] https://archive.ics.uci.edu/ml/datasets/iris


Note that I had some Git issues during the project; I had the blue screen of death on my laptop and had to reinstall Windows.
I eventually did manage to get things sync'd up again after a lot of attempts and googling! I am not sure how it will look when you review it from your side.
The method I ended up using was to delete the directory locally on my own PC (i still had this as it was on OneDrive) and then I cloned the pands-project repository 
and pulled all the files down again.  Seems to be ok now. 


