import matplotlib.pyplot as plt
import numpy as np

#Data = [(2,1),(5,2),(7,3),(8,3)]

x = [62.5, 112,62,122.5,55,75.5,117.5,118.5,59.5,121.5]
y = [85.4,202.55,103.55,202.15,98.9,151.1,181.85,197.3,85.70,195.2]

Data = [(62.5,85.4),(112,202.55),(62,103.55),(122.5,202.15),(55,98.9),(75.5,151.1),(117.5,181.85),(118.5,197.3),(59.5,85.7),(121.5,195.2)]


x = np.zeros((10,2),dtype = int)
y = np.zeros((10,1),dtype = int)

for r in range(0,len(Data)):
    x[r][0] = 1
    x[r][1] = Data[r][0]
    y[r][0] = Data[r][1]

XtX = np.dot(x.transpose(),x)
XtY = np.dot(x.transpose(),y)
Betas = np.dot(np.linalg.inv(XtX),XtY)
print(Betas)
xp = [i[0] for i in Data]
yp = [i[0] for i in Data]
plt.plot(xp,yp,'ro')
t = np.arange(0.,200,1) 
plt.plot(t , Betas[0][0]+Betas[1][0]*t, 'g--')
plt.axis([0,200,0,250])
plt.show()


