#Parent Class (Super class)
class User():  
    def sign_in(self):
        print("Logged In")

    def same_func(self):
        print("User class")

#Child Classes (Derived Classes)
class Wizard(User):                 #user class inherited
    def __init__(self, name, power):
         self.name = name
         self.power = power
    
    def attack(self):
        # User.attack(self)       #calling attack() of the User class
        print(f"Attacking with power of {self.power}")

    def same_func(self):
        print("Wizard class")


class Archer(User):
    def __init__(self, name, arrows):   
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")
    
    def run(self):
        print("Running very fast")

    def same_func(self):
        print("Archer class")

class Hybrid(Wizard, Archer):           #Multiple Inheritance
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)



wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

wizard1.sign_in()           #Inherited function
wizard1.attack()            #own class method

archer1.sign_in()           #Inherited function
archer1.check_arrows()            #own class method

#using isinstance() --> checks if any object is an object of a class
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(wizard1, Archer))


# Introspection --> list of all the available method a class object has access to
print(dir(wizard1))

#Multiple Inheritance
h1 = Hybrid("Arnold", 50, 100)
h1.check_arrows()
h1.attack()
h1.run()
h1.sign_in()
h1.same_func()    #this will use the wizard function because it was inherited first

