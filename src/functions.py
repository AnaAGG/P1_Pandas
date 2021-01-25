import random
import numpy as np
import pandas as pd
import re

def remove_decimals_year(col):
    if '.0' in col:
        return col[:col.rfind('.0')]
    return col


def replace_mean_age(col):    
    mean_age = col.mean()
    mean_age = round(mean_age, 2)
    return mean_age


def replace_sex(col):
    fill_list = ["M", "F"]
    chars =  'M ', 'lli', 'N', '.', 'nan'
    for c in chars:
        col = col.replace(c, random.choice(fill_list))
    return(col)
   

   
def continents (country):
    
    country = str(country)
    
    europe = ["italy"]
    oceania = ["australia", "papua new guinea", "new zealand", "new caledonia", "fiji"]
    asia = ["philippines"]
    africa = ["reunion", "south africa"]
    central_A = ["mexico", "bahamas"]
    south_A = ["brazil"]
    north_A = ["usa"]
    
         
    if country in europe:
        return "Europe"
        
    elif country in oceania:
        return "Oceania"
        
    elif country in asia:
        return "Asia"
        
    elif country in africa:
        return "Africa"
        
    elif country in central_A:
        return "Central_America"
        
    elif country in south_A:
        return "South_America"
        
    elif country in north_A:
        return "North_America"
    
    else:
        return "Unknown"



def injury(x): 
    x = str(x)

    if (x == "M") or (x == "UNKNOWN"):
        return np.nan
    elif (x == "Y"):
        return "Y"
    elif (x == "N"):
        return "N"


def species (col):
    white = re.findall(r".*[Ww](hite|HITE).*", str(col))
    tiger = re.findall(r'.*[Tt].*', str(col))
    grey = re.findall(r'.*[Gg](rey|ray).*', str(col))
    lemon = re.findall(r'.*[Ll].*', str(col))
    bull = re.findall(r'.*[Bb](ull).*', str(col))
    
    if white:
        return "White shark"
    elif tiger:
        return "Tiger shark"
    elif grey:
        return "Grey shark"
    elif lemon:
        return "Lemon shark"
    elif bull:
        return "Bull shark"
    
    else:
        return "Unespecific"