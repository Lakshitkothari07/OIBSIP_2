import numpy as np
import pandas as pd

df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df.head()
df.tail()
df.shape
df.info()
df.describe()
x = df['Region']
x
y = df[' Estimated Unemployment Rate (%)']
y
df2 = df.iloc[:,3]
df2


import plotly.express as px
import matplotlib.pyplot as plt


#Analyzing Data By Bar Graphs
fg = px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (State Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()
fg = px.bar(df,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (Region Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


#Analyzing Data By Box Plot
fg = px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (Statewise) by Box Plot',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


#Analyzing Data By Scatter Plot
fg = px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
                title='Unemploymeny Rate (Statewise) by Scatter Plot',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


#Analyzing Data By Histogram
fg = px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
                  title='Unemploymeny Rate (Statewise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


