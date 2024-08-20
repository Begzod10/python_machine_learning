import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('05-Seaborn/dm_office_sales.csv')
df['division'].value_counts()
plt.figure(figsize=(15, 5), dpi=200)
# sns.countplot(data=df, x='level of education', hue='division', palette="Set2")
sns.barplot(data=df, x='level of education', y='salary', estimator=np.mean, errorbar='sd', hue='division')
plt.legend(loc=(0.95, 0.5))
plt.show()
