# Combiantion of key-value pairs (To create a mapping)
# dict ={
#     "Aman": "Human Being",    # [key, value]
#     "Spoon": "Object"
# }
# print(dict)

# dict2 ={
#     345: "Aman",
#     456: "Isha",
#     789: "Vaibhav"
# }
# # print(dict2[456])

# # print(dict2[345])      #use this if you want to throw an error in your program if the key does not exist
# # print(dict2.get(345))  #use this if you don't want to throw an error in your program if the key does not exist


# print(dict2.keys())  #this will print all the keys
# print(dict2.values()) #this will print all the values
# print(dict2.items())  #this will print all the key-value pairs

# #this loop will iterate to all the keys and print out their values
# for key in dict2:
#     print(dict2[key])  

# for key, value in dict2.items():
#     print(f"Key: {key}, Value: {value}")


# print("\n"*3)
# # DICTIONARY METHODS
# ep1 = {
#     122: 45,
#     133: 78,
#     144: 69,
#     155: 89
# }
# ep2 = {
#     222: 45,
#     333: 77
# }
# # update() --> will update existing dict with another dict
# ep1.update(ep2)  
# print(ep1)

# #clear()
# ep2.clear()
# print(ep2)

# # pop() --> removes any key-value pair
# ep1.pop(122)
# print(ep1)

# #popitem() --> removes the last key-value pair
# ep1.popitem()
# print(ep1)

# del()

# del ep1
# print(ep1)

# del ep1[144]  # deletes a specific key-value pair
# print(ep1)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
# }

# x = car.setdefault("engine", "V8")

# print(x)

# print(car)

car = { "brand": "Ford", "model": "Mustang", "year": 1964}

x = car.get("model")
print(x)

car = { "brand": "Ford", "model": "Mustang", "year": 1964}
for x in car:
  print(x)



for x in car:
  print(car[x])


for x in car.values():
  print(x)

for x, y in car.items():
  print(x, y)
