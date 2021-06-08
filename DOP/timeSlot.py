from config import *

def getTime(course, section):
    lst = []
    for idx, row in inp1_df.iterrows():
        if(row['Course'] == course  and  row['Section'] == section):
            st = int(row['Start'][0:2])
            en = int(row['End'][0:2])
 
            if(en - st == 1):
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st 
                lst.append(temp_slot)
 
            elif(en - st == 2):
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st 
                lst.append(temp_slot)
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st + 1
                lst.append(temp_slot)

            elif(en - st == 3):
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st 
                lst.append(temp_slot)
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st + 1
                lst.append(temp_slot)
                temp_slot = Slot()
                temp_slot.day = row['Day']
                temp_slot.startTime = st + 2
                lst.append(temp_slot)
    
    return lst