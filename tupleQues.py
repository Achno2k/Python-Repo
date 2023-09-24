#1. Write a Python program to convert a tuple to a string.
tup = ("p", "y", "t", "h", "o", "n")
def change_To_Str(tup):
    result_str = ""
    for ch in tup:
        result_str = result_str + ch
    return result_str
print("Changed string is:",change_To_Str(tup))
#-----------------------------------------------------------------------------


#2. Write a Python program to find repeated items in a tuple.
def find_duplicates(my_tuple):
    duplicates = []    #creating a new list to store elements which are repeated
    for i in range(len(my_tuple)):
        for j in range(i + 1, len(my_tuple)):
            if my_tuple[i] == my_tuple[j] and my_tuple[i] not in duplicates:
                duplicates.append(my_tuple[i])

    return duplicates
my_tuple = (1, 2, 3, 2, 4, 5, 4, 6, 6)
result = find_duplicates(my_tuple)
print("Repeated items:", result)
#-----------------------------------------------------------------------------

#3. Function to count elements in a list until a tuple is encountered
def count_until_tuple(lst):
    count = 0
    for item in lst:
        if type(item) == tuple:
            break
        count += 1
    return count
my_list = [1, 2, 3, 'a', (4, 5), 6, 7]
result = count_until_tuple(my_list)
print("Number of elements before tuple:", result)
#-----------------------------------------------------------------------------

#4. Write a Python program to convert a given tuple of positive integers into an integer.
my_tuple = (1, 2, 3, 4, 5)
def convert_into_integer(my_tuple):
    result_str = ""
    for ch in my_tuple:
        temp = str(ch)
        result_str += temp
    
    result_int = int(result_str)
    return result_int
print("The converted integer is:" ,convert_into_integer(my_tuple))

#Second method
def convert_to_int(my_tuple):
    result_int = 0
    for x in my_tuple:
        result_int = result_int * 10 + x
    return result_int
print("The converted integer is:" ,convert_into_integer(my_tuple))
#-----------------------------------------------------------------------------

