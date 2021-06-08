#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:10:46 2021

@author: vezcraz
"""

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import time
def heatMap(x):
    import seaborn as sns
    %matplotlib inline
    corr = x.corr()
    sns.heatmap(corr, 
            xticklabels=corr.columns,
            yticklabels=corr.columns)
changed = []
pca=False
def transform(x):
    for i in range(len(x[0])):
        quantile = QuantileTransformer(output_distribution='normal')
        data = quantile.fit_transform(x[:,i].reshape(-1,1))
        x[:,i] = np.transpose(data)
#        plt.hist(data, bins=100)
#        plt.show()
    return x       
    
df = pd.read_csv("./train.csv")
modeValues={}
for col in df:
    modeValues[col] = df[col].mean()
df.fillna(value = modeValues, inplace=True)
del df['id']
y = df['Result'].values
del df['Result']
correlated_features = set()

for i in range(len(df.columns)):
    if df.iloc[:,i].var()<0.3:
        correlated_features.add(df.columns[i])
correlation_matrix = df.corr()
df.drop(labels=correlated_features, axis=1, inplace=True)
temp1 = correlated_features
correlated_features = set()
for i in range(len(correlation_matrix .columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.7:
            colname = correlation_matrix.columns[i]
            correlated_features.add(colname)
temp2 = correlated_features
df.drop(labels=correlated_features, axis=1, inplace=True)
x = df.values
x = transform(x)
x = StandardScaler().fit_transform(x)
from sklearn.linear_model  import  LogisticRegression
clf = LogisticRegression(random_state=40, tol = 1e-6, max_iter=500,
                         penalty='l2', solver = 'newton-cg')
clf.fit(x, y)
ans = []
test_df = pd.read_csv('./test.csv')
del test_df['id']
test_df.fillna(value = modeValues, inplace=True)
test_df.drop(labels=temp1, axis=1, inplace=True)
test_df.drop(labels=temp2, axis=1, inplace=True)
test_x = test_df.values
test_x = transform(test_x)
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

