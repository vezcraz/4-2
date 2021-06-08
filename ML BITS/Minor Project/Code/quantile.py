#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:10:46 2021

@author: vezcraz
"""
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier,AdaBoostClassifier, VotingClassifier
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from imblearn.combine import SMOTEENN 
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from sklearn.model_selection import train_test_split
import time
from sklearn.linear_model  import  LogisticRegression
def plotter(x):
    plt.hist(x, bins=100)
    plt.show()
def transform(x):
    
    for i in range(len(x[0])):
        quantile = QuantileTransformer(output_distribution='normal')
        data = quantile.fit_transform(x[:,i].reshape(-1,1))
        x[:,i] = np.transpose(data)
    return x       
pca = False
df = pd.read_csv("./train.csv")
modeValues={}
for col in df:
    modeValues[col] = df[col].mean()
df.fillna(value = modeValues, inplace=True)
del df['id']
y = df['Result'].values
del df['Result']
x = df.values
x = transform(x)
X = StandardScaler().fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2, random_state=42, stratify=y)
#resample = SMOTEENN()    
#X_train, y_train = resample.fit_resample(X_train, y_train)
#m1=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(
#        max_depth=2),n_estimators=200)
#clf = RandomForestClassifier(n_estimators=100, random_state=1)
#m3 = GradientBoostingClassifier(n_estimators=200, 
#      learning_rate=1.0,max_depth=1, random_state=0)
m2 = SVC(gamma='auto', probability = True)
m3 = LogisticRegression(random_state=0, tol = 1e-5)
clf =  VotingClassifier(estimators=[
         ('svm', m2), ('lr',m3)],
        voting='soft')
#heatMap(pd.DataFrame(x)) -->no correlation found
#clf.fit(X_train, y_train)
parameters= [{'C':[1,5,10,20,50]}]

clf = GridSearchCV(m3,parameters,
                    scoring='f1', cv=3)
#clf = LogisticRegression(random_state=0)
clf.fit(X,y)

#y_pred = clf.predict(X_test)
#f1_score(y_test,y_pred)


#--submission
test_df = pd.read_csv('./test.csv')
del test_df['id']
test_df.fillna(value = modeValues, inplace=True)
test_x = test_df.values
test_x = transform(test_x)
test_x = StandardScaler().fit_transform(test_x)

ans=list(clf.predict(test_x).astype(int))
fin = np.arange(len(test_df))
finList = list(zip(fin,ans ))
finDf = pd.DataFrame(finList, 
               columns =['id', 'Expected']) 
finDf.to_csv('./submission.csv', index = False) 

