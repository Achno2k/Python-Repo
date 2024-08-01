# #if-elif-else statements
# #=======================

# x = 2
# if(x > 0):
#     print("Positive integer")
# elif(x < 0):
#     print("Negative integer")
# else:
#     print("The number is zero")

# #------------------------------

is_hot = False
if is_hot == True:
    print("It's a hot day!")
elif(is_hot == False):
     print("It's a cold day!")
else:
    print("It's a lovely day")   

# """
# LOGICAL OPERATORS
# -----------------
# AND : Both conditions should be true
# OR : Atleast one of the conditions should be true
# NOT : Inverses any boolean value
# """ 

# #AND
# has_good_credit = True
# has_good_income = True
# if has_good_credit and has_good_income:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# #OR
# has_good_credit = False
# has_good_income = True
# if has_good_income or has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

#NOT
bool_val = True
if not bool_val:
    print("The statement is true")
else:
    print("Nope!")

# """
# COMPARISION OPERATORS
# ---------------------
# >/< -> greator or less than
# >= -> greator than or equal to
# <= -> less than or equal to
# != -> not equal to
# == -> equal to (not  '=', which is an assignment operator) 
# """
 
# name = "Aman"
# if len(name) < 3:
#     print("Name must be atleast 3 characters long")
# elif len(name) > 50:
#     print("Name cannot be a maximum of 50 characters")
# else:
#     print("Name looks good!")



# #WEIGHT CONVERTOR PROGRAM
# weight = float(input("Enter your weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == 'L':
#     converted_weight = weight * 0.453
#     print(f"Your weight in kg: {converted_weight}")
# else:
#     converted_weight = weight / 0.453
#     print(f"Your weight in lbs: {converted_weight}")

#Ternary Operator (Condintional Expressions)
#Syntax --> 'statement_if_true' if 'condition' else 'condition'
is_friend = True
can_message = "message allowed" if is_friend else "no message allowed"
print(can_message)
print("message allowed" if is_friend else "no message allowed")


