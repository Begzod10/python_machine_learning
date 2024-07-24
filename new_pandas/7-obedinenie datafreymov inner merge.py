import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

# pd.merge(registrations,logins,how='inner', on='name') -> 2 ta datafreymni birlashtiradi inner name column boyicha
# pd.merge(left=registrations,right=logins,how='left', on='name') -> chap tarafdagi frame asosiy boladi 2 table dan 1 table dagi malumotlarni id si kochiriladi
# pd.merge(left=registrations,right=logins,how='right', on='name') -> tepadagi kodni aksi
# pd.merge(registrations,logins,how='outer', on='name') -> ikkala frame larni bir biriga qoshadi id tori kemasa NaN bolib tushad
# registrations = registrations.set_index('name') -> name column index ga aylanadi
# pd.merge(registrations,logins,left_index=True,how='inner', right_on='name') -> 2 ta frame ni malumotlarni ketma ketli boyicha merge qiladi

