from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, classification_report, accuracy_score, mean_squared_error

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.20, random_state=42)
clf = KNeighborsClassifier()
gridsearch = GridSearchCV(clf, {"n_neighbors": [1,3,5,7,9,11], "weights": ["uniform", "distance"], 'p':[1,2,3]}, scoring='f1')


gridsearch.fit(X_train, y_train)
print("best params: {}".format(gridsearch.best_params_))
y_pred_train = gridsearch.predict(X_train)
print("Train f1: {}".format(f1_score(y_train, y_pred_train)))
print("Test classification repot:")
y_pred_test = gridsearch.predict(X_test)
print(classification_report(y_test, y_pred_test))
print("Train accuracy: {} \t Test accuracy: {}".format(accuracy_score(y_train, y_pred_train),accuracy_score(y_test, y_pred_test)))