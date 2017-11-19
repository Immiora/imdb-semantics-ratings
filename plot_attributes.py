import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('kaggle_attr6.csv', delimiter = ';')


#scatter plots
df.plot(kind='scatter',x='budget',y='ratings', logx=True) #budget
#df.plot(kind='scatter',x='gross', y='ratings', logx=True) # grosses
df.plot(kind='scatter',x='deltaPopularities',y='ratings', logx=True) #delta popularities
#df.plot(kind='scatter',x='popularities', y='ratings', logx=True) # popularities
df.plot(kind='scatter',x='numberReviews',y='ratings', logx=True) #number of reviews
df.plot(kind='scatter',x='releaseDates',y='ratings') #release dates
df.plot(kind='scatter',x='blackWhite',y='ratings') #blackWhite
df.plot(kind='scatter',x='durations',y='ratings',logx=True) #duration


#density function and histogram of ratings
df.plot(kind='density',y='ratings')  # estimate density function
df.plot(kind='hist', y='ratings')  # histogram

plt.show()