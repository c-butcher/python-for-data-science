import pandas_datareader.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
import cufflinks as cf

py.offline.init_notebook_mode(connected=False)
cf.go_offline(connected=False)


# Google Finance isn't reliable to load data anymore, so we tried using IEX, but IEX limits you to the last 5
# years of data. So we went ahead and loaded the data using our pickle file.
allBanks = pd.read_pickle('data/all_banks')

# Create a list of the ticker symbols (as strings) in alphabetical order.
# It seems our pickle data already had this done, we just needed to pull it.
tickers = allBanks.columns.levels[0]

# Set the column name levels (this is filled out for you)
allBanks.columns.names = ['Bank Ticker', 'Stock Info']

# Check the head of the bank_stocks dataframe.
print(allBanks.head())

# What is the max Close price for each bank's stock throughout the time period?
print(allBanks.xs(key='Close', axis='columns', level=1).max())

# Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock.
returns = pd.DataFrame()

# We can use pandas pct_change() method on the Close column to create a column representing this return value.
# Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a
# column in the returns DataFrame.
for tick in tickers:
    returns[tick + ' Return'] = allBanks[tick]['Close'].pct_change()

print(returns.head())

# Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?
sns.pairplot(returns)
plt.show()

# Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns.
# You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?
print(returns.idxmax())
print(returns.idxmin())

# Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire
# time period? Which would you classify as the riskiest for the year 2015?
print(returns.std())                                      # Citigroup was the riskiest
print(returns.loc['2015-01-01':'2015-12-31'].std())       # Morgan Stanley was the riskiest

# Create a distplot using seaborn of the 2015 returns for Morgan Stanley
morgan_stanley_2015_returns = returns.loc['2015-01-01':'2015-12-31']['MS Return']
sns.distplot(morgan_stanley_2015_returns, bins=100)
plt.show()

# Create a distplot using seaborn of the 2008 returns for CitiGroup
citigroup_2018_returns = returns.loc['2008-01-01':'2008-12-31']['C Return']
sns.distplot(citigroup_2018_returns, bins=100)
plt.show()

# Create a line plot showing Close price for each bank for the entire index of time.
# (Hint: Try using a for loop, or use .xs to get a cross section of the data.)
allBanks.xs(key='Close', axis=1, level=1).plot()
plt.show()

# Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
plt.figure(figsize=(12, 6))
allBanks['BAC']['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
allBanks['BAC']['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()
plt.show()

# Create a heatmap of the correlation between the stocks Close Price.
closing_corr = allBanks.xs(key='Close', axis=1, level='Stock Info').corr()
sns.heatmap(closing_corr, annot=True)
plt.show()

# Optional: Use seaborn's clustermap to cluster the correlations together:
sns.clustermap(closing_corr, annot=True)
plt.show()

# Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.
bac = allBanks['BAC'][['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01']

data = [
    go.Candlestick(
        x=bac.index,
        open=bac['Open'],
        close=bac['Close'],
        high=bac['High'],
        low=bac['Low'],
    )
]

layout = {
    'title': '30 Day Rolling',
    'yaxis': {'title': 'AAPL Stock'},
}

fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='data/candlestick.html')

