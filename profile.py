class User:
    emails = {}

    @classmethod
    def credentials(cls, email, password):
        cls.emails[email] = password

    usersList = []
    @classmethod
    def updateUsersList(cls, id, name, age, role):
        cls.usersList.append([id, name, age, role])

    def __init__(self, id, name, age, role):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__role = role
        self.__rating = 0
        self.__review = []

        User.updateUsersList(self.__id, self.__name, self.__age, self.__role)

    def getRole(self):
        return self.__role
    
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    
    def getAge(self):
        return self.__age
    
    def register(self, email, password):
        if email in User.emails.keys():
            print("User already registered in the system please login with your credentials")
            
        else:
            self.setEmail(email)
            self.setPassword(password)
            User.credentials(self.__email, self.__password)
            print("Registration Successful")
    
    def login(self, email, password):
        if User.emails[email] == password:
            print("Logged in successfully")
            return 1
        elif email not in User.emails.keys():
            print("User doesn't exsist")
            return 0
        else:
            print("Invalid Credentials")
            return -1
    
    def setEmail(self, email):
        self.__email = email
    
    def getEmail(self):
        return self.__email

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password
    
    def setRating(self, rating):
        self.__rating = rating
    
    def getRating(self, rating):
        return self.__rating
    
    def setReview(self, review):
        self.__review.append(review)

    def getReview(self):
        return self.__review