from datetime import datetime


class person:
    AVG_AGE = 18  # static constant

    def __init__(self): #constructor
        self.__name = None
        self.__dob = None  #instance variable
        self.__address = None


    def get__name(self):
        return self.__name
    def set__name(self,name):
        self.__name = name

    def get__dob(self):
        return self.__dob
    def set__dob(self,dob):
        self.__dob = dob

    def get__address(self):
        return self.__address
    def set__address(self,address):
        self.__address = address

        # Age calculation method
    def get_age(self):
        if self.__dob is None:
            return None

        now = datetime.now()
        age = now.year - self.__dob.year
        return age


p = person()
p.set__name("Rehan Mansuri")
p.set__address("Indore")
p.set__dob(datetime(2006, 11, 17))

print("Name:", p.get__name())
print("Age:", p.get_age())
print(p.get__dob())
