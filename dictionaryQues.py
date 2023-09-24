#1. Write a Python script to concatenate the following dictionaries to create a new one.
dict1 = {1 : 'a', 2 : 'b', 3 :'c'}
dict2 = {4 : 'd', 5 : 'e'}
dict3 = {6 : 'f'}
lst = [dict1, dict2, dict3]
new_dict = {}
for d in lst:
    new_dict.update(d)

print(new_dict)
#-----------------------------------------------------------------------------

#2. Write a Python script to check whether a given key already exists in a dictionary.
dict1 = {1 : 'a', 2 : 'b', 3 :'c'}
key = input("Enter the key you want to check: ")
if key in dict1.keys():
    print("Key exists")
else:
    print("Key dosen't exists")
#-----------------------------------------------------------------------------

#3. Write a Python program to sum all the items in a dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}
total_sum = 0

for value in my_dict.values():
    total_sum += value

print("Sum of all items:", total_sum)
#-----------------------------------------------------------------------------

#4. Write a Python program to map two lists into a dictionary
keys = [1, 2, 3]
values = ['a', 'b', 'c']
new_dict = {}

for i in range(len(keys)):
    key = keys[i]
    val = values[i]
    new_dict[key] = val

print(new_dict)
#-----------------------------------------------------------------------------

#5. Write a Python program to print all distinct values in a dictionary
dict = {1 : 'Aman', 2 : 'Python', 3 : 'Singh', 4 : 'IEEE', 5 : 'Aman', 6 : 'Singh'}
new_lst = []

for val in dict.values():
    if val not in new_lst:
        new_lst.append(val)

print(new_lst)
#-----------------------------------------------------------------------------
