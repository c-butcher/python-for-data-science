import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.svm as sks
import sklearn.model_selection as ms
import sklearn.metrics as skm
import sklearn.datasets as skd

# Load the IRIS dataset
iris = sns.load_dataset('iris')
print(iris.head())

# Show a pairplot of the data and separate by the species column.
sns.pairplot(iris, hue='species', palette='Dark2')
plt.show()

setosa = iris[iris['species'] == 'setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'], cmap='plasma', shade=True, shade_lowest=False)
plt.show()

X_train, X_test, y_train, y_test = ms.train_test_split(iris.drop('species', axis=1), iris['species'], test_size=0.3)

# First we create a Scalable Vector Classifier and train it.
model = sks.SVC()
model.fit(X_train, y_train)

# Then we predict off our SVC model, and display the performance reports.
predictions = model.predict(X_test)
confusion_matrix = skm.confusion_matrix(y_test, predictions)
classification_report = skm.classification_report(y_test, predictions)

print(confusion_matrix)
print(classification_report)

# Now we are creating a GridSearch, that will allow us to figure out
# the best parameters for our Scalable Vector Classifier.
search = ms.GridSearchCV(model, {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001]
})

# Train our GridSearch, which attempts to find out which variation
# of the settings works best.
search.fit(X_train, y_train)

# Then we run our predictions off our Grid Search, and display the
# performance reports.
predictions = search.predict(X_test)
confusion_matrix = skm.confusion_matrix(y_test, predictions)
classification_report = skm.classification_report(y_test, predictions)

print(confusion_matrix)
print(classification_report)
