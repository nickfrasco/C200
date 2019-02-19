import random as rn
import math
import numpy as np
import time

#Someone else's code...
#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
#changing how pivot value is determined
#probably a few errors that need to be fixed too...

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first < last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   #take first 4,3,2 values and find average
   #use the value that's nearest the average as pivot
   #in case of ties, pick the smallest value
   pivotvalue = alist[first]
  
       
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark
########################################

def bs(T,L,R):
    if R >= L:
       #print("L = {0}, R = {1}".format(L, R))
       m = math.floor((L+R)/2)
       if a[m] < T:
           L = m + 1
           return bs(T,L,R)
       elif a[m] > T: 
           R = m - 1
           return bs(T,L,R)
       else:
           return True
    else:
       return False

size = 10
a = np.zeros(size,dtype = int)
for i in range(0,size):
    a[i] = int(rn.gauss(100,40))

key = a[rn.randint(0,size-1)]
print("Looking for {0}".format(key))

print(a)
quickSort(a)
print(a)
print(bs(key,0,size))

