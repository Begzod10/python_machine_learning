import pandas as pd
import numpy as np

df = pd.read_csv('files/Sales_Funnel_CRM.csv')

# licenses = df[['Company', 'Product', "Licenses"]] -> columnlar boyicha malumotlarni olish
# pd.pivot(data=licenses, index="Company", columns='Product',values='Licenses') ->
# index -> company column kop joylarda ishlatilvatgani uchun uni qisqartirib beradi
# columns = "Product" -> Product bo'yicha malumotlar sortirovka bo'ladi
# values='Licenses' -> values licenses value lari boladi

# pd.pivot_table(df,index="Company", aggfunc='sum') -> 2 - yoki undan kop joyda ishlatilvatgan bir xil column company larni birlashtirib summalarini bir biriga qoshib beradi

# df.groupby('Company').sum()  -> 2 - yoki undan kop joyda ishlatilvatgan bir xil column company larni birlashtirib summalarini bir biriga qoshib beradi

# pd.pivot_table(df,index="Company", aggfunc='sum',values=['Licenses', 'Sale Price']) -> 2 - yoki undan kop joyda ishlatilvatgan bir xil column company larni birlashtirib values summalarini bir biriga qoshib beradi

# pd.pivot_table(df, index=['Account Manager', "Contact"], values=['Sale Price'],columns=['Product'], aggfunc=[np.sum,np.mean], fill_value=0)
# index=['Account Manager', "Contact"] -> 2 column uchun index yaratiladi
# values=['Sale Price'], columns=['Product'] -> product column lari boyicha sale price summalari bir biriga qoshiladi i averagenini chiqazib beradi
# fill_value=0 -> default qiymat bosh qiymatlaga


# pd.pivot_table df.groupby ga oxshab ishlidi ustun tarafi pivot table da malumotlarni oqishga osson qilib joylashtirish mumkin

# pd.pivot_table(df, index=['Account Manager', "Contact", "Product"], values=['Sale Price'], aggfunc="sum", fill_value=0, margins=True)
# margins=True -> hamma qiymatlarni bir biriga qoshib umumiy summani chiqazib beradi