import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import sklearn.neighbors as skn
import sklearn.metrics as skm

# Load the classified data and display the head, info and describe.
# The data-set contains an index value in the first column,
# which is why we're setting our index column to zero.
classified = pd.read_csv('data/Classified Data', index_col=0)
print(classified.head())
print(classified.info())
print(classified.describe())

# We are creating standard scalar to transform our features
# into standard normally distributed values. We are doing this
# because often the estimator will be biased if the individual
# feature has values that are not evenly distributed.
scaler = pp.StandardScaler()
scaler.fit(classified.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(classified.drop('TARGET CLASS', axis=1))

# Turn  our scaled features into a new DataFrame that contains the standardized features.
classified_features = pd.DataFrame(scaled_features, columns=classified.columns[:-1])
print(classified_features.head())

# Split our data to training and testing data.
X_train, X_test, y_train, y_test = ms.train_test_split(classified_features, classified['TARGET CLASS'], test_size=0.3, random_state=101)

# Create our KNN model and train it
model = skn.KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

# Test our model by getting our predictions
predictions = model.predict(X_test)
print(predictions)

# Get our classification report
class_report = skm.classification_report(y_test, predictions)
print(class_report)

# Get our confusion matrix.
conf_matrix = skm.confusion_matrix(y_test, predictions)
print(conf_matrix)

# We are going to check which n_neighbors value is the best, by trying all values from 1 - 40.
# Then we are going to choose the best one.
iterations = range(1, 40)
error_rate = []
for i in iterations:
    model = skn.KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    error_rate.append(np.mean(predictions != y_test))


# Plotting our error rate, so we can visually see which n_neighbor value has the lowest error rate.
plt.figure(figsize=(10, 6))
plt.plot(iterations, error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

# We found that 18 is the best number of neighbors to look at.
model = skn.KNeighborsClassifier(n_neighbors=18)
model.fit(X_train, y_train)

# Test our model by getting our predictions
predictions = model.predict(X_test)

# Get our new classification report
class_report = skm.classification_report(y_test, predictions)
print(class_report)

# Get our new confusion matrix.
conf_matrix = skm.confusion_matrix(y_test, predictions)
print(conf_matrix)
