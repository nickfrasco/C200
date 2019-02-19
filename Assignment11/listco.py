import numpy as np
np.seterr(divide='ignore',invalid='ignore')
#Above statement was used to ignore an error message
#that read "invalid value encountered in true_divide"

Data = [(2,1),(5,2),(7,3),(8,3)]

X = np.zeros((4,2),dtype = int)
Y = np.zeros((4,1),dtype = int)

for r in range(0,len(Data)):
    X[r][0] = 1
    X[r][1] = Data[r][0]
    Y[r][0] = Data[r][1]

S_y = sum(Y)
S_x2 = sum(X**2)
S_x = sum(X)
S_xy = sum(X*Y)


Beta_0 = (S_y*S_x2 - S_x*S_xy)/(4*S_x2-(S_x)**2)
print(Beta_0)
Beta_1 = (4*S_xy - S_x*S_y)/(4*S_x2 - (S_x)**2)
print(Beta_1)

