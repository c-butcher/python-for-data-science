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

# First we check out the ages by class, so we can find the average age.
sns.boxplot(x='Pclass', y='Age', data=titanic_train)
plt.show()

# We are creating a function that returns the average age, which we have hard-coded
# after looking at the box plot above.
def impute_age(cols):
    age = cols[0]
    pclass = cols[1]

    if pd.isnull(age):
        if pclass == 1:
            return 37
        elif pclass == 2:
            return 29
        else:
            return 24
    else:
        return age


# We are filling in the empty age cells with an average age, which we hard-coded in impute_age.
titanic_train['Age'] = titanic_train[['Age', 'Pclass']].apply(impute_age, axis=1)

# We are dropping the cabin feature since there is too much missing data,
# and then we are dropping any rows that have missing data (which should just be one or two).
titanic_train.drop('Cabin', axis=1, inplace=True)
titanic_train.dropna(inplace=True)

# Now we can see that we have no missing data.
sns.heatmap(titanic_train.isnull(), yticklabels=False, cbar=False)
plt.show()

# When there is a categorical column, we want to create a dummy dataframe
# That converts the values into columns, with a 0 or 1 as the value.
# The problem with this, is that one column will be able to predict the value
# of the other column. This is called "Multi-Co-linearity", and the solution is
# to get rid of one of the columns.
sex = pd.get_dummies(titanic_train['Sex'], drop_first=True)
print(sex.head())

# We are also doing the same with the embark column.
embarked = pd.get_dummies(titanic_train['Embarked'], drop_first=True)
print(embarked.head())

# We want to now add the new sex and embarked columns into the titanic_training data.
titanic_train = pd.concat([titanic_train, sex, embarked], axis=1)

# We are dropping the string columns that we can't use with regression algorithms.
titanic_train.drop(['Embarked', 'Sex', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)
print(titanic_train.head())

# First we need to separate our inputs and outputs.
X = titanic_train.drop('Survived', axis=1)
y = titanic_train['Survived']

# Next we separate our training and testing data.
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.3, random_state=101)

# Then we create our logistical regression model.
model = lm.LogisticRegression()
model.fit(X_train, y_train)

# Run our model and get our predictions
predictions = model.predict(X_test)

# Put our coefficients into a DataFrame for easy viewing.
coef = pd.DataFrame(model.coef_, index=['Coefficient'], columns=X.columns)
print(coef)

# Show a classification report.
print(skm.classification_report(y_test, predictions))

# We can also see the confusion matrix.
print(skm.confusion_matrix(y_test, predictions))
