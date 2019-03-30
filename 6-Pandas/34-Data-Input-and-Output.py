import pandas as pd

# Pandas provides a lot of formats that it can read.
# You can read a CSV file by calling the pandas.read_csv() method.
# It will automatically put it into a data frame.
frame = pd.read_csv('data/example')
print(frame)


# You can also output a data-frame "to" a new file.
# You want to set the index to false when the index column is un-named.
# Otherwise you'll get an "Unnamed: 0" column in your output file.
frame.to_csv('data/example_output', index=False)


# You can also import from Excel files, but pandas does not work with formulas, macros, etc.
# Pandas might throw an error if there are formulas or macros.
# Each sheet will be imported as a data frame, or you can specify a sheet to import.
frame = pd.read_excel('data/Excel_Sample.xlsx', sheet_name='Sheet1')
print(frame)

# You can easily export to excel, and even specify the sheet name.
frame.to_excel('data/Excel_Output.xlsx', sheet_name='Sheet1')


# You can also do a HTTP GET request to retrieve an HTML page.
# This will return a list of data frames, each frame representing a table that was on the html page.
frame = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(frame[0])


# SQL Alchemy is a library that handles SQL interactions
from sqlalchemy import create_engine

# We can create a SQL engine by passing a connection string to the create_engine() method.
# This engine is connecting to a SQLite database that is stored in memory.
engine = create_engine('sqlite:///:memory:')

# Pandas has methods to import or export to SQL using the supplied engine.
# Here we are saving our failed bank data that we loaded from the website above.
frame[0].to_sql('failed_banks', engine)

# We can then use Pandas to load that SQL data into a data frame.
sqldf = pd.read_sql('failed_banks', engine)
print(sqldf)
