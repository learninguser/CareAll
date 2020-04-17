from profile import User

class ElderFolk(User):
    elderFolks = []

    @classmethod
    def updateElders(cls, elder):
        cls.elderFolks.append(elder)

    def __init__(self, id, name, age, role):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__role = role
        self.__isAvailable = True
        self.__allocateFunds = 0
        self.__approveFolk = False      
        ElderFolk.updateElders(self)
    
    def getRole(self):
        return self.__role
    
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    
    def getAge(self):
        return self.__age

    def setAvailabilty(self, availabilty):
        self.__isAvailable = availabilty
    
    def getAvailabilty(self):
        return self.__isAvailable
    
    def setFunds(self, fund):
        self.__allocateFunds += fund
    
    def getFunds(self):
        return self.__allocateFunds
    
    def setApproveFolk(self, approve):
        self.__approveFolk = approve
    
    def getApproveFolk(self):
        return self.__approveFolk
