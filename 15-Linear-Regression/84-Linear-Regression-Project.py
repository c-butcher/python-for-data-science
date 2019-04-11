import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import sklearn.metrics as skm

ecommerce = pd.read_csv('data/Ecommerce Customers')
print(ecommerce.head())
print(ecommerce.info())
print(ecommerce.describe())

# Create a joint plot using Time on Website vs Yearly Amount Spent
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=ecommerce)
plt.show()

# Create a joint plot using Time on App vs Yearly Amount Spent
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=ecommerce)
plt.show()

# Create a joint plot that uses hex bins to display Time on App vs Length of Membership
sns.jointplot(x='Time on App', y='Length of Membership', data=ecommerce, kind='hex')
plt.show()

# Create a pair plot of the ecommerce data
# The most correlated feature with Yearly Amount Spent would be "Length of Membership".
sns.pairplot(ecommerce)
plt.show()

# Create a linear model plot showing Yearly Amount Spent vs Length of Membership.
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=ecommerce)
plt.show()

# Split the data into our inputs and outputs.
X = ecommerce[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = ecommerce['Yearly Amount Spent']

# We're allocating 30% to our testing size and 70% to our training.
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.3, random_state=101)

# Create the model and train it.
model = lm.LinearRegression()
model.fit(X=X_train, y=y_train)

# Print out the coefficients
print(model.coef_)

# Make the predictions on the testing data.
predictions = model.predict(X=X_test)

# Create a scatter plot of our predictions vs the actual values.
# If it's a straight line, then it has a very low error threshold.
sns.scatterplot(x=y_test, y=predictions)
plt.show()

# Get the mean absolute error
mean_absolute_error = skm.mean_absolute_error(y_test, predictions)
print("Mean Absolute Error", mean_absolute_error)

# Get the mean square error
mean_square_error = skm.mean_squared_error(y_test, predictions)
print("Mean Square Error", mean_square_error)

# Get the root mean square error
root_mean_squared = np.sqrt(mean_square_error)
print("Root Mean Square Error", root_mean_squared)

# Calculate and graph the residuals
residuals = y_test - predictions
sns.distplot(residuals, bins=50)
plt.show()

# Create a DataFrame with the model coefficients.
coef = pd.DataFrame(model.coef_, index=X.columns, columns=['Coefficient'])
print(coef)
