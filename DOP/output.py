from config import *

def showEG():
    for i in fieldEG:
        print(i)

def showWS():
    for i in fieldWS:
        print(i)

def printEGCombinations():
    for lst in pathsEG:
        tempMap = {}
        for i in lst:
            timings = i.timing
            for t in timings:
                if(t in tempMap):
                    print("F")
                    break
                tempMap[t] = True


    print("Number\tCapacity\t", end="")
    for i in pathsEG[0]:
        str = i.name
        arr = str.split()
        print("{}{} {}".format(arr[0], arr[1], arr[2][0]), end="\t")

    print()

    cx = 0;

    for lst in pathsEG:
        cx += 1
        print("{}\t{}".format(cx, capacityArrayEG[cx-1]), end="\t")
        for i in lst:
            str = i.name.split()
            print(str[2][1:], end="\t")
        print()

def printWSCombinations():
    for lst in pathsWS:
        tempMap = {}
        for i in lst:
            timings = i.timing
            for t in timings:
                if(t in tempMap):
                    print("F")
                    break
                tempMap[t] = True


    print("Number\tCapacity\t", end="")
    for i in pathsWS[0]:
        str = i.name
        arr = str.split()
        print("{}{} {}".format(arr[0], arr[1], arr[2][0]), end="\t")

    print()

    cx = 0;

    for lst in pathsWS:
        cx += 1
        print("{}\t{}".format(cx, capacityArrayWS[cx-1]), end="\t")
        for i in lst:
            str = i.name.split()
            print(str[2][1:], end="\t")
        print()