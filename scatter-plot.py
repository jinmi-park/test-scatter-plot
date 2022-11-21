import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_file = './test_data.csv'
df = pd.read_csv(csv_file, encoding='cp932')

sns.jointplot(x=df.columns[0], y=df.columns[1], data=df, kind='reg')
plt.show()