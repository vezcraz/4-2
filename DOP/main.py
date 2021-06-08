from config import *
from input import *
from timeSlot import getTime
from sectionMap import *
from combinationGeneratorEG import *
from combinationGeneratorWS import *
from output import *

def main():
    inputEG()
    inputWS()
    createSectionMap()
    generateEGCombinations()
    generateWSCombinations()
    printEGCombinations()
    printWSCombinations()
    print("Number Of Students successfully alloted in EG: {}".format(getNumberOfStudentsAllotedInEG()))
    print("Number Of Students successfully alloted in WS: {}".format(getNumberOfStudentsAllotedInWS()))

if __name__ == "__main__":
    main()