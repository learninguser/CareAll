from profile import User

class YoungFolk(User):
    def __init__(self):
        self.__oldieCount = 0
        self.__oldieTakingCareof = []
        self.__salary = 0

    def setOldieCount(self, count):
        self.__oldieCount += count
    
    def getOldieCount(self):
        return self.__oldieCount
    
    def setOlideTakenCareOf(self, oldie):
        if self.__oldieCount < 5:
            self.__oldieTakingCareof.append(oldie)
        else:
            return "A limit of 4 Olides already exceeded"
    
    def getOlideTakenCareof(self):
        return self.__oldieTakingCareof
    
    def setSalary(self, salary):
        self.__salary += salary
    
    def getSalary(self):
        return self.__salary
