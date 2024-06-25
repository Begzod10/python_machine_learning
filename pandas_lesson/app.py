import pprint

import pandas as pd

df = pd.read_csv('files/pokemon_data.csv')
# print(df.head(3)) boshidan 3 qator
# print(df.tail(3)) oxiridan 3 qator


# df_xlsx = pd.read_excel('files/pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('files/pokemon_data.txt', delimiter='\t')
# print(df_xlsx.head(3))

# Read headers
# print(df.columns)

# read each column
# print(df[['Name', 'Type 1', 'HP']])

# read each row
# pprint.pprint(df.head(4))
# print(df.iloc[0:4])

# read a specific location (R,C)

# print(df.iloc[2, 1])

# iterate_each_row

# for index, row in df.iterrows():
#     pprint.pprint(row)

# res = df.loc[df['Type 1'] == "Grass"]
# print(res)
# print(df.describe())

# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#
# df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]  # columnlarni joylarini almashtirishga

# df.iloc[:, 4:10] : -> hamma  qatorlarni olishga, 4:10 -> columnlarni indexsi boyicha ajratish
print(df.head(20))
