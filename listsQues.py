# #Write a Python program to get the largest number from a list.
# lst = [12, 34, 65, 2, 11]
# max = lst[0]
# for x in lst:
#     if max < x:
#         max = x
# print("The maximum element in the list is: ", max)

# #Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# lst = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for item in lst:
#     if item[0] == item[len(item) - 1]:
#         count = count + 1
# print("Result:", count)

# # Write a Python program to print the numbers of a specified list after removing even numbers from it.
# lst = [12, 33, 49, 122, 56, 73]
# newlst = []            
# for i in lst:
#     if i % 2 != 0:
#         newlst.append(i)
# print(newlst)