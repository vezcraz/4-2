import pandas as pd
import numpy as np
import os
import math
from sortedcontainers import *
os.chdir('.')

df = pd.read_excel('first.xlsx')
inp2_df = pd.DataFrame()
for index, row in df.iterrows():
    tempStr = row['COURSE SEC']
    temp = tempStr.split(' ')
    tempRow = {}
    tempRow['Course'] = temp[0]+' ' + temp[1]
    # print(temp)
    tempRow['Section'] = temp[2]
    tempRow['Capacity'] = row['TOT SEC CAP']
    # print(row['TOT SEC CAP'])
    inp2_df=inp2_df.append(tempRow, ignore_index = True)

# for index, row in inp2_df.iterrows():
# 	print('{} {} {}'.format(row['Course'], row['Section'], row['Capacity']))