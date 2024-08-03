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
# print(df.describe())

# print(df[['total_bill', 'tip']])  # bittada 2 ta qator column olish uchun
# df['tip_percentage'] = np.round(100 * df['tip'] / df['total_bill'], 2) # rounda oxshab ishlidi (round boladigan son, nechi xonali songa qisqarishi)
# df['price_per_person'] = df['total_bill'] / df['size']
# print(df['tip_percentage'])
# df.drop('tip_percentage', axis=1)  # malumot udalit qilish uchun axis=1 => gorizontal , axis=0 => vertikal

# print(df.shape[0])
# df = df.set_index('Payment ID') Payment ID column ni index ga aylantiradi
# df = df.reset_index() indexsla reset boladi
# df = df.set_index('Payment ID')
# print(df.iloc[0]) 1-qatordagi hamma ma'lumotlarni th lari bn chiqazib beradi
# print(df.loc['Sun2959']) index nomi boyicha ma'lumot olish
# print(df.iloc[0:4]) index raqami boyicha malumotlarni olish
# print(df.loc[['Sun2959', 'Sun4608']]) 2 yoki undan ortiq index nomi orqali malumotlarni olish
# print(df.drop('Sun4608')) vertikal boyicha malumot udalit qilish uchun (default axis=0 ga teng)
# print(df.iloc[1:100]) shu orqali kereli ma'lumotlarni ob qolisham mumkin qogani udalit qilib
# one_row = df.iloc[0]
# print(one_row)
# print(df._append(one_row)) malumot qoshish oxiriga
print(df.head())
