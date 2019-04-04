import pandas as pd
import plotly as py
import plotly.graph_objs as go

py.offline.init_notebook_mode(connected=False)

# Create our choropleth map with hard-coded data.
data = dict(
    type='choropleth',
    locations=['AZ', 'CA', 'NY'],
    locationmode='USA-states',
    colorscale='Earth',
    text=['Arizona', 'California', 'New York'],
    z=[221, 115, 332],
    colorbar={'title': 'Colorbar Title'}
)

# Set the layout scope to be the united states.
layout = dict(geo={'scope': 'usa'})

# Load our data and layout information into our figure.
figure = go.Figure(data=[data], layout=layout)

# Plot the choropleth map.
py.offline.plot(figure, filename='data/1-usa-choromap.html', auto_open=False)


# Load the US Agricultural Exports by State
df = pd.read_csv('data/2011_US_AGRI_Exports')
print(df.head())

# Create the data for the choropleth map.
data = dict(
    type='choropleth',
    locations=df['code'],
    locationmode='USA-states',
    colorscale='Viridis',
    text=df['text'],
    marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
    z=df['total exports'],
    colorbar={'title': 'Total Exports'}
)

# Set the layout of the map
layout = dict(
    title='2011 US Agriculture Exports by State',
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(85, 173, 240)'
    )
)

# Create the figure
figure = go.Figure(data=[data], layout=layout)

# Take the figure information and plot it.
py.offline.plot(figure, filename='data/2-usa-agri-exports.html')


