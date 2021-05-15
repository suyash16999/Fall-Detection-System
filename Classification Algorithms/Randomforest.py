import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

dataset = pd.read_csv('Extracted_Features.csv')
dataset.dropna(axis = 0, inplace = True)
dataset = dataset.sample(frac = 1, random_state = 0)
dataset.to_csv('features500.csv') 

X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(
                      min_samples_split=3,
                      n_estimators=10,
                      bootstrap=True,
                      n_jobs=-1,
                      random_state=0,
                      max_features='auto')

rf_classifier.fit(X_train, y_train)
from sklearn.externals import joblib
# Save the model as a pickle in a file
joblib.dump(rf_classifier, 'RF.pkl') 
# Load the pickled model
Test_Classifier = joblib.load('RF.pkl') 
y_pred = Test_Classifier.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, roc_auc_score, roc_curve, f1_score

accuracy_score(y_test, y_pred)
print("The accuracy of the model is  {} %".format(str(round(accuracy_score(y_test,y_pred),3)*100)))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

# get importance
importance = rf_classifier.feature_importances_
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xlabel('Features')
pyplot.ylabel('Importance')
pyplot.title('Before Feature Reduction')
pyplot.show()
# summarize feature importance
for i,v in enumerate(importance):
            out = np.logical_not(importance < 0.005) 
            final = importance[out]
            #print(importance[out])
            #print('Feature: %0d, Score: %.5f' % (i,v))

# plot feature importance
pyplot.bar([x for x in range(len(final))], final)
pyplot.xlabel('Features')
pyplot.ylabel('Importance')
pyplot.title('After Feature Reduction')
pyplot.show()