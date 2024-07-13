import numpy as np
import pandas as pd

#
# np.random.seed(101)
# my_data = np.random.randint(0, 101, (4, 3))
# my_index = ['CA', 'NY', 'AZ', 'TX']
# my_columns = ['Jan', 'Feb', 'Mar']
# df = pd.DataFrame(my_data,my_index, my_columns)
df = pd.read_csv('files/tips.csv')
# print(df.columns) th nomlarini oberadi
# print(df.index)
# print(df.head(10)) boshidagi 10 ta danniylar
# print(df.tail(10)) oxiridagi 10 ta danniylar
# print(df.info())
print(df.describe())