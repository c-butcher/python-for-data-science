import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.metrics as skm
import sklearn.tree as skt
import sklearn.ensemble as ske

# Kyphosis is a medical condition of the spine. This dataset represents the
# people who had surgical operations and whether the Kyphosis is 'absent' or 'present'.
data = pd.read_csv('data/kyphosis.csv')
print(data.head())
print(data.info())

# Show a quick pair plot of the data.
sns.pairplot(data, hue='Kyphosis', diag_kind='hist')
plt.show()

# We are splitting our data into our training and testing sets.
X_train, X_test, y_train, y_test = ms.train_test_split(data.drop('Kyphosis', axis=1), data['Kyphosis'], test_size=0.3)

# Create our decision tree model
model = skt.DecisionTreeClassifier()
model.fit(X_train, y_train)

# Create predictions based on our trained model
predictions = model.predict(X_test)

# Evaluate how well our decision tree is able to predict
# by creating the confusion matrix and classification report.
confusion_matrix = skm.confusion_matrix(y_test, predictions)
classification_report = skm.classification_report(y_test, predictions)

print(confusion_matrix)
print(classification_report)


# Now we are creating a random forest model and train it.
model = ske.RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Make predictions based on our trained random forest,
# and then create our confusion matrix and classification report.
predictions = model.predict(X_test)
confusion_matrix = skm.confusion_matrix(y_test, predictions)
classification_report = skm.classification_report(y_test, predictions)

print(confusion_matrix)
print(classification_report)

