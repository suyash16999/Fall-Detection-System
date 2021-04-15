# Support Vector Machine (SVM)
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Extracted_Features.csv')
dataset.dropna(axis = 0, inplace = True)
dataset = dataset.sample(frac = 1, random_state = 0) 
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split, cross_val_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(C=40, kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

from sklearn.externals import joblib
# Save the model as a pickle in a file
joblib.dump(classifier, 'SVM.pkl') 
# Load the pickled model
Test_Classifier = joblib.load('SVM.pkl') 

# Predicting the Test set results
y_pred = Test_Classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))




