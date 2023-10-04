class PlayerCharacter:
    membership = True    #class object attribute
    def __init__(self, name = 'Anonymous', age = 0):   #constructor method
        self.name = name       #attributes or properties
        self.age = age

    def run(self):
        print("Running")

    @classmethod        #classmethod (can also be used as a constructor)
    def adding_nums(cls, num1, num2):
        return cls(num1 + num2)

player1 = PlayerCharacter("Aman", 19)
print(player1.name)
print(player1.adding_nums(2, 3))
player1.run()