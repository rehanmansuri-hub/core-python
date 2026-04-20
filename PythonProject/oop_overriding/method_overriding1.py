class shape:
    def area(self):
        print("shape area.....")
        return print("shape class area metod")


class rectangle(shape):
    pass
    def area(self):
        print("rectangle area....")
        return print("rectangle class area method")


r = rectangle()
r.area()
s = shape()
s.area()
shape: shape = rectangle()
shape.area()