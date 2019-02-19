import numpy as np
a = np.zeros ((4,4),dtype = float)
a[0] = [0,1,1,1]
a[1] = [0,0,0,1]
a[2] = [1,0,0,0]
a[3] = [1,1,0,0]

#input - an adjancency matrix A of 0's and 1's
#output - page rank vector
def pr(a,k):
    for row in range(len(a)):
        total = 0 #init total

        for p in range(len(a)):
            if a[row][p] == 1:
                total += 1

        for p in range(len(a)):
            a[row][p] = a[row][p]/total #division by tot
            
    
    vector = np.zeros(len(a))

    T = np.transpose(a)

    for i in range(len(vector)):
        T = np.dot(T,T)
  
    for i in range(len(vector)):
        vector[i] = 1/(len(vector))
    
    fin = np.dot(T,vector)

    return fin

print(pr(a,8))