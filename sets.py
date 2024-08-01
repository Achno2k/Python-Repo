# Sets -> Unordered collection of unique objects
my_set = {1, 2, 3, 4, 5} 
print(my_set)

my_set = {1, 2, 3, 4, 5, 5} #it won't take duplicate values
print(my_set)

my_set.add(100)
print(my_set)
my_set.clear()   #clears the whole set and creates an empty set

my_list = [1,2,3,4,5,5]
my_set1 = set(my_list)    #set() converts a list to a set and removes all the duplicates
print(my_set1)

# These does not support indexing
print(1 in my_set)

# Some important methods
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8}

print(my_set.difference(your_set)) #This returns a new set containing elements that are in my_set but not in your_set.
print(my_set.intersection(your_set)) #This returns a new set containing elements that are common to both my_set and your_set.

my_set.discard(3)
print(my_set)

my_set.difference_update(your_set)
print(my_set)

print(my_set.isdisjoint(your_set)) #This returns True if my_set and your_set have no elements in common.
print(my_set.union(your_set)) #This returns a new set containing all unique elements from both my_set and your_set.

print(my_set.issubset(your_set)) #This returns False because not all elements of my_set are in your_set.
print(my_set.issuperset(your_set)) #This returns False because my_set does not contain all elements of your_set.