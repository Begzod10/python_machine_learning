import numpy as np
import pandas as pd

df = pd.read_csv('files/mpg.csv')

year_cyl = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
# year_cyl.xs(key=70,level="model_year") model year 70 yildagi malumotlarni chiqazib beradi
#  year_cyl.xs(key=4,level="cylinders") har yildagi cylinder 4 bogan malumotlarni chiqazib beradi
# df[df['cylinders'].isin([6,8])] -> cylinders 6,8 bogan malumotlarni filterlab beradi
# df[df['cylinders'].isin([6,8])].groupby(['model_year', 'cylinders']).mean(numeric_only=True) -> cylinderi 6,8 bogan malumotlarni filterlab moder_year cylinder boyicha group by qilib averagini hisoblab beradi qolgan danniylarni

# !!! birinchi bolib filter qilib keyin group by qilgan yaxshi, group by bolgan elementlarni 2-yoki undan kop column boyicha filterlab bomidi

# year_cyl.swaplevel() -> indexlarni ornini almashtirib beradi

# year_cyl.sort_index(level='model_year',ascending=False) -> model year value larni teskari taxlab beradi
# df.agg({'mpg': ['max', 'mean'],'weight': ['mean', 'std']}) -> mpg max, mean bocyicha hisoblab beradi, weight mean, std boyicha hisoblab beradi

# df.agg(['std','mean'])['mpg'] ishlamadi
# df.agg(['std','mean']) ishlamadi