import pandas as pd
import sys
import time
import datetime
df = pd.read_csv('org.csv')
data = pd.DataFrame([df['end_date'], df['vaccines'], df['population'], df['dose']]).transpose()
data = data.groupby(['dose','end_date']).sum()
data.reset_index(inplace=True)
pop = data['population'][0]
data=data.drop(['population'], axis=1)

def getDateTime(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')
def extrapolate(data, typeOfDose):
    curr = getDateTime('2020-12-08')
    lst = [{'date':curr, 'vaccines':0}]
    
    for index, row in data.iterrows():
        if row['dose']==typeOfDose:
            end = getDateTime(row['end_date'])
            div = (row['vaccines']-lst[-1]['vaccines'])/((end-curr).days )
            for i in range((end-curr).days):
                lst.append({'date':lst[-1]['date']+datetime.timedelta(days=1), 
                            'vaccines':int(lst[-1]['vaccines']+div)})
            
            curr=end
    return pd.DataFrame(lst)

data_dose1 = extrapolate(data,'1st dose')
data_dose2 = extrapolate(data,'2nd dose')

