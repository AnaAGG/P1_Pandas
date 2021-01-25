# W2-pandas-proyect

![portada.jpg](https://cdn.pixabay.com/photo/2014/04/02/10/56/shark-305004_1280.png)

## Proyect objetive
As a part of the **Data Analytics** bootcamp in Ironhack, I have done this first database cleaning exercise. For this, I have used the database of ![*shark attacks*] (https://www.kaggle.com/teajay/global-shark-attacks). The main purpose of this project is to learn the exploration process in a data cleaning process using Python. 
The following libaries are provided to analyze Shark Attack dataset: **pandas and numpy** and their visualization using the libraries of **matplotlib.pyplot and seaborn**
 

## Data download and description
*Origin*: ![*shark attacks*] (https://www.kaggle.com/teajay/global-shark-attacks). 

It is a table of shark attack incidents compiled by the Global Shark Attack File. This data has been sourced directly from reported shark incidence throughout history. The data has been put together by a team of marine biologists to further understand common factors in shark attack incidents. The data is classified into many variables, stating where, why and when these incidents happened and who was affected.

Each row of the data represents a single incident. In addition, each column represent something different with variables that describe the people attacked (Age, Sex, Activity), characteristic of the attack (Country, Location, date, type of attack, time). 

This is a shark attack data set which contains 25723 rows and 24 columns.  
Data set columns: ['Unnamed: 0', 'Year', 'Month', 'Country', 'Area', 'Type', 'Activity', 'Sex', 'Age', 'Fatal', 'Injury', 'Species'] FALTA ALGUNA?

By using this dataset we evaluate the XXX **hypothesis** for research and testing the ability to work over the dataset:

    1. There are more attacks on men
    2. There are more attacks during the afternoon
    3. What is the age range with the most shark attacks? Regardless of age, there are more attacks in men 
    4. What year were there the most shark attacks?

        

## Data cleaning
This is a collection of both Nan and fresh data, here before performing the analysis on it first we will remove all Nan or NULL value from the given data set and prepare the data to exploit it as best as possible.

- **Imported/Used libraries:** before start I import the following libraries to perform all the analysis:

    `import pandas as pd`

    `import numpy as np`

    `import matplotlib as plt`

    `import re`

- **Exploring the rows and columns looking for NaN:** the objetive of this step was remove those rows or columns with irrelevant information or with all NaN information.
    * ROWS: in this case I remove those rows with all NaN data. I observed that a total of 17.020 rows didn't have any information. For this I procedeed to remove them.
    
    * COLUMNS: I chose a arbitary threshold to remove the some columns in the data frame. Based on experiende and other information I select a 0.7 threshold to consider remove the columns. Based on this criteria the high percentage of cells with NaN in two columns (Unnamed22n = 0.999885, Unnamed23 =  0.999770) i poceed to remove them.

    After data cleaning I worked with a Data Frame with 8703 rowns and 

- Convert Data Types
    1. Keep numeric values as numerics
    2. Check whether a numeric is a string or not. If you entered it as a string, it would be incorrect. 
    3. If you can’t convert a specific data value, you should enter ‘NA value’ or something of this sort. Make sure you add a warning as well to show that this particular value is wrong. 

- List of functions used
    - `replace_sex`: with the objetive of replace all the erroneous coding informmation in the data frame. 
    - `mean_age`: with the aim of not having NaN along the age columns I decide to replace this values by the mean age of all the data we have


## Data visualization and Results

1. Hypothesis: What year had the most shark attacks recorded?

HOW I REPRESENTED IT GRAPHICALLY?

The results showed that the year 2015 had the most incidents reported with 153 shark attacks globally, closely followed by 2017 with 137 attacks recorded. Whilst looking into this question we also found that the amount of attacks each year were fairly consistent, with the average of 125.6, and a standard deviation of 9.225 representing a tight cluster of data (not including 2018, as the year has not been fully completed). When we represented the findings visually, we could see constant trend through the use of a straight line of best fit, showing a levelled set of data.

2. Hypothesis: Which continent had the most attacks reported?

 The figure revealed 2 continents accounting for the majority of the attacks. The findings showed that North America and Oceania was reponsible for 27% of the attacks. 
 
 We looked further into the data to see why this occurred and found that the majority of the incidents involved with attacks were surfing and swimming, and these activities occur predominantly within and North America and Oceania with both countries hosting the top surfing competitions around the world. 
 
3. Hypothesis: what gender was more commonly attacked? My hypothesis: men are more attacked 

Our findings were astounding, we found that men were more attacked by sharks within the studied period. This could be due to a number of reasons such as male predominance in activities around the water including; surfing, fishing, swimming and sailing. 

4. Hypothesis: when there are more sharks attacks? My hypothesis: during the morning 

My hypothesis was rejected, because the peak of attacks occurs during the afternoon. This could be explained because during the afternoon there are more people in the beach. 

In the same way 