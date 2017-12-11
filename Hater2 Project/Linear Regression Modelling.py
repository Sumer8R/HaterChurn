# -*- coding: utf-8 -*-
"""
Haters Group 2
Alexander Lambert
"""


import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR


"""
X is the days of the usage data
X2 is the shortened days of the usage data
y is the list tester inputs shortened to the desired length
y_pred is the list of people's data to be matched to a model from y
full_y is the full data of the people in y, used to show future of predicted models
"""
X = []
X2 = []
y = []
y_pred = []
full_y= []
test =[]    
    
    
def create(file1, file2, file3='', trained=False):
    """
    sample input: create('Haters_Data_Mit_Events.csv', 'Haters_Data_Mit_Events_Second.csv', 'Linear Models Testing Set.csv', trained=True)
    Used to import the csv files downloaded from the Haters database
    file1 = data of tester set, should have more data than the set you want to predict. Reccomended 20+ days
    file2 = data of prediction set, should have less data than the tester set. Reccomended 7- days
    file3 = Saved data of models trained off of the data in file 1. 
    """
    global X
    global X2
    global y
    global full_y
    global y_pred
    
    #reads csv files with the delimiter used by the Haters database
    full_y = np.genfromtxt(file1, delimiter=',')
    y_pred = np.genfromtxt(file2, delimiter=',')
    #create shortened tester data to match prediction set
    y = [i[:y_pred.shape[1]] for i in full_y]
    
    #creates list of days from 1 to full length of tester data
    for i in range(1, len(full_y[0]) + 1):
        X += [[i]]
    #creates list of days from 1 to length of 
    for i in range(1,len(y[0]) + 1):
        X2 += [[i]]
     
    
    X = np.array(X).astype('float')
    X2 = np.array(X2).astype('float')
    y = np.array(y).astype('float')
    full_y = np.array(full_y).astype('float')
    
    # if input trained is set to True, read in the trained tester data models along with the tester data
    if trained == True:
        reader(file3)
    
"""
models_lin is the linear models of the tester data
models_lin_pred is the linear models of the prediction set
models_lin_check is a linear model for the full tester set`
"""
models_lin = []
models_lin_pred = []
models_lin_pred_check = []

    
def train_testers():
    """
    Trains the tester set
    Needs y already defined as input for models_lin
    """
    global models_lin
    global models_lin_pred
    global models_lin_pred_check
    
    for i,j in enumerate(y):
        #Switch kernel to 'rbf' for an almost exact fit
        svr_lin = SVR(kernel='linear', C=1)
        models_lin += [svr_lin.fit(X2, j).predict(X2)]
    
    models_lin = np.array(models_lin)
    

def train_predictions():
    """
    Trains the prediction set
    Needs y_pred already defined for input to models_lin_pred
    """
    global models_lin
    global models_lin_pred
    global models_lin_pred_check
    
    for i,j in enumerate(y_pred):
        #Switch kernel to 'rbf' for an almost exact fit
        svr_lin = SVR(kernel='linear', C=1)
        models_lin_pred += [svr_lin.fit(X2, j).predict(X2)]
    
    models_lin_pred = np.array(models_lin_pred)
    


def save(file1, mat1, file2='2.csv', mat2=[], file3='3.csv', mat3=[], checker=False, checker2=False):
    """
    sample input: reader('Linear Models Testing Set.csv', models_lin file2 = 'Linear Models Prediction Set.csv', mat2=models_lin_pred checker=True)
    Saves up to 3 matrixes to csv
    """
    np.savetxt(file1, mat1, delimiter=' ')
    if checker == True:
        np.savetxt(file2, mat2, delimiter=' ')
    if checker2 == True:
        np.savetxt(file3, mat3, delimiter=' ')
    
    
def reader(file1, file2='2.csv', file3='3.csv', checker=False, checker2=False):
    """
    sample input: reader('Linear Models Testing Set.csv', file2 = 'Linear Models Prediction Set.csv', checker=True)
    Reads up to three csv files
    file1 = models_lin (tester modelled data)
    file2 = models_lin_pred (prediction modelled data)
    file3 = models_lin_pred_check (full tester set modelled data)
    """
    global models_lin
    global models_lin_pred
    global models_lin_pred_check
    
    models_lin = np.genfromtxt(file1, delimiter=' ')
    if checker == True:
        models_lin_pred = np.genfromtxt(file2, delimiter=' ')
    if checker2 == True:
        models_lin_pred_check = np.genfromtxt(file3, delimiter=' ')


"""
sim is an array of the most similar temporal graphs with indexes the same as those in models_lin_pred
"""
sim = []
def simularity():
    """
    Calculates the simularity between two sets of models using euclidean distance
    Needs models_lin and models_lin_pred with the second axis the same size (aka the same amount of features)
    """
    global sim
    for i,vec in enumerate(models_lin_pred):
        best_sim = float("inf")
        best_model = -1
        for j,vec2 in enumerate(models_lin):
            simil = np.sqrt(np.sum(np.subtract(vec, vec2)**2))
            if simil < best_sim:
                best_sim = simil
                best_model = j
        sim += [best_model]

"""
returners are a 1 for a person who returns and 0 for a nonreturner
The indexes are the same as lin_models_pred
"""
returners = []
def comeback(day):
    """
    Predicts if a person will return to the app based on the useage of the the person with the most similar usage during the monitoring period
    day = int to represnt what day to check if a user will return. Should be larger than the monitoring period
    """
    global sim
    global full_y
    global returners
    
    returners = []
    if day > full_y.shape[1]:
        return "Not enough days in data"
    else:
        for i,ind in enumerate(sim):
            if full_y[ind][day-1] > 0:
                returners += [1]
            else: 
                returners += [0]
    returners = np.array(returners)


def plot(fir, sec, checker=False):
    """
    sample input: plot(sim[20],20)
    plots specified pair of models from the testing set and prediction set along with the testing set's full daily usage data
    used to visualize model simularity and future prediction
    """
    lw = 2
    plt.figure(figsize = (15,10))
    plt.scatter(X, full_y[fir], color='darkorange', label='data')
    plt.plot(X2, models_lin_pred[sec], color='green', lw=lw, label='Predicted Model')
    plt.plot(X2, models_lin[fir], color='cornflowerblue', lw=lw, label='Tester Model')
    if checker == True:
        plt.plot(X, models_lin_pred_check[sec], color='navy', lw=lw, label='Full Predicted Model')
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
