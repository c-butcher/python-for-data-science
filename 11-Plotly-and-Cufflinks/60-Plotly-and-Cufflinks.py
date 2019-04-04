import pandas as pd
import numpy as np
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go

# Plotly allows you to host the figures online.
# Unfortunately we don't want that, so we are enabling offline mode.
cf.go_offline()

# Here we are creating some random data.
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())


# Create a scatter plot. Since we are in offline mode, we need
# to save our plot to a file.
py.offline.plot([
    go.Scatter(x=df.index, y=df['A'], mode='markers', name='A'),
    go.Scatter(x=df.index, y=df['B'], mode='markers', name='B'),
    go.Scatter(x=df.index, y=df['C'], mode='markers', name='C'),
    go.Scatter(x=df.index, y=df['D'], mode='markers', name='D'),
], filename='data/one.html', auto_open=False)


# Create a bar plot.
py.offline.plot([
    go.Bar(x=['A', 'B', 'C'], y=[32, 43, 50]),
], filename='data/two.html', auto_open=False)


# Create a box plot.
py.offline.plot([
    go.Box(y=df['A'], name='A'),
    go.Box(y=df['B'], name='B'),
    go.Box(y=df['C'], name='C'),
    go.Box(y=df['D'], name='D'),
], filename='data/three.html', auto_open=False)

# Create a three-dimensional surface plot.
df2 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 20, 10], 'z': [5, 4, 3, 2, 1]})
py.offline.plot([
    go.Surface(z=df2.as_matrix(), colorscale='Jet')
], filename='data/four.html', auto_open=False)


# Create a histogram. We need to first create figure so that we can customize the
# layout to have the bars be overlayed.
fig = go.Figure([
    go.Histogram(x=df['A'], name='A'),
    go.Histogram(x=df['B'], name='B'),
    go.Histogram(x=df['C'], name='C'),
    go.Histogram(x=df['D'], name='D')
], layout=go.Layout(barmode='overlay'))

py.offline.plot(fig, filename='data/five.html', auto_open=False)


# Scatter plot with bubbles
py.offline.plot([
    go.Scatter(x=df['A'], y=df['B'], mode='markers')
], filename='data/six.html', auto_open=False)


# Scatter plot matrix.
py.offline.plot([
    go.Splom(dimensions=[
        {'label': 'A', 'values': df['A']},
        {'label': 'B', 'values': df['B']},
        {'label': 'C', 'values': df['C']},
        {'label': 'D', 'values': df['D']},
    ], diagonal=dict(visible=False))
], filename='data/seven.html', auto_open=False)
