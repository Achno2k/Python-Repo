from math import * #importing math module or file to use various mathemeatical functions/methods
# #start with a simple program
# #===========================

# print("Hello world")

# #====================================+
# #Teach them about console
# #By telling them some print statements
# #====================================+

# #Variables and datatypes
# #=======================

# name = "Aman"
# age = "20" #this is a string declaration
# #python declares a string variable by default
# print("Name " + name + " of age " + age)

# #different types of datatypes
# #=======================
# name = "Aman" #strings
# age = 20 #int
# float_num = 34.34343 #float
# bool_val = True #Boolean

# #working with strings
# #====================

# print("Aman \nSingh") #insert a new line
# str = "string variable"
# print(str) 
# print(str + " is cool") #concatenation
# print(str.lower())
# print(str.upper())
# print(str.upper().isupper())
# print(len(str))
# print(str[0]) #indexing starts from 0
# print(str.index("s")) #will give you the index
# print(str.index("variable")) #throws error if is not present in the string
# print(str.replace("variable", "Methods")) #replaces the string with a new string

# #working with numbers
# #====================

# print(2) #printing an integer number
# print(-1) #printing an negative integer number
# print(2.0034) #printing a floating number

# print(2*(3+5))
# print(10 % 2)  #remainder operator

# val = 2
# print(str(val)) #converts it into string
# #***print(2 + " is my favorite number")*** 
# #this will throw an error because you cannot concate an int and a string
# print(str(val) + " is my favourite number") #use str function if you want to write an int with some comment

# val1 = -1
# print(abs(val1)) #for getting an absolute value of the integer
# print(pow(4, 2)) #to get the power of an int
# print(max(2,3))  #for getting the max between two ints
# print(min(1,2))  #for getting min between the two ints
# print(round(3.7)) #rounding off to nearest int
# print(sqrt(36))
# print(floor(4.34))
# print(ceil(2.9))

# #getting input from a user
# #=========================
# #python takes input as a string by default
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hi " + name + "!, You are " + age)

# float_val = float(input("Enter a float value: "))
# print(float_val)


# #Arithmetic Operators
# print(10 + 3) #addition --> 13
# print(10 - 3) #subtraction --> 7
# print(10 * 3) #multiplication --> 30
# print(10 / 3) #division --> 3.333333
# print(10 // 3) #division to the nearest int --> 3
# print(10 ** 3) #exponent --> 1000

#Operator Precedence
# ** -> * or / --> + or -
# or we can use parenthesis to change the preference

#String formatting
# name = "Aman"
# country = "India"
# print("Hi my name is", name, "and I am from", country)
# print(f"Hi my name is {name} and I am from {country}")
# txt = f"Hi my name is {name} and I am from {country}"
# print(txt)

