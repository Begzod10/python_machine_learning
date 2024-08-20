import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('05-Seaborn/StudentsPerformance.csv')

df.head()
plt.figure(figsize=(14, 4), dpi=200)
# x va y boyicha sub category qilib grafik chizish
# sns.boxplot(data=df, x='reading score', y='parental level of education', hue='test preparation course')


# split -> 2 ta grafikni yopishtiradi
# inner -> grafikdagi chiqizni yoqotadi (inner turlari -> stick, quartile)
# sns.violinplot(data=df, x='reading score', y='parental level of education', hue='test preparation course', split=True,
#                inner=None)

# bw -> signalni kuchli kuchsiz qilib korsatish (0.1 siganlni kuchli qib korsatadi)
# sns.violinplot(data=df, x='reading score', y='parental level of education', bw=0.1)

# dodge -> y oqidgi malumotlarni alohida qismlarga bolib korsatadi
# sns.swarmplot(data=df, x='math score', y='gender', hue='test preparation course', size=2, dodge=True)
sns.boxenplot(data=df, x='math score', y='test preparation course', hue='gender')
plt.show()
