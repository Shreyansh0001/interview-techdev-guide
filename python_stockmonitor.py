import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
#specify the start and end date of the duration for which you want to see the activity of the stock

start = dt.datetime(2016,10,10)
end = dt.datetime(2020,4,21)

df = web.DataReader('GC=F', 'yahoo', start, end) 
#download the csv data for stocks from websites like yahoo finance.
df.to_csv('gold.csv')
 
#plot the graph for the data
df[['Adj Close']].plot()
plt.show()
