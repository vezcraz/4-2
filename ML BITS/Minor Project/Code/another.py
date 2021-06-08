#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:10:46 2021
 
@author: vezcraz
"""
 
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from scipy import stats
import pandas as pd
def heatMap(x):
    import seaborn as sns
    %matplotlib inline
    corr = x.corr()
    sns.heatmap(corr, 
            xticklabels=corr.columns,
            yticklabels=corr.columns)
changed = []
pca=False
def logTransformTrain(x):
    for i in range(len(x[0])):
        avg=0
        for j in range(40):
            avg+= stats.shapiro(np.random.choice(x[:,i],200))[1]
        val = avg/40
        print(val)
        if val<0.004:
            changed.append(i)
            for j in range(len(x)):
                if(x[j,i]>=0):
                    x[j,i]=np.log(x[j,i]+1)
                else:
                    x[j,i]=-np.log(1-x[j,i])
    return x       
def logTransformTest(x):
    for i in changed:
        for j in range(len(x)):
            if(x[j,i]>=0):
                x[j,i]=np.log(x[j,i]+1)
            else:
                x[j,i]=-np.log(1-x[j,i])
    return x       
df = pd.read_csv("./train.csv")
modeValues={}
for col in df:
    modeValues[col] = df[col].mode()
del df['id']
y = df['Result'].values
del df['Result']
x = df.values
x = logTransformTrain(x)
x = StandardScaler().fit_transform(x)
#heatMap(pd.DataFrame(x))
if pca:
    train_x = x
    u, s, vt = np.linalg.svd(x, full_matrices=False)
    pref = np.cumsum(s)
    for i in range(100):
        print(i,pref[i]*100/pref[99])
    r=100
    u = u[:,:r]
    s = s[:r]
    vt = vt[:r]
    x = u*s
#heatMap(pd.DataFrame(x))
from sklearn.linear_model  import  LogisticRegression
clf = LogisticRegression(random_state=0)
clf.fit(x, y)
ans = []
test_df = pd.read_csv('./test.csv')
del test_df['id']
for i in range(len(test_df.columns)):
    test_df.iloc[:,i] = test_df.iloc[:,i].fillna(test_df.iloc[:,i].median())
test_x = test_df.values
test_x = logTransformTest(test_x)
test_x = StandardScaler().fit_transform(test_x)
if pca:
    test_x = test_x@np.transpose(vt)
for i in range(len(test_df)):
    ans.append(int(clf.predict([test_x[i]])[0]))
fin = np.arange(len(test_df))
finList = list(zip(fin,ans ))
finDf = pd.DataFrame(finList, 
               columns =['id', 'Expected']) 
finDf.to_csv('./submission.csv', index = False) 
 