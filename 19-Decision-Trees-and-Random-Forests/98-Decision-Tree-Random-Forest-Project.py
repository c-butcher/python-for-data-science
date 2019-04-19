import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.tree as skt
import sklearn.ensemble as ske
import sklearn.metrics as skm
import sklearn.model_selection as ms

# Read the data and print out the first few rows, column information and a few metrics for the columns.
loans = pd.read_csv('data/loan_data.csv')
print(loans.head())
print(loans.info())
print(loans.describe())

# Create a histogram of two FICO distributions on top of each other, one for each credit.policy outcome.
plt.figure(figsize=(10, 6))
sns.distplot(loans[loans['credit.policy'] == 1]['fico'], bins=30, color='blue', label='Has Credit Policy', kde=False)
sns.distplot(loans[loans['credit.policy'] == 0]['fico'], bins=30, color='red', label='No Credit Policy', kde=False)

plt.legend()
plt.xlabel('FICO')
plt.show()

# Create a similar figure, except this time select by the not.fully.paid column.
plt.figure(figsize=(10, 6))
sns.distplot(loans[loans['not.fully.paid'] == 1]['fico'], bins=30, color='blue', label='Not Fully Paid', kde=False)
sns.distplot(loans[loans['not.fully.paid'] == 0]['fico'], bins=30, color='red', label='Fully Paid', kde=False)

plt.legend()
plt.xlabel('FICO')
plt.show()

# Create a countplot using seaborn showing the counts of loans by purpose, with the color hue defined by not.fully.paid.
sns.countplot(x='purpose', data=loans, hue='not.fully.paid')
plt.show()

# Let's see the trend between FICO score and interest rate. Recreate the following jointplot.
sns.jointplot(x='fico', y='int.rate', data=loans, color='purple')
plt.show()

# Create the following lmplots to see if the trend differed between not.fully.paid and credit.policy.
sns.lmplot(x='fico', y='int.rate', data=loans, hue='credit.policy', col='not.fully.paid', palette='Set1')
plt.show()

# Now we can start cleaning our data to get it ready for our classifier.
# The 'purpose' column is categorical, so we need to change it to numbers using dummy variables.
cleaned_data = pd.get_dummies(loans, columns=['purpose'], drop_first=True)

# Create our training and testing data.
X_train, X_test, y_train, y_test = ms.train_test_split(cleaned_data.drop('credit.policy', axis=1), cleaned_data['credit.policy'], test_size=0.3)

# Create a decision tree classifier and train it.
model = skt.DecisionTreeClassifier()
model.fit(X_train, y_train)

# Run our predictions and get the confusion matrix and classification report.
predictions = model.predict(X_test)
print("\r\nConfusion Matrix\r\n", skm.confusion_matrix(y_test, predictions))
print("\r\nClassification Report\r\n", skm.classification_report(y_test, predictions))

# Now create a Random Forest model, but lets predict the 'not.fully.paid' variable.
X_train, X_test, y_train, y_test = ms.train_test_split(cleaned_data.drop('not.fully.paid', axis=1), cleaned_data['not.fully.paid'], test_size=0.3)

model = ske.RandomForestClassifier(n_estimators=600)
model.fit(X_train, y_train)

# Run our predictions and get the confusion matrix and classification report.
predictions = model.predict(X_test)
print("\r\nConfusion Matrix\r\n", skm.confusion_matrix(y_test, predictions))
print("\r\nClassification Report\r\n", skm.classification_report(y_test, predictions))
