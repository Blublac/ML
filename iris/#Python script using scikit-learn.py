#Python script using scikit-learn
#for decision tree classifer


#sample decision tree classifer
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

#load the iris datasets
datasets = datasets.load_iris()

#fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(datasets.data, datasets.target)
print (model)


#make prediction
excepted = datasets.target
predicted = model.predict(datasets.data)


# summarize the fit of the model

print(metrics.classification_report(excepted,predicted))
print(metrics.confusion_matrix(excepted,predicted))
