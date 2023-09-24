# #LOOPS 
# #=====

# # WHILE LOOP
# #===========
# i = 1  #initialization
# while i <= 10:  #condition
#     print(i)
#     i += 1  #updation
# print("Loop is successfully executed!")

# #printing a pattern
# i = 1
# while i<5:
#     print("*" * i)
#     i += 1
# print("Done!")

# #------------------------
# #Building a guessing game 
# #------------------------
# secret_num = 9
# guess_count = 0
# while guess_count < 3:
#     x = int(input("Enter your guess: "))
#     guess_count += 1
#     if x == secret_num:
#         print("You won!")
#         break
# else:      # here the else block for the while loop works as an if else block for the while loop, if the code does not break till the loops completion it will automatically execute the else block
#     print("Sorry, You failed")

#----------------------------
# #Building a little car game
# #--------------------------
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if(command == "start"):
#         if started:
#             print("Car is already started!")
#         else:
#             print("Car started...")
#             started = True
#     elif(command == "stop"):
#         if not started:
#             print("Car is already stopped!")
#         else:
#             print("Car stopped...")
#             started = False
#     elif(command == "help"):
#         print("""
#         start -> starting the car
#         stop -> stopping the car
#         quit -> to exit the game
#         """)
#     elif command == "quit":
#         print("Game successfully exited...")
#         break


# FOR LOOPS
# =========
for item in "Python":
    print(item)  # this will iterate over every letter in the word Python

for item in ['Aman', 'Isha', 'Vaibhav']: # this will iterate over every list item and print them
    print(item)

"""
General for loop using range function
Syntax -> for i in range(start, end, update)
"range" function is predefined in python
default start value is 0
default step value is 1
"""
for i in range(10):  
    print(i)
print()

for i in range(5, 10):
    print(i)
print()

for i in range(1, 10, 2):
    print(i)
print()

#adding a lists items using for loop
prices = [10, 20, 30]
sum = 0
for price in prices:
    sum += price
print(f"Total: {sum}")

# NESTED LOOPS
# ============
#printing coordinates of a 3x3 matrix using nested for loops
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")
    print()    

