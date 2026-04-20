# class Shape:
#     def __init__(self, color, borderWidth):
#         print("Shape Constructor Called")
#         self.color = color
#         self.borderWidth = borderWidth
#
#     def setColor(self, c):
#         self.color = c
#
#     def getColor(self):
#         return self.color
#
#     def setBorderWidth(self, bw):
#         self.borderWidth = bw
#
#     def getBorderWidth(self):
#         return self.borderWidth
#
#
# class Rectangle(Shape):
#
#     def __init__(self, length=0, width=0, color='', borderWidth=0):
#         self.length = length
#         self.width = width
#         super().__init__(color, borderWidth)
#
#     def setLength(self, l):
#         self.length = l
#
#     def getLength(self):
#         return self.length
#
#     def setWidth(self, w):
#         self.width = w
#
#     def getWidth(self):
#         return self.width
#
#
# r = Rectangle(10, 20, 'red', 100)
# print("Rectangle:")
# print("Length:", r.getLength())
# print("Width:", r.getWidth())
# print("Color:", r.getColor())
# print("Border Width:", r.getBorderWidth())


class Shape:
    def __init__(self, color):
        self.color = color

    def showColor(self):
        print("Color:", self.color)


class Rectangle(Shape):
    def __init__(self, color, length, width):
        # Parent constructor call
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display(self):
        self.showColor()
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())


# Object create
r1 = Rectangle("Blue", 10, 5)
r1.display()