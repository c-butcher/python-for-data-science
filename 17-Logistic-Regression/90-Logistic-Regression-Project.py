import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import sklearn.metrics as skm

# Load our data
advertising = pd.read_csv('data/advertising.csv')
print(advertising.head())
print(advertising.info())
print(advertising.describe())

# Create a histogram of the Age
sns.distplot(advertising['Age'], bins=30, kde=False)
plt.show()

# Create a jointplot showing Area Income versus Age.
sns.jointplot(x=advertising['Age'], y=advertising['Area Income'])
plt.show()

# Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.
sns.jointplot(x=advertising['Age'], y=advertising['Daily Time Spent on Site'], kind='kde', color="r")
plt.show()

# Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage
sns.jointplot(x=advertising['Daily Time Spent on Site'], y=advertising['Daily Internet Usage'], color='g', s=10, xlim=[20, 100], ylim=[50, 300])
plt.show()

# Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.
plot = sns.pairplot(advertising, hue='Clicked on Ad', palette='bwr', diag_kind='hist')
plt.show()

# Now we break our data into inputs and outputs.
X = advertising[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = advertising['Clicked on Ad']

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, train_size=0.3, random_state=101)

# Next create our model and train it.
model = lm.LogisticRegression()
model.fit(X_train, y_train)

# Test our model by running predictions.
predictions = model.predict(X_test)

# Create a classification report.
report = skm.classification_report(y_test, predictions)
print(report)

# Displaying the column coefficients.
coef = pd.DataFrame(data=model.coef_, index=['Coefficients'], columns=X.columns)
print(coef)
