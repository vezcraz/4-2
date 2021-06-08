import pandas as pd
import numpy as np
import os
import math
from sortedcontainers import *
os.chdir('.')

path = os.getcwd()
# print(path)
df = pd.read_excel('./output_Format1.xlsx')

# print(len(df))
l = []
s=SortedSet()
for index, row in df.iterrows():
    temp = {}
    if row['Catalog'][1]!='1':
        continue
    row['Section'] = row['Section'][0:-2]
    temp['Course'] = row['Subject'] +' '+row['Catalog']
    temp['Section'] = row['Section']
    temp['Type'] = row['Section'][0]
    days = []
    flag=0;
    x = row['Class Pattern']
    if not isinstance(x,str):
        continue
    for i in range(len(x)):
        if x[i]=='H':
            days[i-1] = days[i-1]+"H"
            flag=1
        else:           
            days.append("")
            days[i-flag] = x[i]
    for day in days:
        temp['Day'] = day
        temp['Start'] = row['Mtg Start']
        temp['End'] = row['End time']
        if isinstance(temp['Start'], float) and math.isnan(temp['Start']):
            continue
        else:
            x=temp
            tempList = list(x.items())
            day = tempList[-3]
            stime = tempList[-2]
            etime = tempList[-1]
            tempList.remove(day)
            tempList.remove(stime)
            tempList.remove(etime)
            tempList.insert(0,day)
            tempList.insert(1,stime)
            tempList.insert(2,etime)
                    
            s.add(tuple(tempList))

lst=[]
for x in s:
    lst.append(dict(x))
           
            
inp1_df = pd.DataFrame(lst)     




