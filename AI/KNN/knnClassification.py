import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

iris = datasets.load_iris()
print(type(iris["target"]))

#keys
print("\nKey values: \n", list(iris.keys()))

#features
print("\nFeatue names:\n", list(iris.feature_names))

#target names
print("\nTarget names:\n", list(iris.target_names))

#data matrix
x = iris["data"]

print(iris["target"])

y = (iris["target"] == 2).astype(np.int_) #cast 2 into 0

print(x.shape)
print(y.shape)

print("\nX data type: \n", x.dtype)
print("\nY Data type\n", y.dtype)

#n samples in each class
y_virginica = (y == 1).sum()
y_not_virginica = (y == 0).sum()

print("\nTotal vir:\n", y_virginica)
print("\nTotal Notvir:\n", y_not_virginica)

plt.figure(figsize= (0,0))

classes = ["Viginica", "Not-Virginica"]
data = [y_virginica, y_not_virginica]

plt.bar(0, y_virginica, width=0.5, color='y')
plt.bar(1, y_not_virginica, width=0.5, color='b')

plt.title("Distribution of classes")
plt.ylabel("N of instances")
plt.xticks(range(len(classes)) ,classes)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#classifier model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

#evaluation: training data
y_train_pedicted = knn.predict(X_train)
train_accuracy_knn = np.mean(y_train_pedicted == y_train)
print("\nTraining Accuracy: \n", train_accuracy_knn)

#evaluation: test data
#model accuracy
test_accuracy_knn = knn.score(X_test, y_test)
print("\nTest accuracy: \n", test_accuracy_knn)
y_test_predicted = knn.predict(X_test)
print("No of correct prediction {Test}: %d/%d"%(np.sum(y_test_predicted == y_test), len(y_test)))

cm = confusion_matrix(y_test, y_test_predicted)
print("\nConfusion Matrix (Test Data):\n", cm)

precision = precision_score(y_test, y_test_predicted)
print("\nTest: Precesion = %f\n"%precision)

recall = recall_score(y_test, y_test_predicted)
f1 = f1_score(y_test, y_test_predicted)
print("Test: F1 Score = %f"%f1)



y_virginica_test = (y_test == 1).sum()
y_not_virginica = (y_test == 0).sum()
print(y_virginica_test, y_not_virginica)

cmd = ConfusionMatrixDisplay(cm, display_labels=classes)
cmd.plot()
plt.show()
