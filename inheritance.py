#Parent Class (Super class)
class User():  
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged In")

    # def attack(self):
    #     print("Do nothing")

#Child Classes (Derived Classes)
class Wizard(User):                 #user class inherited
    def __init__(self, name, power, email):
         super().__init__(email)            #super() calls the init() of User class without worriyng about self
         self.name = name
         self.power = power
    
    def attack(self):
        # User.attack(self)       #calling attack() of the User class
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)   
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"Attacking with {self.arrows} number of arrows")

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 100, "robin@gmail.com")

print(wizard1.email)
print(archer1.email)

wizard1.sign_in()           #Inherited function
wizard1.attack()            #own class method

archer1.sign_in()           #Inherited function
archer1.attack()            #own class method

#using isinstance() --> checks if any object is an object of a class
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(wizard1, Archer))


# Introspection --> list of all the available method a class object has access to
print(dir(wizard1))