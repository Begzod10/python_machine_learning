import numpy as np
import pandas as pd

email = 'rimefara@gamil.com'

names = pd.Series(['andrew', 'bobo', 'claire', 'david', '5'])
# names.str -> string metodlarini ishlatsa boladi
text_finance = ['GOOG,APPL,AMZN', 'JPN,BAC,GS']
tickers = pd.Series(text_finance)
tech = 'GOOG,APPL,AMZN'
messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])

def cleanup(name):
    name = name.replace(";", "")
    name = name.strip()
    name = name.capitalize()
    return name
