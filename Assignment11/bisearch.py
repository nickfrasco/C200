import random as rn
import math
import numpy as np
import time


#inputting (Key,0,size)

def bs(T,L,R):
   if R >= L:
       m = math.floor((L+R)/2)
       if a[m] < T:
           R = T - 1
           L = m + 1
           return bs(T,L,R)
       elif a[m] > T: 
           R = m - 1
           return bs(T,L,R)
       else:
           return m
   else:
       return -1



#([5],0,10000000)
#(Key,0,size)

 

size = 10000000
a = np.zeros(size,dtype = int)
for i in range(0,size):
    a[i] = int(rn.gauss(10000,300))

key = a[rn.randint(0,size)]
print("Looking for {0}".format(key))

stime = time.time()
found = False
for i in range(0,size):
    if a[i] == key:
        found = True
        break
print("{0} Sec {1} ".format(time.time()-stime,bool(True*found)))

#Default is quicksort
a.sort()

stime = time.time()
print("{0} sec {1} ".format(time.time()-stime,bool(True*bs(key,0,size))))
