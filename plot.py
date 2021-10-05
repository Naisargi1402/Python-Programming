import matplotlib.pyplot as plt
import statistics
plt.plot([1, 2, 3, 4],[1, 4, 9, 16],)
plt.ylabel("square values")

Estimates=[1000, 1010, 1786, 2000, 1500, 120, 160, 1600]
y=[]

    
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]

for i in range(len(Estimates)):
    y.append(5)
    
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([375],[5],'g^')

plt.show()