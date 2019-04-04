import pandas as pd
import plotly as py
import plotly.graph_objs as go

py.offline.init_notebook_mode(connected=False)

gdp = pd.read_csv('data/2014_World_GDP')
print(gdp.head())

data = dict(
    type='choropleth',
    locations=gdp['CODE'],
    z=gdp['GDP (BILLIONS)'],
    text=gdp['COUNTRY'],
    colorbar={'title': 'GDP in Billions USD'}
)

layout = dict(
    title='2014 Global GDP',
    geo=dict(
        showframe=False,
        projection={'type': 'natural earth'}
    )
)

worldmap = go.Figure(data=[data], layout=layout)
py.offline.plot(worldmap, filename='data/3-world-gdp.html')
