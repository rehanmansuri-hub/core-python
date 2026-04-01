class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        className = self.__class__.__name__
        print("Destroying ", className)

    def __str__(self):
        return "Person: name = %s, age = %s" % (self.name, self.age)


person = Person("rehan", 30)
p1 = Person("rehan", 25)

print(person)
print(p1)
