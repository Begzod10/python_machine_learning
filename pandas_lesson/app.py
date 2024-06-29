import pprint

import pandas as pd
import re

df = pd.read_csv('modified.csv')
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

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# cols = list(df.columns.values)
# columnlarni joylarini almashtirishga
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# df.iloc[:, 4:10] : -> hamma  qatorlarni olishga, 4:10 -> columnlarni indexsi boyicha ajratish
# print(df.head(20))
# df.to_csv('modified.csv', index=False)
# df.to_csv('modified.xlsx', index=False)

# df.to_csv('modified.txt', index=False, sep='\t')

# res = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == "Poison") & (df['HP'] > 70)]
# res = res.reset_index(drop=True) index reset
# res = df.loc[df['Type 1'].str.contains('Fire|Grass',flags=re.I, regex=True)]
# res = df.loc[df['Name'].str.contains('pi[a-z]*',flags=re.I, regex=True)]
# res = df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I, regex=True)]
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' ## Type 1 dagi hamma value Flamer ga ozgaradi
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST', ' VALUE']

# res = df.groupby(['Type 1']).mean(numeric_only=True).sort_values('HP', ascending=False)
# res = df.groupby(['Type 1']).sum()
# df['count'] = 1
# res = df.groupby(['Type 1']).count()['count']
# res = df.groupby(['Type 1', 'Type 2']).count()['count']
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=10):
    res = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, res])
    print(new_df)
