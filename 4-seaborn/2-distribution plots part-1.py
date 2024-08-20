import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('05-Seaborn/dm_office_sales.csv')
# plt.figure(figsize=(5, 8), dpi=200)
# sns.rugplot(x='salary', data=df, height=0.5)
sns.set(style='darkgrid')
# data -> malumotlar belgilanadi
# x -> malumot categoriyasi nomi yoziladi
# bins -> yozilgan sonni kichik yoki kottaligiga qarab malumotni analiz qilish osson yoki qiyin boladi

# sns.displot(data=df, x='salary', bins=50, color="red", edgecolor="black", linewidth=4, kde=True)
# sns.histplot(data=df, x='salary')


# sns.kdeplot(data=df, x='salary')
np.random.seed(42)
sample_ages = np.random.randint(0, 100, 200)
sample_ages = pd.DataFrame(sample_ages, columns=['age'])
print(sample_ages)
# sns.rugplot(data=sample_ages, x='age')

# sns.displot(data=sample_ages, x='age', bins=30, rug=True, kde=True)

# clip -> sonlar orasi
# bw_adjust -> grafikdagi statistikani signal ritmi
# fill = True -> linyalarni toldirib beradi rang bn

sns.kdeplot(data=sample_ages, x='age', clip=[0,100], fill=True)
plt.show()
