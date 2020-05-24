# Use MyKNeighborsClassifier on iris dataset from sklearn

from MyKNeighborsClassifier import *
import random
from scipy.spatial import distance
from sklearn import datasets
from sklearn.metrics import accuracy_score

# load data
iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = split_data(x, y)

# build KNeighborsClassifier
my_classifier = MyKNeighborsClassifier()
my_classifier.fit(x_train, y_train)

predictions = my_classifier.pradict(x_test)
print(accuracy_score(y_test, predictions))
