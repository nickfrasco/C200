import numpy as np

def next(b):
    count = 0 
    alive = False #start false
    for i in b:
        for j in i:
            if j:
                count += 1
    if b[1][1] == 1:
        alive = True #true??
        count -= 1
    if alive:
        if count == 2 or count == 3:
            return 1
        else:
            return 0
    else:
        if count == 3:
            return 1
        else:
            return 0

w = np.zeros ((3,3),dtype = int)
w[0][1] = 1
w[1][1] = 1



x = np.zeros ((3,3),dtype = int)
x[0][1] = 1
x[1][0] = 1 



y = np.zeros ((3,3),dtype = int)
y[0][1] = 1
y[1][2] = 1
y[2][0] = 1



z = np.zeros ((3,3),dtype = int)
z[0][1] = 1
z[1][1] = 1
z[2][0] = 1
z[2][1] = 1



print(next(w))
print(next(x))
print(next(y))
print(next(z))