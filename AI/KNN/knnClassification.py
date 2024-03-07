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