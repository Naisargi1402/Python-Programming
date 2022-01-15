# GitHub:
# Prepared by: Naisargi Vadodariya(20CS100)
# Aim: Python script to concatenate dictionaries to create a new one

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print("Concatenated Dictionary =", dic1)