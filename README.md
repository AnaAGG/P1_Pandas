# W2-pandas-proyect

![portada.jpg](https://cdn.pixabay.com/photo/2014/04/02/10/56/shark-305004_1280.png)

## Proyect objetive
As a part of the **Data Analytics** bootcamp in Ironhack, I have done this first database cleaning exercise. For this, I have used the database of [shark attacks](https://www.kaggle.com/teajay/global-shark-attacks) from kaggle. The main purpose of this project is to learn the exploration process in a data cleaning process using Python. 
 

## Data download and description
It is a table of shark attack incidents compiled by the Global Shark Attack File. This data has been sourced directly from reported shark incidence throughout history. The data has been put together by a team of marine biologists to further understand common factors in shark attack incidents. The data is classified into many variables, stating where, why and when these incidents happened and who was affected.

Each row of the data represents a single incident. In addition, each column represent something different with variables that describe the people attacked (Age, Sex, Activity) or characteristic of the attack (Country, Location, date, type of attack, time). This dataset contains 25723 rows and 24 columns.  

By using this dataset we evaluate the few **hypothesis** for research and testing the ability to work over the dataset:

> **HYPOTHESIS** 
>
> **Oceania is the most dangerous and lethal place to relaxing by the beach** 
> **The species that attacks the most is the tiger shark**
>
>Other questions checked in this proyect:
> - What is the age range with the most shark attacks? Regardless of age, are there more attacks in men?
>-  Are there more attacks during the afternoon?
>-  What year were there the most shark attacks?
>

        

## Data cleaning
This is a collection of both Nan and fresh data, here before performing the analysis on it first we will remove all Nan or NULL value from the given data set and prepare the data to exploit it as best as possible.

- **Imported/Used libraries:** before start I import the following libraries to perform all the analysis:

    `import pandas as pd`

    `import numpy as np`

    `import matplotlib as plt`

    `import re`

    `import random`

    `import re`

- **Exploring the rows and columns looking for NaN:** the objetive of this step was remove those rows or columns with irrelevant information or with all NaN information.
    * ROWS: in this case I remove those rows with all NaN data. I observed that a total of 17.020 rows didn't have any information. For this I procedeed to remove them.
    
    * COLUMNS: I remove all the irrelevant columns for the proyect objetive. In addition , I create a new column named *"Continents"*

    After data cleaning I worked with a Data Frame with 8703 rowns and 15 columns.

|Variable |list |
|:---:| --- |
| Date (months) | Activity |
| Year | Area |
| Type of attack| Location |
| Country | Sex|
|Fatal (Y/N) | Age |
|Time | Species | 
|Continent|


- **Convert Data Types**
    1. Keep numeric values as numerics
    2. Check whether a numeric is a string or not. If you entered it as a string, it would be incorrect. 
    

- **List of functions used**
    - `replace_sex`: to replace all the erroneous coding informmation in the data frame. 
    - `replace_mean_age`: to replace this values by the mean age of all the data we have.
    - `continents` to create a new column with continent information.
    - `injury` to replace erroneous data for NaN.
    - `species` to clear the species columns and extract the five most dangerous species using *regex*.


## Data visualization and Results

**1. Main Hypothesis: Is Oceania the most dangerous and lethal place to relaxing by the beach?**

The results showed that in 2018 (the last year with available data), Oceania present the higher number of attacks (12) followed by far by North America (3). In 2017 this pattern was inverted and North America presented more sharks attacks (21) than Ocenia (12). However, when we plotted the number of attacks by continent we clearly shown that Oceania is the most dangerous to enjoy safely in the beach(Fig_1).

Then I tried to know is if there are differences in the activity that the attacked were carrying out. The hypothesis can be raised that surfers are those who attack the most. In this case, the Fig_2 indicated that this hypothesis is true.  
 
**2. Hypothesis: What is the age range with the most shark attacks? Regardless of age, are there more attacks in men? My hypothesis:young people are mor attacked,  men are more attacked** 

Firstly, the result showed that there are a peak of attacks in ages around 28. In addition, we found that men were more attacked by sharks within the studied period. 

Fewer women suffer lethal attacks than men, but this may be related to the higher number of men attacked (Fig_3).

**3. Hypothesis: when there are more sharks attacks? My hypothesis: during the morning** 

My hypothesis was rejected, because the peak of attacks occurs during the afternoon. This could be explained because during the afternoon there are more people in the beach (Fig_4). 

**4. Which is the relation between species and type of attacks/Fatal/Time**

- 4.1 Species *vs* type of attacks:

In general, the sharks attacks are provoked for all species excet for Whithe shark that attack more to boats(Fig_5).


- 4.2 Species *vs* Fatal attacks:

Regardless of species, attacks are not lethal (Fig_6)


- 4.3 Species *vs* Time:

All species attacks during the afternoon (Fig_7)

