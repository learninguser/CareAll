from profile import User
from ElderFolk import ElderFolk

class YoungFolk(User):
    YoungFolks = []

    @classmethod
    def updateYoung(cls, young):
        cls.YoungFolks.append(young)

    def __init__(self, id, name, age, role):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__role = role
        self.__oldieCount = 0
        self.__oldieTakingCareof = []
        self.__salary = 0
        YoungFolk.updateYoung(self)
    
    def getRole(self):
        return self.__role
    
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    
    def getAge(self):
        return self.__age

    def applyForService(self, elder):
        if not elder.getAvailabilty():
            print("Sorry, Not available")
            return False
        print("Thank you for applying")
        return True

    def setOldieCount(self, count):
        self.__oldieCount += count
    
    def getOldieCount(self):
        return self.__oldieCount
    
    def setOlideTakenCareOf(self, elder):
        if elder.getAvailabilty() and elder.getApproveFolk() and self.getOldieCount() < 4:
            self.__oldieTakingCareof.append(elder.getName())
            self.setOldieCount(1)
        elif elder.getApproveFolk() and self.__oldieCount >= 4:
            print("A limit of 4 Olides already exceeded")
            return True

    def getOlideTakenCareof(self):
        return self.__oldieTakingCareof
    
    def setSalary(self, salary):
        self.__salary += salary

    def getSalary(self):
        return self.__salary
