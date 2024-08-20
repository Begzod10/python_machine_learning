import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('05-Seaborn/StudentsPerformance.csv')
# kind -> grafik turlarini yozish uchun

# sns.jointplot(data=df, x='math score', y='reading score',hue='gender')
# corner=True -> duplicate grafiklarni yoqotadi
sns.pairplot(data=df, hue='gender', corner=True)
plt.show()
