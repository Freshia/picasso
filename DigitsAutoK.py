from sklearn import datasets,preprocessing,cross_validation,neighbors,model_selection
import numpy as np

digits=datasets.load_digits()
x=np.array(digits.data)
y=np.array(digits.target)
x_train,x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)

def train_model(data,target):
    clf = neighbors.KNeighborsClassifier()
    clf.fit(x_train, y_train)
    return clf

def accuracy(classifier_model):
    accuracy = classifier_model.score(x_test,y_test)
    print(accuracy)

clf = train_model(x,y)
accuracy(clf)