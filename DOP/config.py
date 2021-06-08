from inp1 import inp1_df 
from inp2 import inp2_df

courseListAll = [ 'BITS F110 P', 'CHEM F110 P', 'PHY F110 P', 'MATH F113 L', 'MATH F113 T', 'BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 L', 'PHY F111 T', 'BIO F111 L' , 'BIO F111 T' , 'MATH F111 L', 'MATH F111 T',  'CHEM F111 L', 'CHEM F111 T' ]
courseListEG = [ 'BITS F110 P', 'CHEM F110 P', 'PHY F110 P', 'MATH F113 T', 'MATH F113 L',  'BIO F111 L' , 'BIO F111 T' , 'MATH F111 L', 'MATH F111 T',  'CHEM F111 L', 'CHEM F111 T' ]
courseListWS = [ 'BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 T', 'PHY F111 L', 'BIO F111 L' , 'BIO F111 T' , 'MATH F111 L', 'MATH F111 T',  'CHEM F111 L', 'CHEM F111 T' ]
courseListPureEG = [ 'BITS F110 P', 'CHEM F110 P', 'PHY F110 P', 'MATH F113 T', 'MATH F113 L' ]
courseListPureWS = [ 'BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 T', 'PHY F111 L' ]
# courseListWS = [ 'BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 T', 'PHY F111 L' ]

numberOfCoursesAll = len(courseListAll)
numberOfCoursesEG = len(courseListEG)
numberOfCoursesWS = len(courseListWS)
numberOfCoursesPureEG = len(courseListPureEG)
numberOfCoursesPureWS = len(courseListPureWS)
stopEG1 = False
stopEG2 = False
stopEG3 = False
stopWS1 = False
stopWS2 = False
stopWS3 = False
sm = 0
smWS = 0
smEG = 0

sectionTimeMap = {}

capacityArrayEG = []
capacityArrayWS = []
capacityPureEG = []
capacityPureWS = []
pathsEG = []
pathsWS = []
pathsPureEG = []
pathsPureWS = []
fieldEG = []
fieldWS = []
for i in range(20):
    fieldEG.append([])
    fieldWS.append([])

class Slot:
    day = str()
    startTime = int()

    def __repr__(self):
        return str(self)
 
    def __str__(self):
        return  self.day + ' ' + str(self.startTime)
 
class Section:
    name = str()
    timing = [Slot()]
    capacity = int()
    allotted = int()

    def __repr__(self):
        return str(self) + "\n"
 
    def __str__(self):
        strs = ""
        strs = self.name + "\t"
        strs = strs + str(self.capacity) + "\t"
        for i in self.timing:
            strs = strs + i.day + " " + str(i.startTime) + " "
        return strs