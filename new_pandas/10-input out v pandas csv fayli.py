import numpy as np
import pandas as pd

df = pd.read_csv('files/example.csv')

df.to_csv('test.csv', index=False)