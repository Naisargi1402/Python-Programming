# GitHub:
# Prepared by: Naisargi Vadodariya(20CS100)
# Aim: Python script to merge two Python dictionaries.

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
     
# Driver code
dict1 = {'a': 100, 'b':200}
dict2 = {'c': 40,'d': 60}
dict3 = Merge(dict1, dict2)
print(dict3)