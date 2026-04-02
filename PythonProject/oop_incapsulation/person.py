
class person:

        def __init__(self):
            self.__name = None
            self.__dob = None
            self.__address = None

        def get__name(self):
            return self.__name

        def set__name(self,name):
            self.__name = name

        def get__dob(self):
            return self.__dob

        def set__dob(self,dob):
            self.__dob = dob

        def get__address(self,):
            return self.__address

        def set__address(self,address):
            self.__address = address


p = person()
p.set__name("rehan")
p.set__address("kalapipal")
p.set__dob((2006,11, 17))
print(p.get__name())
print(p.get__dob())
print(p.get__address())