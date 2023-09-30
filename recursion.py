# Recursion -> Calling the same function inside that function is called Recursion
# ===============================================================================

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)   #calling it recursively here

print(factorial(5))


def fibonacci(n):
    if n <= 1:
        return 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))
        