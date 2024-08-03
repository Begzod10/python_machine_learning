import numpy as np
import pandas as pd

df = pd.read_csv('files/tips.csv')

print(df['total_bill'])
# df[(df['sex'] == 'Male') & (df['size'] > 3)] -> 2 ta ma'lumot bo'yicha filterlash (& -> va | -> yoki)

#
# options = ['Sat', 'Sun']
# df[df['day'].isin(options) ]# xuddi sqlalchemy dagi filter in_ ga oxshab ishlidi
