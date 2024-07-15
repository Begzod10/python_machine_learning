import numpy as np
import pandas as pd

df = pd.read_csv('files/movie_scores.csv')
# df[(df.pre_movie_score.isnull()) & (df['first_name'].notnull())]
# isnull() -> bosh danniylarni filterlashga
# notnull() -> boshmas danniylarni filterlashga
# df.dropna() -> bosh danniylari bor bogan hamma ma'lumotlarni o'chirib tashidi
# df.dropna(thresh=1) -> 1 qatordagi 1 column danniysi bosh bomagan danniylarni ochirmidi
# df.dropna(subset=['last_name']) last_name bosh boganlarni ochirib tashidi
# df.fillna('new name') -> hamma bosh danniylarni new name ga ozgartiradi
# df['pre_movie_score'].fillna(12) -> 'pre_movie_score' columni danniylarini 12 ga ozgartiradi
# df.pre_movie_score.mean() -> 'pre_movie_score' column dagi hamma sonlarni bir biriga qoshib average ni hisoblab beradi
airline_tix = {'first': 100, 'business': np.nan, 'economy-plus': 50, "economy": 30}

ser = pd.Series(airline_tix)
# ser.interpolate() bosh danniyni intorpalatsiya qib beradi (bor malumotlarga qarab bosh danniy ni taxmin qib toldiradi)