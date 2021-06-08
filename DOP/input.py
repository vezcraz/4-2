from config import *
from timeSlot import *

def inputEG():
    global numberOfCoursesEG

    for idx, row in inp2_df.iterrows():
        courseName = row['Course'] + " " + row['Section'][0]
        sectionName = row['Course'] + " " + row['Section']
        if(courseName not in courseListEG):
            continue 

        index = courseListEG.index(courseName)
        temp_sec = Section()
        temp_sec.name = sectionName
        temp_sec.capacity = int(row['Capacity'])
 
        temp_sec.timing = getTime(row['Course'], row['Section'])
        fieldEG[index].append(temp_sec)

    k = 20 - len(courseListEG)
    for i in range(k):
        fieldEG.pop()

def inputWS():
    global numberOfCoursesWS

    for idx, row in inp2_df.iterrows():
        courseName = row['Course'] + " " + row['Section'][0]
        sectionName = row['Course'] + " " + row['Section']
        if(courseName not in courseListWS):
            continue 

        index = courseListWS.index(courseName)
        temp_sec = Section()
        temp_sec.name = sectionName
        temp_sec.capacity = int(row['Capacity'])
 
        temp_sec.timing = getTime(row['Course'], row['Section'])
        fieldWS[index].append(temp_sec)

    k = 20 - len(courseListWS)
    for i in range(k):
        fieldWS.pop()

    i = numberOfCoursesPureEG
    j = numberOfCoursesPureWS
    common = numberOfCoursesEG - numberOfCoursesPureEG

    for k in range(common):
        fieldWS[j+k] = fieldEG[i+k]
