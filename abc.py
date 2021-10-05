students={'Ajay':10,'shw':3,'pqr':2}
s=''
for i in students:
    s=s+ str(students[i])+' '
    s1 = s[:-1]
    
print(s1[::-1])