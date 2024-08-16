import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('05-Seaborn/dm_office_sales.csv')
df.head()
plt.figure(figsize=(12, 4), dpi=200)
# hue -> category boyicha grafik chizib beradi
# palette -> rang turi
# size -> nuqtalarni razmeri malumot soniga qarab kotta yoki kichik boladi
# s > nuqtalarga razmer berishga
# alpha -> css dagi opacity
# style -> har bir malumotga categoriyasiga qarab marker belgilidi
sns.scatterplot(x='salary', y='sales', data=df, style="level of education", hue="level of education")
plt.savefig('my_plot.png')
plt.show()
