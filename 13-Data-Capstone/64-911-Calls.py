import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py

py.offline.init_notebook_mode(connected=False)

# Read the 911 call data
calls = pd.read_csv('data/911.csv')
print(calls.info())
print(calls.head())


# What are the top 5 zipcodes for 911 calls?
zipcodes = calls['zip'].value_counts().head(5)
print(zipcodes)


# What are the top 5 townships (twp) for 911 calls?
townships = calls['twp'].value_counts().head(5)
print(townships)


# Take a look at the 'title' column, how many unique title codes are there?
unique_titles = calls['title'].nunique()
print(unique_titles)


# In the titles column there are "Reasons/Departments" specified before the title code.
# These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create
# a new column called "Reason" that contains this string value.
calls['Reason'] = calls['title'].apply(lambda title: title.split(':')[0])
print(calls.head(5))


# What is the most common Reason for a 911 call based off of this new column?
common_reasons = calls['Reason'].value_counts()
print(common_reasons.head())


# Now use seaborn to create a countplot of 911 calls by Reason.
sns.countplot(x='Reason', data=calls)
plt.show()


# Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
# The assignment says it should be a 'str' value, but we are getting 'object'. This is because the course is
# using older versions of python and pandas.
print(type(calls['timeStamp'].iloc[0]))


# You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from
# strings to DateTime objects.
calls['timeStamp'] = pd.to_datetime(calls['timeStamp'])


# Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called
# Hour, Month, and Day of Week
calls['Hour'] = calls['timeStamp'].apply(lambda timestamp: timestamp.hour)
calls['Month'] = calls['timeStamp'].apply(lambda timestamp: timestamp.month)
calls['Day of Week'] = calls['timeStamp'].apply(lambda timestamp: timestamp.dayofweek)


# Use the .map() with this dictionary to map the actual string names to the day of the week
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
calls['Day of Week'] = calls['Day of Week'].map(lambda dow: dmap[dow])


# Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column
sns.countplot(x='Day of Week', hue='Reason', data=calls, palette='GnBu_d')
plt.legend(bbox_to_anchor=(1.0, 1), loc='top right')
plt.show()

# Now use seaborn to create a countplot of the Month column with the hue based off of the Reason column
sns.countplot(x='Month', hue='Reason', data=calls, palette='GnBu_d')
plt.legend(bbox_to_anchor=(1.0, 1), loc='top right')
plt.show()


# We have missing months, so we need to fill those numbers in with estimates.
# First we need to group by month.
byMonth = calls.groupby('Month').count()
print(byMonth.head(15))


# Then we are going to create a line plot so we can see the data.
sns.set_style('whitegrid')
byMonth['lat'].plot()
plt.show()

# Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month.
# Keep in mind you may need to reset the index to a column.
sns.set_style('whitegrid')
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.show()

# Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to
# use apply along with the .date() method.
calls['Date'] = calls['timeStamp'].apply(lambda ts: ts.date())

# Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
call_count_by_date = calls.groupby('Date').count()
call_count_by_date['title'].plot()
plt.tight_layout()
plt.show()

# Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
traffic_count = calls[calls['Reason'] == 'Traffic'].groupby('Date').count()
fire_count = calls[calls['Reason'] == 'Fire'].groupby('Date').count()
ems_count = calls[calls['Reason'] == 'EMS'].groupby('Date').count()

traffic_count['title'].plot()
plt.title('Traffic')
plt.show()

fire_count['title'].plot()
plt.title('Fire')
plt.show()

ems_count['title'].plot()
plt.title('EMS')
plt.show()

# Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe
# so that the columns become the Hours and the Index becomes the Day of the Week.
heatmap_hour_count = calls.groupby(['Day of Week', 'Hour']).count()
heatmap_hour_count = heatmap_hour_count['Reason'].unstack()

plt.figure(figsize=(10, 5))
sns.heatmap(heatmap_hour_count)
plt.show()

sns.clustermap(heatmap_hour_count)
plt.show()

# Now repeat these same plots and operations, for a DataFrame that shows the Month as the column
heatmap_month_count = calls.groupby(['Day of Week', 'Month']).count()
heatmap_month_count = heatmap_month_count['Reason'].unstack()

plt.figure(figsize=(10, 5))
sns.heatmap(heatmap_month_count)
plt.show()

sns.clustermap(heatmap_month_count)
plt.show()



