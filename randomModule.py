import random

# for i in range(3):
#     print(random.random())   #generates random values between 0 and 1
#     print(random.randint(10, 20))   #generates random values b/w 10-20

# members = ["Aman", "Vaibhav", "Isha"]
# print(random.choice(members))

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    
obj1 = Dice()
print(obj1.roll(), type(obj1.roll()))   #type-> tuple
 



