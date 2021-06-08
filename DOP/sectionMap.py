from config import *
from timeSlot import *

def createSectionMap():
    for idx, row in inp2_df.iterrows():
        courseName = row['Course'] + " " + row['Section'][0]
        if(courseName not in courseListAll):
            continue 
        sectionName = row['Course'] + " " + row['Section']
        timing = getTime(row['Course'], row['Section'])
        sectionTimeMap[sectionName] = timing