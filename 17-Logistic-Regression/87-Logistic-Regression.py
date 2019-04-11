import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import sklearn.metrics as skm

# Load our training data
titanic_train = pd.read_csv('data/titanic_train.csv')

# Output the information about our training data.
print(titanic_train.head())
print(titanic_train.info())
print(titanic_train.describe())

# We can show how much data is missing by creating a heatmap based on the null data.
sns.heatmap(titanic_train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

# Set our grid style to white with gray lines.
sns.set_style('whitegrid')

# Plot the number of survivors by sex.
sns.countplot(x='Survived', data=titanic_train, hue='Sex')
plt.show()

# Plot the number of survivors by class
sns.countplot(x='Survived', data=titanic_train, hue='Pclass')
plt.show()

# Plot out the number of passengers by age.
sns.distplot(titanic_train['Age'].dropna(), kde=False, bins=30)
plt.show()

# Plot the number of relatives people had on board.
sns.countplot(x='SibSp', data=titanic_train)
plt.show()

# Plot out how much a person paid for a ticket.
plt.figure(figsize=(10, 4))
sns.distplot(titanic_train['Fare'], kde=False, bins=40)
plt.show()



