#Handling ValueError
try:                #try this
    age = int(input("Enter your age: "))
    print(age)
except ValueError: #if gives ValuesError. print this 
    print("Invalid value")


#Handling ZeroDivisioneError
try:
    income = int(input("Enter your income: "))
    age = int(input("Enter your age: "))
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("Age cannot be 0")  