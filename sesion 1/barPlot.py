import matplotlib.pyplot as plt
import numpy as np


v = np.array([25,50,100,150,200,300,400,500,600,700,800,900,1000])
q = np.array(v)
pr = [] 
for i, _ in enumerate(v):
    pr.append("Value: "+str(i))
    v[i] *= 1000
    q[i] *= 1230
print("Mean", np.mean(q))
v = np.sort(v)
print("Max", q[len(q)-1])
print("Min", q[0])





plt.bar(pr,v)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()

