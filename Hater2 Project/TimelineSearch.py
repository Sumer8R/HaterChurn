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
This file is similar to HatersTimeline.py 
I reccomend understanding that file first
This file is used to show the relation between 
changing the monitoring length, prediction day length, and what day is predicted
It is currently set to 
"""
toppest_top = 0
toppest_bot = 0
toppest_name = ""
toppest_score = 0

toppest_mat = []
xx = 1
for top in range(1,50):
    for bot in range(1, 2):#72 - top):
        
        X = []
        #X2 = []
        y = []
        
        #SWITCH top AND xx TO HAVE CONSTANT MONITORING LENGTH AND CHANGING PREDICTION LENGTH
        X_len = top
        # 1 and 1 for next column
        #I reccomend keeping distance to 1. unless you want some gap between the monitoring period and when you're looking for a return
        distance = 1
        limit = xx
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
         
        
        X = np.array(X).astype('float')
        #X2 = np.array(X2).astype('float')
        y = np.array(y).astype('int')
        print(y.shape)
        
        
        
        y = np.sum(y, axis = 1)
        
        y = [1 if y[t] > 0 else 0 for t in range(len(y))]
        y = np.array(y)
        
        X1 = sk.preprocessing.normalize(X)
        X2 = sk.preprocessing.scale(X)
        #X3 = np.average(X, axis = 0)
        
        
        #print(X)
        #print(X1)
        #print(X2)
        #print(X3)
        
        
#        print("CONTROL: ")
#        con = np.sum(np.absolute(np.random.randint(2, size = len(y)) - y))/ len(y)
        acc = np.sum(y)/len(y)
#        #print(con,y)
#        print(con, acc, "\n\n")
        
        datasets = [(X,y), (X1,y), (X2,y)]#sk.datasets.make_moons(noise=0.3, random_state=0), sk.datasets.make_circles(noise=0.2, factor=0.5, random_state=1), (X,y), (X1,y)]
        datasetsname = ["Raw Data", "Normalized Data", "Scaled Data"]
        
        best_name = ""
        best_score = 0
        
        val = 1
        for f,i in enumerate(datasets):
            
            
            inp = i[0]
            clas = i[1]
            
            X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(inp, clas, test_size=.2, random_state=42)
            
            
            
            testers = [sk.neural_network.MLPClassifier(activation = 'relu', hidden_layer_sizes=(50,), max_iter = 2000)]#, sk.linear_model.LogisticRegression(), sk.ensemble.RandomForestClassifier(criterion='entropy')] #sk.svm.SVC(kernel='rbf', probability = True)]
            testersname = ["Neural Net"]#, "Logistic Regression", "Random Forest"]
            
            for t,j in enumerate(testers):
                #print("-------------------------------------------------")
                reg =  j
                #reg =  sk.linear_model.LogisticRegressionCV()
                reg.fit(X_train,y_train)
                score = reg.score(X_test,y_test)
                #pred = reg.predict(X_test)
                #conf_mat = sk.metrics.confusion_matrix(y_test, pred)
                #precision, recall, thresholds = sk.metrics.precision_recall_curve(y_test, pred)
                
                name = testersname[t] + " | " + datasetsname[f]
                
                #print(name, ":\n")
                #print("Accuracy: ", score)
                acc2 = acc
                if acc < .5:
                    sco = (score - (1 - acc)) * 100
                    acc2 = 1 - acc
                else:
                    sco = (score - acc) * 100
                #print("Score: ", sco, "%")
                # Correct Red |  False Blue
                #  False Red  | Correct Blue 
                #print("Confusion Matrix: \n", conf_mat)
                #print("Precision: ", precision)
                #print("Recall: ", recall)
                #print("Thresholds: ", thresholds)
                #print(sk.metrics.classification_report(y_test, pred, target_names=['1', '0']))
                #print("Accuracy: ", sk.metrics.accuracy_score(y_test, pred))
                #print("Log Loss Entropy: ", sk.metrics.log_loss(y_test, pred))
                #print("\n\n")
               
                if sco > best_score:
                    best_score = sco
                    best_name = name
        
        toppest_mat += [[top, bot, best_name, acc2, best_score]]
        
        print(top, bot)
        
        if best_score > toppest_score:
            toppest_score = best_score
            toppest_name = best_name
            toppest_top = top
            toppest_bot = bot

#graphs the best results from each iteration     
print("Best Results: ")
print(toppest_name)
print("Score: ", toppest_score)
print("Days considered for modelling: ", toppest_top)
print("Days considered for testing: ", toppest_bot)

f = open( 'mat_X.txt', 'w' )
f.write(str(toppest_mat))
f.close()

accur = [i[3]*100 for i in toppest_mat]
bestscore = [(i[3]*100) + i[4] for i in toppest_mat]
advantage = [i[4] for i in toppest_mat]
x_val = range(1,50-xx +1)

plt.figure(figsize=(25,35))
plt.plot(x_val, accur, 'r',  label='Guessing')
plt.plot(x_val, bestscore, 'b', label='Neural Net')
plt.plot(x_val, advantage, 'g',  label='Difference' )
plt.xticks(range(0,50-xx+1))
plt.yticks(range(0,101, 5))
plt.xlabel('Length of Days Checked for a Return')
plt.ylabel('Percent Correct')
plt.title("Guessing Vs Neural Net")
plt.grid(True)
plt.legend(loc="lower right")