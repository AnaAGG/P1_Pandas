# W2-pandas-proyect
![portada.jpg](poner la dirección del gt hub cuando lo haya subido)
## Proyect objetive
As a part of the **Data Analytics** bootcamp in Ironhack, I have done this first database cleaning exercise. For this, I have used the database of ![*shark attacks*] (https://www.kaggle.com/teajay/global-shark-attacks). The main objective of this project is to learn to clean databases using **pandas and numpy** and their visualization using the libraries of **matplotlib.pyplot and seaborn**

## Data download and description
-  *Origin*:![*shark attacks*] (https://www.kaggle.com/teajay/global-shark-attacks) it is a table of shark attack incidents compiled by the Global Shark Attack File.

-  *Variables and kind of variables*: The data frame have 24 variables. 
      - Categorical variables: Case number, Date, Country, Area, Location, Activity, Name, Sex, Age, Injury, Fatal (Y/N), Time, Species, Investigator, pdf, href formula, href, Case Number.1, Case Number.2, Unnamed: 22, Unnamed: 23

      - Continuous variables : Year, Originial order
-  Hypothesis
    1. There are more attacks on men.
    2. There are more attacks during the afternoon
    3. What is the age range with the most shark attacks? Regardless of age, there are more attacks in men 
    4. What year were there the most shark attacks?

        

## Data cleaning
- **Imported/Used libraries:** before start I import the following libraries to perform all the analysis:

    `import pandas as pd`
    `import numpy as np`
    `import matplotlib as plt`
    `import re`

- **Exploring the rows and columns looking for NaN:** the objetive of this step was remove those rows or columns with irrelevant information or with all NaN information.
    * ROWS: in this case I remove all the empty rows using the remove those rows with all NaN data. I observed that a total of 17.020 rows didn't have any information. For this I procedeed to remove them.
    * COLUMNS: i chose a arbitary threshold to remove of the data frame. Based on experiende and other information i select a 70% value to consider remove the columns. Based on this criteria the high percentage of cells with NaN in two columns (Unnamed22n = 0.999885, Unnamed23 =  0.999770) i poceed to remove them.

        Selected variables|Unselected variables|
        Year|Unnamed| 
- Eliminar duplicados

- Convert Data Types
    1. Keep numeric values as numerics
    2. Check whether a numeric is a string or not. If you entered it as a string, it would be incorrect. 
    3. If you can’t convert a specific data value, you should enter ‘NA value’ or something of this sort. Make sure you add a warning as well to show that this particular value is wrong. 

- List of functions used
    - *replace_sex*: with the objetive of replace all the erroneous coding informmation in the data frame. 
    - *mean_age*: with the aim of not having NaN along the age columns I decide to replace this values by the mean age of all the data we have


## Data visualization