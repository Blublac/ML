#load the necessary libraries
import pandas as pd
#import scikit-learn as sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#load the irisflower

df= pd.read_csv('iris.csv')

#split the data into features and lables
X= df[['sepal_length','sepal_width','petal_length', 'petal_width']]
y= df['variety']

#split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)
#create an svm model and train it
model= SVC()
model.fit(X_train,y_train)
#evaluate the model on thr test data
accuracy= model.score(X_test,y_test)


print('Test accuracy:', accuracy)
