class Shape:
    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, borderWidth):
        self.borderWidth = borderWidth

    def getBorderWidth(self):
        return self.borderWidth


s = Shape("Red", 5)
print("Color", s.getColor())
print("BorderWidth", s.getBorderWidth())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age


# Object create karte waqt values pass kar rahe hain
s1 = Student("Rehan", 18)

print("Name:", s1.getName())
print("Age:", s1.getAge())