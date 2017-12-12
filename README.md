# HaterChurn
Hater group 2 BU Spark

DATA:

TIMELINE_TOTAL_ENTRIES_50.csv:
(74355,52)
This file contains over 74,000 unique IDs as rows and each collumn represents a single day's total activity, starting from the user's first day. 
The leading two columns are ID and the user's created date.

TIMELINE_TOTAL_ENTRIES_Tester.csv:
(50000,50)
This file is the first 50,000 rows of TIMELINE_TOTAL_ENTRIES_50.csv. 
Each row corresponds to the same row in Linear Models Testing Set.csv.
The leading two columns have been removed, so every column is now daily activity data.

Linear Models Testing Set.csv:
(50000,7)
This file contains 50,000 linear models created for matching purposes with future models. 
Each row corresponds to the same row in TIMELINE_TOTAL_ENTRIES_Tester.csv and TIMELINE_TOTAL_ENTRIES_50.csv.
Each column corresponds to a y value for a temporal graph.

HATERSDATA_ONEDAY_ONEWEEK_TOTAL_EVENTMATCHES.csv:
(43340,21)
The first 15 columns are counts of the following data in a one day time span:
id, total messages, created date, user sex, matches, photos viewed, profiles viewed,
no recommendation notifactions sent, icebreakers completed, photos added,
topics answered, recomendations answered, dating mode visits, session start event,
total app events

The last 6 columns are counts of the following data for the life of the account starting after one week:
session start event, Datemode visited, message events, topic answered, reccomendation answered, total app events

The first 15 columns are meant to be used as the inputs for a neural net to be trained on. 
Excluding the first 3 columns, which are just for documentation.
The last 6 can be chosen from to create the classifcation for churn.





Python Files:

HatersTimeline.py:

TEST FILE
Run with 2 types of data. Either data similar to what is found in HATERSDATA_ONEDAY_ONEWEEK_TOTAL_EVENTMATCHES.csv or TIMELINE_TOTAL_ENTRIES_50.csv.
This file can be used for two different prediction methods.
It can run and predict returners based on individual event monitoring with data from HATERSDATA_ONEDAY_ONEWEEK_TOTAL_EVENTMATCHES.csv.
Or it can run on daily total event monitoring with data from TIMELINE_TOTAL_ENTRIES_50.csv.
It does not understand the temporal nature of daily event monitoring, yet still has decent predictions.
To run, insert file name where it says to and run the entire file. It will output it's prediction accuracy and some statistics.

TimelineSearch.py:

TEST FILE
This file is similar to HatersTimeline.py.
I reccomend understanding that file first.
This file is used to show the relation between changing the monitoring length, prediction day length, and what day is predicted.
It is currently set to run every monitoring length and to predict the next day.
The monitoring length is the amount of days that the neural net will take as input.
The prediction day length is the period of time that the neural net will try to predict a return during.
This file should be run with the data from TIMELINE_TOTAL_ENTRIES_50.csv.
To run, insert the file name where it says to and run the whole file. It may take up to a half hour to run and will output a graph detailing the accuracy.

PredictChurn.py:

This file is ready for use predicting new behavior.
This file can be used for two different prediction methods.
It can run and predict returners based on individual event monitoring.
Or it can run on daily total event monitoring.
It does not understand the temporal nature of daily event monitoring, yet still has decent predictions.
To run this file, enter the file name of the training set where it says to, and enter the name of the prediction set underneath.
The training set should have the same monitoring length as the prediction set, but have the information about wheather or not those users returned.
The prediction set should just have the information of a user's usage so far, 
and the file will write out a csv file with the predictions for each person in that set.
I reccomend using one week monitoring for the best results. 

Linear Regression Modelling.py:

This file is used to create linear models for users' daily usage. 
There are several ways to use this file. 
Firstly, the training set must always have the full raw data for each user. 
I provided TIMELINE_TOTAL_ENTRIES_Tester.csv which can be used.
A set of models for the training set can then be uploaded or created, but should have the same amount of days as the prediction set, not the training set. 
I have provided one named Linear Models Testing Set.csv.
The prediction will be used to create models, and then the models will be compared against the previous created training models to find the most similar.
Then it can use the full raw data for the training set to determine if these users will return.
To run this file you should follow these steps:
create('training file.csv', 'prediction file.csv')
reader('training models.csv') 
train_predictions()
simularity()
comeback(predicted day)












