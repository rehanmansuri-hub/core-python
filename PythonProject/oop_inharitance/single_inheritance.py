
# class Shape:
#     def __init__(self):
#         self.color = ''
#         self.borderWidth = 0
class Shape:
    def __init__(self):
        self.color = ''
        self.borderWidth = ''


    def setcolor(self,color):
        self.color = color
    def getcolor(self):
        return self.color

    def setborderWidth(self,borderWidth):
        self.borderWidth = borderWidth
    def getborderWidth(self):
        return self.borderWidth

class Rectangle(Shape):

    def __init__(self):
        self.length = 0
        self.width = 0
    def setlength(self,length):
        self.length = length
    def getlength(self):
        return self.length

    def setwidth(self,width):
        self.width = width
    def getwidth(self):
        return self.width




r = Rectangle()
r.setlength(10)
r.setwidth(20)
r.setcolor("red")
r.setborderWidth(100)


print("Length:", r.getlength())
print("Width:", r.getwidth())
print("Color:", r.getcolor())
print("Border Width:", r.getborderWidth())
