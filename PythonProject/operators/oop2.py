class shape:
    def __init__(self,color='',machine=0):
        self.color = color
        self.machine = machine

    def setcolor(self,color):
        self.color = color
    def getcolor(self):
        return self.color

    def setmachine(self,machine):
        self.machine = machine
    def getmachine(self):
        return self.machine



class Rectangle(Shape):
    def __init__(self, length=0, width=0, color='', borderWidth=0):
        self.length = length
        self.width = width
        super().__init__(color, borderWidth)

