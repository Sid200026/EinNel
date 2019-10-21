#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

def predictModel(arr):
    empdata = np.array(arr)
    dataset=pd.read_csv("employee_dataint.csv")

    X=dataset.iloc[:,:35].values

    X=np.delete(X,24,1)
    X=np.delete(X,9,1)

    y=dataset['PerformanceRating'].values


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = None)


    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    row=sc.transform(empdata.reshape(1,-1))


    logisticregression = LogisticRegression(solver='liblinear', multi_class='ovr')
    logisticregression.fit(X_train, y_train)

    y_pred = logisticregression.predict(X_test)
    y_pred1= logisticregression.predict(row)


    #lets see the actual and predicted value side by side
    y_compare = np.vstack((y_test,y_pred)).T
    #actual value on the left side and predicted value on the right hand side
    #printing the top 5 values

    # Making the Confusion Matrix

    cm = confusion_matrix(y_test, y_pred)

    #finding accuracy from the confusion matrix.
    a = cm.shape
    corrPred = 0
    falsePred = 0
    for row in range(a[0]):
        for c in range(a[1]):
            if row == c:
                corrPred +=cm[row,c]
            else:
                falsePred += cm[row,c]
    returndict = {'accuracy':corrPred/(cm.sum()), 'result':y_pred1}
    return returndict
