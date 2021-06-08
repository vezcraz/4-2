from config import *

def dfs1():
    global stopWS1, smWS, numberOfCoursesWS
    temp = [] 
    p = []
    clashCheck = {}

    for i in range(numberOfCoursesWS):
        for j in range(len(fieldWS[i])):
            sec = fieldWS[i][j]
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

    if(len(temp) != numberOfCoursesWS):
        stopWS1 = True
        return

    pathsWS.append(temp)
    mn = temp[0].capacity
    for i in temp:
        mn = min(mn, i.capacity)

    capacityArrayWS.append(mn)

    smWS += mn
    for i in range(len(temp)):
        x = p[i][0]
        y = p[i][1]

        fieldWS[x][y].capacity -= mn

        if(fieldWS[x][y].capacity == 0):
            fieldWS[x].pop(y)
            if(len(fieldWS[x]) == 0):
                stop = True

def getWSCombinationsStage1():
    global stopWS1
    while(not stopWS1):
        dfs1()

def remPart(temp, count):
    global smWS, numberOfCoursesPureWS
    clashCheck = {}
    path = []

    for i in temp:
        clashCheck[i] = True

    cx = numberOfCoursesPureWS

    for it0 in fieldWS[cx-1]:
        for it1 in fieldWS[cx]:
            for it2 in fieldWS[cx + 1]:
                for it3 in fieldWS[cx + 2]:
                    for it4 in fieldWS[cx + 3]:
                        for it5 in fieldWS[cx + 4]:
                            for it6 in fieldWS[cx + 5]:
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

    mn = capacityPureWS[0]
    for i in path:
        mn = min(mn, i.capacity)
    smWS += mn
    capacityArrayWS.append(mn)

    if(mn == capacityPureWS[0]):
        capacityPureWS.pop(0)
        pathsPureWS.pop(0)
    else:
        capacityPureWS[0] -= mn

    for i in path:
        nm = i.name
        for j in range(len(fieldWS[cx - 1])):
            if(fieldWS[cx - 1][j].name  == nm):
                fieldWS[cx - 1][j].capacity -= mn
                if(fieldWS[cx - 1][j].capacity == 0):
                    fieldWS[cx - 1].pop(j)
                break
        cx += 1

    array = temp + path
    pathsWS.append(array)

def createList():
    global smWS
    while(len(pathsPureWS) != 0):
        temp = pathsPureWS[0]
        count = capacityPureWS[0]
        remPart(temp, count)

def dfs2():
    global stopWS2, numberOfCoursesPureWS
    temp = []
    p = []
    clashCheck = {}

    # numberOfCoursesPureWS -= 1

    for i in range(numberOfCoursesPureWS - 1):
        for j in range(len(fieldWS[i])):
            sec = fieldWS[i][j]
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

    if(len(temp) != numberOfCoursesPureWS - 1):
        stopWS2 = True
        return

    pathsPureWS.append(temp)
    mn = temp[0].capacity
    for i in temp:
        mn = min(mn, i.capacity)

    capacityPureWS.append(mn)

    for i in range(len(temp)):
        x = p[i][0]
        y = p[i][1]

        fieldWS[x][y].capacity -= mn

        if(fieldWS[x][y].capacity == 0):
            fieldWS[x].pop(y)
            if(len(fieldWS[x]) == 0):
                stopWS2 = True

def getWSCombinationsStage2():
    global stopWS2
    while(not stopWS2):
        dfs2()

    createList()

def getNumberOfStudentsAllotedInWS():
    global smWS
    return smWS

def generateWSCombinations():
    getWSCombinationsStage1()
    getWSCombinationsStage2()
    getNumberOfStudentsAllotedInWS()
    