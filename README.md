# W2-pandas-proyect
![portada.jpg](poner la dirección del gt hub cuando lo haya subido)
## Proyect objetive
As a part  
## Data download and description
-  Origin
-  *Variables and kind of variables*: The data frame have 24 variables. 
      - Categorical variables: Case number, Date, Country, Area, Location, Activity, Name, Sex, Age, Injury, Fatal (Y/N), Time, Species, Investigator, pdf, href formula, href, Case Number.1, Case Number.2, Unnamed: 22, Unnamed: 23

      - Numerical variables : Year, Originial order
-  Hypothesis
    El mayor número de ataues tuvo lugar en la costa Este
    ¿Qúe año hubo más ataques de tiburones?

        ¿Cuál será mi varable respuesta?
        ¿Y mis variables predicitvas? De que tipo son esas variables?


## Data cleaning
- **Imported/Used libraries:** before start I import the following libraries to perform all the analysis:

    `import pandas as pd`
    `import numpy as np`
    `import matplotlib as plt`
    `import re`

- **Exploring the rows and columns looking for NaN:** the objetive of this step was remove those rows or columns with irrelevant information or with all NaN information.
    * ROWS: in this case I remove all the empty rows using the remove those rows with all NaN data
    * COLUMNS: i chose a arbitary threshold to remove of the data frame. Based on experiende and other information i select a 70% value to consider remove the columns. 

    
- Eliminar duplicados
- Avoid typos
- Convert Data Types
    1. Keep numeric values as numerics
    2. Check whether a numeric is a string or not. If you entered it as a string, it would be incorrect. 
    3. If you can’t convert a specific data value, you should enter ‘NA value’ or something of this sort. Make sure you add a warning as well to show that this particular value is wrong.

- Eliminar columnas vacias

- List of functions used
- Filtrado del dataFrame para quedarme solo con aquellas columnas que me interesan? est seria lo último de este apartado quedandome solo con aquellos datos que me son útiles para testar mi hipótesis

## Data visualization