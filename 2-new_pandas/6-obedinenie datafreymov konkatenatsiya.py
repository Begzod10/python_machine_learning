import numpy as np
import pandas as pd

data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)
# pd.concat([one,two], axis=1) data frame larni column boyicha birlashtirish
# two.columns = one.columns -> two dagi columnlarni hammasin nomini one dagi column nomiga ozgartiradi
# mydf.index = range(len(mydf)) -> indexsini yangilab beradi dataframeni