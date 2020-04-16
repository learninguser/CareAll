from profile import User

class ElderFolk(User):
    def __init__(self):
        self.__isAvailable = True
        self.__allocateFunds = 0
        self.__approveFolk = False        

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
