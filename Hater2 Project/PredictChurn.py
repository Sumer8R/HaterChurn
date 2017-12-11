# -*- coding: utf-8 -*-
"""
Haters Group 2
Alexander Lambert
"""

import csv
import sklearn as sk
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import matplotlib.colors as co
import sklearn.datasets
import sklearn.model_selection
import sklearn.neural_network
import sklearn.naive_bayes 
import sklearn.linear_model
import sklearn.svm
import sklearn.tree
import sklearn.ensemble

"""
This file is ready for use predicting new behavior 
This file can be used for two different prediction methods
It can run and predict returners based on individual event monitoring
Or it can run on daily total event monitoring
It does not understand the temporal nature of daily event monitoring, yet still has decent predictions
"""
#X is the training input
#y is the training classifier
#X_pred is the prediction input
X = []
X_pred = []
y = []

# Length of monitoring period
X_len = 7
# distance = 1 and limit = 1 for next column
# distance is days after the monitoring period to start checking/predicting for returns
distance = 1
# Number of days to check or predict for. Can be set to a large number such as float('inf')
# to check and predict for all days in data after the start day noted by distance
limit = 1
# This part reads in a csv file in the format of the haters database download and extracts features for training
with open('ENTER TRAINING FILE NAME HERE') as file:
    read = csv.reader(file)
    for row in read:
        temp_X = []
        temp_y = []
        for i,r in enumerate(row):
            #FIRST TWO ROWS ARE ID AND CREATED DATE FOR TESTING
            if i > 1 and i < X_len + 2:
                temp_X += [r.replace(',','')]
            elif i > 1 and i >= X_len + distance + 1 and i < X_len + distance + limit + 1:
                temp_y += [r.replace(',','')]
            #USE THIS INSTEAD IF ALL COLUMNS ARE DATA 
            """
            if i < X_len:
                temp_X += [r.replace(',','')]
            elif i >= X_len + distance - 1 and i < X_len + distance + limit - 1:
                temp_y += [r.replace(',','')]
            """
        X += [temp_X]
        y += [temp_y]

#This part will read in the prediction set
with open('ENTER PREDICTION FILE NAME HERE') as file:
    read = csv.reader(file)
    for row in read:
        temp_X = []
        for i,r in enumerate(row):
            #FIRST TWO ROWS ARE ID AND CREATED DATE FOR TESTING
            if i > 1 and i < X_len + 2:
                temp_X += [r.replace(',','')]
            #USE THIS INSTEAD IF ALL COLUMNS ARE DATA 
            """
            if i < X_len:
                temp_X += [r.replace(',','')]
            """
        X_pred += [temp_X]
 
# casts the arrays from the csv file to numpy arrays
X = np.array(X).astype('float')
y = np.array(y).astype('int')
X_pred = np.array(X_pred).astype('float')

#This will have no affect if there is individual events being monitored
#This will sum the total usage of days that are going to be predicted for
y = np.sum(y, axis = 1)

#This will change the y values to a 0/1 classification prediction
y = [1 if y[t] > 0 else 0 for t in range(len(y))]
y = np.array(y)

#Preprocesses data since some features are drastically more spread out than others
X1 = sk.preprocessing.normalize(X)
X2 = sk.preprocessing.scale(X)
X1_pred = sk.preprocessing.normalize(X_pred)
X2_pred = sk.preprocessing.scale(X_pred)

datasets = [(X,y), (X1,y), (X2,y)]
datasetsname = ["Raw Data", "Normalized Data", "Scaled Data"]
datasets_pred = [X_pred, X1_pred, X2_pred]

#computes the prediction for all three prediction datasets after training on the equivalent training dataset
for f,i in enumerate(datasets):
        
    inp = i[0]
    clas = i[1]    
    
    reg = sk.neural_network.MLPClassifier(activation = 'relu', hidden_layer_sizes=(100,50,20))
    reg.fit(inp,clas)
    pred = reg.predict(datasets_pred[f])
    np.savetxt('mat_X' + str(f) +'.csv', pred, delimiter=',', fmt='%i')
    