# #fucntion to find the max of three numbers
# def findMax(a, b, c):
#     if a > b:
#         if a > c:
#             print(f"a = {a} is max")
#         else:
#             print(f"c = {c} is max")
#     elif b > a:
#         if b > c:
#             print(f"b = {b} is max")
#         else:
#             print(f"c = {c} is max")
# findMax(2, 3, 4)

# #function to multiply all the numbers in a list.
# def func(*numbers):
#     value = 1
#     for x in numbers:
#         value *= x
#     return value
# print(func(1,2,3,4,5))


# #Python program to reverse a string.
# def func(str):
#     newStr = ""
#     index = len(str) - 1
#     while index >= 0:
#         newStr += str[index]
#         index = index - 1
#     return newStr

# print(func("Aman1234"))

# #function to calculate the factorial of a number (a non-negative integer)
# # using recursion
# def fact(n):
#     if n > 0:
#         return n * fact(n-1)      
#     else: 
#         return 1
# print(fact(5))

# #using for loop
# def fact(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     return factorial
# print(fact(5))

# #function that accepts a string and counts the number of upper and lower case letters
# def func(str):
#     upperCount = 0
#     lowerCount = 0
#     for x in str:
#         if x.isupper():
#             upperCount = upperCount + 1
#         elif x.islower():
#             lowerCount = lowerCount + 1
#     print(f"No. of Uppercase letters are: {upperCount}")
#     print(f"No. of Lowerrcase letters are: {lowerCount}")

# func("Aman Singh")

# # function that takes a list and returns a new list with distinct elements from the first list.
# def func(lst):
#     newlst = []
#     for x in lst:
#         if x not in newlst:
#             newlst.append(x)
#     return newlst
# lst = [1,2,3,3,3,3,4,5,5]
# print(func(lst))


# # Python function that takes a number as a parameter and checks whether the number is prime or not.
# def checkPrime(num):
#     for i in range(2, num//2 + 1):
#         if num % i == 0:
#             return False
#     return True
# print("Prime" if checkPrime(27) else "Not Prime")

# # function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
# def createList():
#     newlst = []
#     for i in range(0,31):
#         newlst.append(i*i)
#     return newlst
# print(createList())

