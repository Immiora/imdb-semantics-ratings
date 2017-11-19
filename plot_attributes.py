import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('kaggle_attr6.csv', delimiter = ';')

df.plot(x='deltaPopularities',y='ratings')  # plots all columns against index
df.plot(kind='scatter',x='deltaPopularities',y='ratings') # scatter plot
df.plot(kind='density',x='deltaPopularities',y='ratings')  # estimate density function
df.plot(kind='hist', x='deltaPopularities',y='ratings')  # histogram

plt.show()