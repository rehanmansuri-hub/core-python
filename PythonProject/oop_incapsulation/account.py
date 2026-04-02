class account :
    def __init__(self):  #constructor
        self.__number = None  #instance variable
        self.__accountType = None
        self.__balance = 0.0


    def set__number(self,number):
        self.__number = number

    def get__number(self):
        return self.__number

    def set__account_type(self,account_type):
        self.__accountType = account_type

    def get__account_type(self):
        return self.__accountType

    def set__balance(self,balance):
        self.__balance = balance

    def get__balance(self):
        return self.__balance


acc = account()
acc.set__number(2154)
acc.set__account_type("Saving")
acc.set__balance(1000)
print("Account Number:", acc.get__number())
print("Account Type:", acc.get__account_type())
print("Balance:", acc.get__balance())


