# # LISTS
# marks = [3, 5, 6]  #this is a list
# print(marks)       #to print the list
# print(type(marks)) 

# #list index start with 0
# print(marks[0])    #this will print the element at the index 0

# #lists can store multiple datatypes
# l = [1,2,"Aman", True]    #list with different datatypes
# print(l)
# print(len(l))

# #negative index
# #--------------
# l = [3, 5, 6, 7]
# print(l[-3]) #negative index
# print(l[len(l)-3])
# print(l[4-3])
# print(l[1])
# #all the above print statements will give you the same output


# if 7 in l:
#     print("Present in list!")
# else:
#     print("Not present in list!")


# #this same thing applies for strings as well
# if "str" in l:
#     print("Present!")
# else:
#     print("Not present!")

# print(l)
# #works the same as string slicing
# print(l[:])    # equivalent to [0:len(l)]
# print(l[1:3])  # the syntax here is [start : end : step]

# #List Comprehension
# lst = [i for i in range(5)]
# print(lst)
# lst = [i*i for i in range(5) if i%2==0]
# print(lst)



"""
LIST METHODS
============
"""
lst = [1, 2, 3, 4, 5]
# print(lst)

# lst.append(7) # appends a new element at the end of the list
# lst.sort() # sorts the whole list in increasing order
# lst.reverse() # reverses the whole list
# lst.sort(reverse=True) # sorts the whole list in decreasing order
# print(lst.index(4)) # returns the index of the element
# print(lst.count(4)) # returns the count of the element
# lst.insert(0, 900)
# m  = [900, 1000, 2000]
# k = lst + m    # this will concatenate two given lists to a new one
# lst.extend(m)  # this will also concatenate the given list to a different list
# print(f"k = {k}") 
# print(f"lst = {lst}")
# l = lst.copy() # this will copy the existing list to a new list
# print(l)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#2-D Lists
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[0][1])   #should print 2
for row in matrix:
  for item in row:
    print(item)

sum = 0
for row in matrix:
  for item in row:
    sum += item
print(sum)

#UNPACKING A LIST
lst = [1, 2, 3]
x, y, z = lst
print(x, y, z)