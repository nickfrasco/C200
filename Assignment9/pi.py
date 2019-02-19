import matplotlib.pyplot as plt
import random as rn
import math as m

len = 100
inside = 0
total = 0

for i in range(0,2000):
    x = rn.randint(0,100)
    y = rn.randint(0,100)
    if m.sqrt(((x-(len/2))**2) + ((y-(len/2))**2)) < (len/2):
        plt.plot(x,y, 'r-o')
        inside += 1
    else:
        plt.plot(x,y, 'b-o')
        total +=1

pi = 4 * (inside/(inside+total))


plt.axis([0,len,0,len])
plt.xlabel('Pi - ' + str(pi))
plt.show()

