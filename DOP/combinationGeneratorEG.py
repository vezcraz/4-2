from config import *

def dfs1():
    global stopEG1, smEG, numberOfCoursesEG
    temp = [] 
    p = []
    clashCheck = {}

    for i in range(numberOfCoursesEG):
        for j in range(len(fieldEG[i])):
            sec = fieldEG[i][j]
            if(sec.capacity == 0):
                continue
            timing = sec.timing
            clashing = False

            for k in range(len(timing)):
                key = str(timing[k])
                if(key in clashCheck):
                    clashing = True
                    break

            if(clashing == False):
                temp.append(sec)
                p.append([i,j])
                for k in range(len(timing)):
                    key = str(timing[k])
                    clashCheck[key] = True;
                break;

    if(len(temp) != numberOfCoursesEG):
        stopEG1 = True
        return

    pathsEG.append(temp)
    mn = temp[0].capacity
    for i in temp:
        mn = min(mn, i.capacity)

    capacityArrayEG.append(mn)

    smEG += mn
    for i in range(len(temp)):
        x = p[i][0]
        y = p[i][1]

        fieldEG[x][y].capacity -= mn

        if(fieldEG[x][y].capacity == 0):
            fieldEG[x].pop(y)
            if(len(fieldEG[x]) == 0):
                stop = True

def getEGCombinationsStage1():
    global stopEG1
    while(not stopEG1):
        dfs1()

def remPart(temp, count):
    global smEG, numberOfCoursesPureEG
    clashCheck = {}
    path = []

    for i in temp:
        clashCheck[i] = True

    cx = numberOfCoursesPureEG

    for it0 in fieldEG[cx-1]:
        for it1 in fieldEG[cx]:
            for it2 in fieldEG[cx + 1]:
                for it3 in fieldEG[cx + 2]:
                    for it4 in fieldEG[cx + 3]:
                        for it5 in fieldEG[cx + 4]:
                            for it6 in fieldEG[cx + 5]:
                                tempDict = {}
                                tempDict = clashCheck
                                arr = [it0, it1, it2, it3, it4, it5, it6]

                                success = True

                                for i in arr:
                                    lst = i.timing

                                    for it in lst:
                                        if(it in tempDict):
                                            success = False

                                    if(success == False):
                                        break

                                    for it in lst:
                                        tempDict[it] = True

                                if(success == True):
                                    path = arr
                                    break
                            if(success == True):
                                break
                        if(success == True):
                            break
                    if(success == True):
                        break
                if(success == True):
                    break
            if(success == True):
                break
        if(success == True):
                break

    mn = capacityPureEG[0]
    for i in path:
        mn = min(mn, i.capacity)
    smEG += mn
    capacityArrayEG.append(mn)

    if(mn == capacityPureEG[0]):
        capacityPureEG.pop(0)
        pathsPureEG.pop(0)
    else:
        capacityPureEG[0] -= mn

    for i in path:
        nm = i.name
        for j in range(len(fieldEG[cx - 1])):
            if(fieldEG[cx - 1][j].name  == nm):
                fieldEG[cx - 1][j].capacity -= mn
                if(fieldEG[cx - 1][j].capacity == 0):
                    fieldEG[cx - 1].pop(j)
                break
        cx += 1

    array = temp + path
    pathsEG.append(array)

def createList():
    global smEG
    while(len(pathsPureEG) != 0):
        temp = pathsPureEG[0]
        count = capacityPureEG[0]
        remPart(temp, count)

def dfs2():
    global stopEG2, numberOfCoursesPureEG
    temp = []
    p = []
    clashCheck = {}

    # numberOfCoursesPureEG -= 1

    for i in range(numberOfCoursesPureEG - 1):
        for j in range(len(fieldEG[i])):
            sec = fieldEG[i][j]
            if(sec.capacity == 0):
                continue
            timing = sec.timing
            clashing = False

            for k in range(len(timing)):
                key = str(timing[k])

                if(key in clashCheck):
                    clashing = True
                    break

            if(clashing == False):
                temp.append(sec)
                p.append([i,j])
                for k in range(len(timing)):
                    key = str(timing[k])
                    clashCheck[key] = True;
                break

    if(len(temp) != numberOfCoursesPureEG - 1):
        stopEG2 = True
        return

    pathsPureEG.append(temp)
    mn = temp[0].capacity
    for i in temp:
        mn = min(mn, i.capacity)

    capacityPureEG.append(mn)

    for i in range(len(temp)):
        x = p[i][0]
        y = p[i][1]

        fieldEG[x][y].capacity -= mn

        if(fieldEG[x][y].capacity == 0):
            fieldEG[x].pop(y)
            if(len(fieldEG[x]) == 0):
                stopEG2 = True

def getEGCombinationsStage2():
    global stopEG2
    while(not stopEG2):
        dfs2()

    createList()

def getNumberOfStudentsAllotedInEG():
    global smEG
    return smEG

def generateEGCombinations():
    getEGCombinationsStage1()
    getEGCombinationsStage2()
    getNumberOfStudentsAllotedInEG()
    