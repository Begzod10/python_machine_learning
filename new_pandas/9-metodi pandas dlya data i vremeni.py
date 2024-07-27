import numpy as np
import pandas as pd

from datetime import datetime

my_year = 2015
my_month = 1
my_day = 1
my_hour = 2
my_min = 30
my_sec = 15

my_date = datetime(my_year, my_month, my_day)
my_datetime = datetime(my_year, my_month, my_day, my_hour, my_min, my_sec)
myser = pd.Series(['Nov 3, 1990', '2000-01-01', None])
time_ser = pd.to_datetime(myser, format='mixed')
# pd.to_datetime(myser,format='mixed') -> datetime aylantiradi string date larni
# sales = pd.read_csv('files/RetailSales_BeerWineLiquor.csv')
sales = pd.read_csv('files/RetailSales_BeerWineLiquor.csv', parse_dates=[0])

# FutureWarning: 'A' is deprecated and will be removed in a future version, please use 'YE' instead.
#   sales.resample(rule='A')
