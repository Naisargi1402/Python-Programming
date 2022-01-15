# GitHub:
# Prepared by: Naisargi Vadodariya(20CS100)
# Aim: To check whether a given key already exists in a dictionary.


d = {1: "Naisargi", 2: "Riya", 3: "Shyam", 4: "Raj", 5: "Krupa", 6: "Dev"}
def is_key_present(x):
  if x in d:
    print('Key is present in the dictionary. The value is:')
    print(d[x])
  else:
    print('Key is not present in the dictionary')
    
key = int(input("Enter the key to find: "))
is_key_present(key)