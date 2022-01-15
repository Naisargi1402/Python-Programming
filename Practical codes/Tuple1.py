# GitHub:
# Prepared by: Naisargi Vadodariya(20CS100)

# Aim: a. Write a Python program to create a tuple with different data types.
tuple= ("tuple", False, 3.2, 1,)
print(tuple)


#b. Write a Python program to create a tuple with numbers and print one item.
tuple2=(1,67,45,78,90,145)
print(tuple2[4])


#c. Write a Python program to add an item in a tuple.
ele=input("Enter item to add in tuple: ")
tuple=tuple+ (ele,)
print(tuple)

#d. Write a Python program to convert a tuple to a string.
tup = ('C', 'S', 'P', 'I', 'T')
str = ''
for i in tup:
    str = str + i
print(str)

#e. Write a Python program to find the length of a tuple.
print(len(tup))