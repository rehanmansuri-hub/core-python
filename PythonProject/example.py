# class shape:
#     def area(self):
#         print("area of shape")
#
#
# class rectangle(shape):
#     def area(self):
#         print("area of rectangle")
#
# r = rectangle()
# r.area()
#
# s = shape()
# s.area()
#
#
#
# class Bank:
#     def get_interest(self):
#         print("Default interest rate is 4%")
#
# class ICICI(Bank):
#     def get_interest(self):
#         print("ICICI interest rate is 6%")
#
# class Axis(Bank):
#     def get_interest(self):
#         print("Axis interest rate is 7%")
#
# # Objects
# b = Bank()
# i = ICICI()
# a = Axis()
#
# b.get_interest()
# i.get_interest()
# a.get_interest()
#
#
# # Parent class
# class Bank:
#     def __init__(self, name, rate):
#         self.name = name
#         self.rate = rate
#
#     def interest(self, amount, time):
#         # simple interest formula
#         si = (amount * self.rate * time) / 100
#         print(f"{self.name} Interest: {si}")
#
#
# # Child class SBI
# class SBI(Bank):
#     def __init__(self):
#         super().__init__("SBI", 7)   # calling parent constructor
#
#     def interest(self, amount, time):   # overriding
#         print("Calculating SBI Interest...")
#         super().interest(amount, time)
#
#
# # Child class HDFC
# class HDFC(Bank):
#     def __init__(self):
#         super().__init__("HDFC", 6)
#
#     def interest(self, amount, time):   # overriding
#         print("Calculating HDFC Interest...")
#         super().interest(amount, time)
#
#
# # Objects
# s = SBI()
# h = HDFC()
#
# # User values
# amount = 10000
# time = 2
#
# s.interest(amount, time)
# h.interest(amount, time)


# Parent class
class animal:
    def sound(self):
        print("animal make a sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class cat(animal):
    def sound(self):
        print("cat meows")

class lion(animal):
    def sound(self):
        print("lion roar")

class cow(animal):
    def sound(self):
        print("cow moo")


# object
d = dog()
c = cat()
l = lion()
co = cow()

d.sound()
c.sound()
l.sound()
co.sound()