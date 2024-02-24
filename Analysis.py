import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Processing 1
df = pd.read_csv('Top_Stories_NYT.csv')
#print(df.head())
#df['section'] = df['section'].astype('|S80')

df["section"].replace("", np.nan).value_counts(dropna=False).plot(kind="pie")
#plt.show()
plt.savefig("News_Categories_Pie_Chart.png")

#Processing 2
