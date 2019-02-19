import matplotlib.pyplot as plt
import numpy as np
import statistics as stats

def mean(lst):
    mean = sum(lst)/len(lst)
    return mean

def sd(xlst):
    return stats.stdev(xlst)

x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]

acme = open("acme_zyx.txt", "r")
print(acme.readlines())

print(sd(x))
plt.plot([i[0] for i in x],[i[1] for i in x],'ro')
t = np.arange(0,6,.1)
plt.plot(t,t*.65 + .5,'g--')
plt.axis([0,6,0,6])
plt.xlabel("A values")
plt.ylabel("B value")
plt.title("r = {0:.3}".format(x))
plt.show()
