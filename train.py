import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

#Load datase
dataset = pd.read_csv('Student_performance_data _.csv')

# Drop useless ID column
dataset = dataset.drop(columns=['StudentID'])
# 2. Split features and targe
X = dataset.drop(columns=['GradeClass']).values
y = dataset['GradeClass'].astype(int).values
#Train/Test spli
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)
#Base model (Decision Tree
dt = DecisionTreeClassifier(random_state=0)
#Cross validation (baseline check
cv_scores = cross_val_score(dt, X_train, y_train, cv=5)
print("CV Mean Accuracy:", cv_scores.mean())
#GridSearchCV 
params = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5]
}

grid = GridSearchCV(dt, param_grid=params, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best CV Score:", grid.best_score_)
#Train best mode
best_model = grid.best_estimator_

best_model.fit(X_train, y_train)
#Predictio
y_pred = best_model.predict(X_test)
#Evaluatio
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print("Test Accuracy:", acc)

#load model
joblib.dump(best_model, "model.pkl")