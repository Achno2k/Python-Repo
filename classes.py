# Classes are used to create user defined datatypes

class  Point:
    def __init__(self, x, y):   #Constructor, __init__ is short for initialization
        self.x = x              #you need to have self as arguments in all your methods
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point1 = Point(3, 4)
print(point1.x)
point1.draw()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Aman")
print(p1.name)
p1.talk()


#Inheritance
class Mammal:
    def walk(self):
        print("Walking")

class Dog(Mammal):    #Dog class inherited the properties of Mammal class
    def bark(self):
        print("Barking")

class Cat(Mammal):
    def be_annoying(self):
        print("Be annoying")

dog1 = Dog()
dog1.walk()       #here I can use the walk() because we inherited the properties of Mammal class
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()