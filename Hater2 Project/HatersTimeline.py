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
This is a test file to find the best system of analysis
This file can be used for two different prediction methods
It can run and predict returners based on individual event monitoring
Or it can run on daily total event monitoring
It does not understand the temporal nature of daily event monitoring, yet still has decent predictions
"""
X = []
#X2 = []
y = []

# Length of monitoring period
X_len = 7
# distance = 1 and limit = 1 for next column
# distance is days after the monitoring period to start checking/predicting for returns
distance = 1
# Number of days to check or predict for. Can be set to a large number such as float('inf')
# to check and predict for all days in data after the start day noted by distance
limit = 1
# This part reads in a csv file in the format of the haters database download and extracts features for testing and predicting
with open('ENTER FILE NAME HERE') as file:
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
 
# casts the arrays from the csv file to numpy arrays
X = np.array(X).astype('float')
y = np.array(y).astype('int')


#This will have no affect if there is individual events being monitored
#This will sum the total usage of days that are going to be predicted for
y = np.sum(y, axis = 1)

#This will change the y values to a 0/1 classification prediction
y = [1 if y[t] > 0 else 0 for t in range(len(y))]
y = np.array(y)

#Preprocesses data since some features are drastically more spread out than others
X1 = sk.preprocessing.normalize(X)
X2 = sk.preprocessing.scale(X)


print("CONTROL: ")
#Shows a random guesser (always 50% since the only options are 0/1)
con = np.sum(np.absolute(np.random.randint(2, size = len(y)) - y))/ len(y)
#Shows a naive guesser (predicts that everyone returns)
acc = np.sum(y)/len(y)
#print(con,y)
print(con, acc, "\n\n")

datasets = [(X,y), (X1,y), (X2,y)]#sk.datasets.make_moons(noise=0.3, random_state=0), sk.datasets.make_circles(noise=0.2, factor=0.5, random_state=1), (X,y), (X1,y)]
datasetsname = ["Raw Data", "Normalized Data", "Scaled Data"]

best_name = ""
best_score = 0

val = 1
for f,i in enumerate(datasets):
    
    
    inp = i[0]
    clas = i[1]
    
    #splits up data into testing and training sets
    X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(inp, clas, test_size=.2, random_state=42)
    
    
    
    testers = [sk.neural_network.MLPClassifier(activation = 'relu', hidden_layer_sizes=(100,50,20), max_iter = 2000), sk.linear_model.LogisticRegression(), sk.ensemble.RandomForestClassifier(criterion='entropy')] #sk.svm.SVC(kernel='rbf', probability = True)]
    testersname = ["Neural Net", "Logistic Regression", "Random Forest"]
    
    #trains each system on each set of data and then outputs success rate
    for t,j in enumerate(testers):
        print("-------------------------------------------------")
        reg =  j
        reg.fit(X_train,y_train)
        score = reg.score(X_test,y_test)
        pred = reg.predict(X_test)
        conf_mat = sk.metrics.confusion_matrix(y_test, pred)
        precision, recall, thresholds = sk.metrics.precision_recall_curve(y_test, pred)
        
        name = testersname[t] + " | " + datasetsname[f]
        
        print(name, ":\n")
        print("Accuracy: ", score)
        sco = (score - (1 - acc)) * 100
        print("Score: ", sco, "%")
        # Correct Red |  False Blue
        #  False Red  | Correct Blue 
        print("Confusion Matrix: \n", conf_mat)
        print(sk.metrics.classification_report(y_test, pred, target_names=['1', '0']))
        print("Log Loss Entropy: ", sk.metrics.log_loss(y_test, pred))
        print("\n\n")
       
        if sco > best_score:
            best_score = sco
            best_name = name
        
        val+=1
        
        #Plots ROC curve to examine true positive rate vs false positive rate
        fpr, tpr, threshold = sk.metrics.roc_curve(y_test, pred)
        roc_auc = sk.metrics.auc(fpr, tpr)
        plt.figure()
        lw = 2
        plt.plot(fpr, tpr, color='darkorange',
                 lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic example')
        plt.legend(loc="lower right")
        plt.show()

print("Best Results: ")
print(best_name + ": ", str(best_score))


