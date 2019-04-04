import pandas as pd
import plotly as py
import plotly.graph_objs as go

py.offline.init_notebook_mode(connected=False)

consumption = pd.read_csv('data/2014_World_Power_Consumption')

# Now we can create our data.
data = dict(
    type='choropleth',
    locations=consumption['Country'],
    locationmode='country names',
    z=consumption['Power Consumption KWH'],
    text=consumption['Text'],
    colorbar={'title': 'Power Consumption in KWH'}
)

# And assign our layout information.
layout = dict(
    title='2014 Power Consumption',
    geo=dict(
        showframe=False,
        projection={'type': 'natural earth'}
    )
)

# Then we can plot the information on the map.
worldmap = go.Figure(data=[data], layout=layout)
py.offline.plot(worldmap, filename='data/4-world-power-consumption.html')


# Load the election data.
elections = pd.read_csv('data/2012_Election_Data')
print(elections.head())


# Now we can create our data.
data = dict(
    type='choropleth',
    locations=elections['State Abv'],
    locationmode='USA-states',
    z=elections['Voting-Age Population (VAP)'],
    text=elections['Voting-Age Population (VAP)'],
    colorbar={'title': 'Eligible Population'}
)

# And assign our layout information.
layout = dict(
    title='US Voting Age Population',
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(85, 173, 240)',
    )
)

# Then we can plot the information on the map.
statemap = go.Figure(data=[data], layout=layout)
py.offline.plot(statemap, filename='data/5-us-voting-age-population.html')
