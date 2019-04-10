import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import sklearn.metrics as skm

# Load our housing data using pandas and then display the first few results along with the data-frame info.
housing = pd.read_csv('data/USA_Housing.csv')
print(housing.head())
print(housing.info())
print(housing.describe())
print(housing.columns)

# Display a pair plot of all the columns.
sns.pairplot(housing)
plt.show()

# Display a distribution plot of the house pricing.
sns.distplot(housing['Price'])
plt.show()

# Display a heat map of the housing correlations.
sns.heatmap(housing.corr(), annot=True, cmap='Reds')
plt.show()

# We are now splitting our data into our features that we can train on (X)
# and the target variables (y)
X = housing.drop(columns=['Price', 'Address'])
y = housing['Price']


# Now we are going to split our data into a training set, and a testing set.
# train_test_split returns a tuple with the training and testing sets, which is why we're using tuple unpacking.
# The inputs our are features (X) and our outputs (Y).
# The test_size is the percentage of data that you want to allocate to the testing data, in this case 40% is testing
# and 60% will go into training. The random_state argument is used to randomly split your data in a uniform way.
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.4, random_state=101)

# Next we will create our linear regression model and train it using the model.fit() method.
model = lm.LinearRegression()
model.fit(X_train, y_train)

# You can see the y-intercept, and also the coefficients of all our features.
print(model.intercept_)
print(model.coef_)

# The coefficients tell you the change in the output value, based on a features unit value.
coef = pd.DataFrame(model.coef_, X.columns, columns=['Coefficients'])
print(coef)

# Now that we've trained our model, we can get our predictions on the test data.
# The returned value will be the predicted 'Price' of the house.
predictions = model.predict(X_test)
print(predictions)

# We can now visualize our predictions against our test answers (y_test).
plt.scatter(y_test, predictions)
plt.show()

# The residuals are the difference between the test answers, and the predictions.
residuals = (y_test - predictions)
sns.distplot(residuals)
plt.show()

# Now we want to figure out the error deviation. We can use Mean Absolute Error:
mean_absolute = skm.mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mean_absolute)

# Or we can use the squared mean
mean_squared = skm.mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mean_squared)

# Or we can use the Root Mean Squared Error
root_mean_squared = np.sqrt(mean_squared)
print("Root Mean Squared Error:", root_mean_squared)
