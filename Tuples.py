# """The difference between lists and tuple is
# you cannot change a tuple after you declare it
# i.e., it's an immutable object """

# tup = (2, 5, 6)
# print(tup)
# print(type(tup))  # O/P --> <class 'tuple'>

# tup2 = (2, 5, "green", 9.8, True)  # can store multiple datatypes
# print(tup2)

# #tuple indices
# print(tup2[0])  # positive indices
# print(tup2[3])
# print(tup2[-1]) #negative indices
# print(tup2[len(tup2) - 1])  #equivalent to tup2[len(tup2) - 1]
# print(tup2[-3])  

# if "green" in tup2:
#     print("Yes")
# else:
#     print("No")

# # tuple slicing
# print(tup2[1:])  #equivalent to print(tup2[1:len(tup2)])
# print(tup2[:4])  #equivalent to print(tup2[0:4])


# Operations on Tuples
"""
Tuples are immutable, hence if you want to add, remove or change tuple items, 
then first you must convert the tuple to a list. 
Then perform operation on that list and convert it back to tuple.
"""
# tup1 = (1, 2, 3, 4)
# print(tup1)
# temp = list(tup1)  #creating a temporary list using list() method
# temp[1] = 5
# tup1 = tuple(temp)
# print(tup1)


#performing tuple(list) comprehension 
# tuple2 = (1, 2, 3, 4)
# temp = list(i * 2 for i in tuple2)
# tuple2 = tuple(temp)
# print(tuple2)
