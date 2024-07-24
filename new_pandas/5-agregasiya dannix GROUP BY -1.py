import numpy as np
import pandas as pd

df = pd.read_csv('files/mpg.csv')
# df['model_year'].value_counts() model year dagi hamma value larni qoshib beradi
# df.groupby('model_year').mean(numeric_only=True) malumotlarni model_year value si orqali ortanchasini chiqazib beradi taxlab beradi
# df.groupby('model_year').mean(numeric_only=True)['mpg'] model year value si ketma ketligi boyicha mpg qiymatlarini ortanchasini chiqazib beradi
# df.groupby(['model_year', 'cylinders']).mean(numeric_only=True) -> birinchi bolib model_year group by boladi kyin cylinders
# df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)['mpg'] mpg malumotlarni model_year, cylinders boycha group_by qilib beradi
# df.groupby('model_year').describe().transpose() -> har bitta columni yil boyicha statisticlarni chiqazib beradi

# year_cyl = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
# year_cyl.index -> indexlarni ozini spiska qb chiqazib beradi ketma ketli boyicha
# year_cyl.index.names -> indexlarni nomini chiqazib beradi
# year_cyl.loc[80] -> model_year dagi 80 yildagi malumotlarni chiqazib beradi
# year_cyl.loc[(80,4)] -> model year 80 cylinder 4 dagi ma'lumotlarni chiqazib beradi



