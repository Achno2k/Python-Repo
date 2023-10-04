# # #===================
# # #Functions in Python
# # #===================

# # #Case-1 --> Required Arguments: To provide the parameters in a particular order
#Calculating the greater between two numbers

def isGreater(a, b):
    """This program tells the greater between two numbers"""
    if a > b:
        print(a, "is greater")
    elif a < b:
        print(b, "is greater")
    else:
        print("Both are equal")

print(isGreater.__doc__)
isGreater(3, 4)
isGreater(4, 3)
isGreater(4, 4)

# # #using different datatypes (String)
def isGreater(a, b):
    """This program tells the greater between two numbers"""
    if a > b:
        print(a, "is greater")
    elif a < b:
        print(b, "is greater")
    else:
        print("Both are equal")
print(isGreater.__doc__)   #doc strings
isGreater('Aman', 'Singh')


# # #Case-2 --> Default Arguments: Giving the function arguments a default value to work with
def isGreater(a = 4, b = 5):
    """This program tells the greater between two numbers"""
    if a > b:
        print(f"a: {a} is greater")
    elif a < b:
        print(f"b: {b} is greater")
    else:
        print("Both are equal")

isGreater()      # here providing no values because the function already has values to work with, so it will work just fine
isGreater(6, 7)  # here the value of the arguments will get override by new values 


# # # #Case 3: Keyword Arguments: the parameter values are sent along with the parameter name thus the order does not matter
def isGreater(a, b):
    """This program tells the greater between two numbers"""
    if a > b:
        print(f"a: {a} is greater")
    elif a < b:
        print(f"b: {b} is greater")
    else:
        print("Both are equal")

isGreater(b = 4, a = 5)   # here while sending values to the function arguments along with their argument names, the order in which they are sent does not matter
isGreater(a = 6, b = 5)

# # # #Case 3: Variable Length Arguments: for multiple inputs
def average(*numbers):    
    print(type(numbers))   #numbers works as a "Tuple"
    sum = 0
    for i in numbers:
        sum += i
    print("Average is:", sum/len(numbers))

average(1,2,3,4,5,6)

def printInfo(info):
    print(type(info))
    for key, value in info.items():
        print(f"{key} : {value}")

info = {"fname": "Aman", "sname": "Singh", "Domain": "Python"}
printInfo(info)

# # #Return Statements
# # #=================

def func(a):
    return 2*a     #returning twice the value of the passed argument

returnedVal = func(4)  #for integer value
print(returnedVal)

returnedVal = func(5.982975)  #for float value
print(returnedVal)

returnedVal = func("Aman")  #for string value
print(returnedVal)


lst = [12, "Aman", True, 9.665676]
def get(lst):
    for item in lst:
        print(item)
get(lst)

print()
print()

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def myfunction():
  pass


def sumNums(*numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def average(*numbers):
    total = sumNums(*numbers)      # calling sumNums() in average()
    print("Average is:", total / len(numbers))

average(1, 2, 3, 4, 5)


#Emoji convertor function
def emoji_convertor(message):
    words = message.split(' ')
    emojis = {
    ":)" : "😊",
    ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">>")
print(emoji_convertor(message))
