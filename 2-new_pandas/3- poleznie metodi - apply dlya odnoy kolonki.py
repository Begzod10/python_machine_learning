import numpy as np
import pandas as pd
import timeit

df = pd.read_csv('files/tips.csv')


def last_four(num):
    return str(num)[-4:]


# df['CC Number'].apply(last_four) -> pandas dagi apply funksiyasi pythondagi boshqa funksiyalarni ishlatishga yordam beradi

def yelp(price):
    if price < 10:
        return '$'
    elif 10 <= price < 30:
        return '$$'
    else:
        return '$$$'


# apply dlya neskolkix kolonok


# lambda num: num * 2

def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return 'shedriy chivi'
    else:
        return 'obichnie chivi'


# res = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']),axis=1)

# df['Tip Quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1) sekin
# df['Tip Quality'] = np.vectorize(quality)(df.total_bill, df.tip) tez

# timeit ni organish kere