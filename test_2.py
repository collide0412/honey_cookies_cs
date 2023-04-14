#this is the version that using DTC to predict the phishing website 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

# Load the data from CSV file
data = pd.read_csv('dataset_phishing.csv')

# Print the column names of the data DataFrame
print(data.columns)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('status', axis=1), data['status'], test_size=0.2, random_state=42)

# Create the Decision Tree Classifier model
dtc = DecisionTreeClassifier(random_state=42)

# Fit the model on the training data
dtc.fit(X_train, y_train)

# Predict the labels for the testing data
y_pred = dtc.predict(X_test)

# Evaluate the model performance
accuracy = dtc.score(X_test, y_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the model performance metrics
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1 Score:', f1)

# Save the predicted results to a new CSV file
results = pd.DataFrame({'Numerical order': range(1, len(X_test) + 1), 'URL': X_test['URL'], 'Status': y_pred})
results.to_csv('predicted_results.csv', index=False)