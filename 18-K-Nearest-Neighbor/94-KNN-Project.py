import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import sklearn.neighbors as skn
import sklearn.metrics as skm

# Read the project data and check the top few results.
data = pd.read_csv('data/KNN_Project_Data')
print(data.head())

# Display a pairplot of all the data with a hue of the Target Class.
#sns.pairplot(data, hue='TARGET CLASS', palette='bwr', diag_kind='hist', aspect=0.5)
#plt.show()

# We are now going to transform the data into standard normalized data.
scaler = pp.StandardScaler()
scaler.fit(data.drop('TARGET CLASS', axis=1))
data_scaled = scaler.transform(data.drop('TARGET CLASS', axis=1))
data_features = pd.DataFrame(data_scaled, columns=data.columns[:-1])
print(data_features.head())

# Separate our data into training and testing sets.
X_train, X_test, y_train, y_test = ms.train_test_split(data_features, data['TARGET CLASS'], test_size=0.3, random_state=101)

# Create a K Neighbors classifier and train our model.
model = skn.KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

# Get the predictions from the model.
predictions = model.predict(X_test)

# Create a confusion matrix
conf_matrix = skm.confusion_matrix(y_test, predictions)
print(conf_matrix)

# Create a classification report.
class_report = skm.classification_report(y_test, predictions)
print(class_report)

error_rate = []
for i in range(1, 40):
    model = skn.KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    error_rate.append(np.mean(predictions != y_test))


# Create a plot showing the error rates
plt.figure(figsize=(10, 6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

# Redoing our model with the best number of neighbors to look at.
model = skn.KNeighborsClassifier(n_neighbors=27)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Create a confusion matrix
conf_matrix = skm.confusion_matrix(y_test, predictions)
print(conf_matrix)

# Create a classification report.
class_report = skm.classification_report(y_test, predictions)
print(class_report)
