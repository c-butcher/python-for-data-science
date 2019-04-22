import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.svm as sks
import sklearn.model_selection as ms
import sklearn.metrics as skm
import sklearn.datasets as skd

# Load the breast cancer data from scikit-learn.
cancer = skd.load_breast_cancer()
print(cancer.keys())
print(cancer['DESCR'])

# Convert the loaded cancer data into a pandas data frame.
features = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
print(features.head())
print(features.info())

# Separate our data into training and testing sets.
X_train, X_test, y_train, y_test = ms.train_test_split(features, cancer['target'], test_size=0.3, random_state=101)

# Create our Support Vector Classifier and train it.
model = sks.SVC()
model.fit(X_train, y_train)

# Create our predictions
predictions = model.predict(X_test)

# Check to see how accurate our model was...
print("\r\nConfusion Matrix:")
print(skm.confusion_matrix(y_test, predictions))

print("\r\nClassification Report:")
print(skm.classification_report(y_test, predictions))


# Now we are switching to using a GridSearch to find the best
# parameters for our SVC model.
search = ms.GridSearchCV(model, verbose=3, param_grid={
    'C': [0.1, 1, 10, 100, 1000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001]
})

# You can train and predict directly off your GridSearch
search.fit(X_train, y_train)
predictions = search.predict(X_test)

# Then print our confusion matrix and classification report.
print("\r\nConfusion Matrix:")
print(skm.confusion_matrix(y_test, predictions))

print("\r\nClassification Report:")
print(skm.classification_report(y_test, predictions))
