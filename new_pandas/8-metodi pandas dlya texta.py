# import numpy as np
# import pandas as pd
#
# email = 'rimefara@gamil.com'
#
# names = pd.Series(['andrew', 'bobo', 'claire', 'david', '5'])
# # names.str -> string metodlarini ishlatsa boladi
# text_finance = ['GOOG,APPL,AMZN', 'JPN,BAC,GS']
# tickers = pd.Series(text_finance)
# tech = 'GOOG,APPL,AMZN'
# messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
#
# def cleanup(name):
#     name = name.replace(";", "")
#     name = name.strip()
#     name = name.capitalize()
#     return name

import timeit

# Этот фрагмент кода запускается только один раз
setup = '''
import pandas as pd
import numpy as np
messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name
'''

# Это фрагменты кода, для которых мы будем измерять время выполнения
# (они запускаются много раз)
stmt_pandas_str = ''' 
messy_names.str.replace(";","").str.strip().str.capitalize()
'''

stmt_pandas_apply = '''
messy_names.apply(cleanup)
'''

stmt_pandas_vectorize = '''
np.vectorize(cleanup)(messy_names)
'''