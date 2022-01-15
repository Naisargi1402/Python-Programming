# GitHub:
# Prepared by: Naisargi Vadodariya(20CS100)
from collections import Counter 
#Aim: a. Write a Python program to add member(s) in a set and clear a set
colors = set()
print("Add single element:")
colors.add("Red")
print(colors)
print("Add multiple items:")
colors.update(["Blue", "Green"])
print(colors)
colors.clear()
print(colors)

#b. Write a Python program to remove an item from a set if it is present in the set.
num = set([0, 1, 2, 3, 4, 5])
print(num)
temp=int(input("Enter element to remove :"))
if temp in num:
    num.discard(temp)
    print("Element removed successfully")
    print(num)
    
else:
    print("Element not found in Set!")
    
#c. Write a Python program to create an intersection, Union, difference of sets.
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
# union
print("Union :", A | B)
# intersection
print("Intersection :", A & B)
# difference
print("Difference :", A - B) 
# symmetric difference
print("Symmetric difference :", A ^ B)

#d. Write a Python program to find maximum and the minimum value in a set.
print("Maximum :", max(num))
print("Minimum :", min(num))

#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list = [9, 4, 5, 4, 4, 5, 9, 5, 4]
# printing original list
print ("Original list : " + str(list))
# using max() + set() to get most frequent element
res = max(set(list), key = list.count)
      
# printing result
print ("Most frequent number is : " + str(res)+"\nThe count is : " , list.count(res))


tuple=(1,67,45,78,1,45,1) 
print ("Original tuple : " + str(tuple))
res = max(set(tuple), key = tuple.count)
print ("Most frequent number is : " + str(res)+"\nThe count is : " , tuple.count(res))

dict={1:10, 2:20,3:10}
print ("Original Dictionary : " + str(dict))
value, count = Counter(dict.values()).most_common(1)[0]
print ("Most frequent number is : " , value,"\nThe count is : " , count)
  