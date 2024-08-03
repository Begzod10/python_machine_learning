import numpy as np
import pandas as pd

# my_index = ['USA', 'CANADA', 'MEXICO']
# mydata = [1776, 1867, 1821]
# my_user = pd.Series(data=mydata, index=my_index)
#
# print(my_user.iloc[0])
# print(my_user['USA'])
# ages = {
#     "sam": 5,
#     "Fran": 10,
#     "Spike": 8
# }
# ages_series = pd.Series(ages)
# print(ages_series)

q1 = {
    "Japan": 80,
    'China': 450,
    "India": 200,
    "USA": 250
}
q2 = {
    "Brazil": 100,
    'China': 500,
    "India": 210,
    "USA": 260
}
sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)
sales = sales_q1 * 2

print(sales)

print(sales_q1.add(sales_q2, fill_value=0))
