import numpy as np
import matplotlib.pyplot as plt

def error(s, x):
    return abs((s-x**2)/(2*x))

def bakhshali(s, epsilon, estimate):
    x = estimate
    i = 0
    v[i] = error(s,x)
    g[i] = x
    while error(s,x) > epsilon:
        i += 1
        a = (s-x**2)/(2*x)
        x = x + a - (a**2) / (2*(x+a))
        v[i] = error(s,x)
        g[i] = x
        print(x,error(s,x))
    return x

def square_root(s,epsilon,estimate):
    x = estimate
    i = 0
    v[i] = error(s,x)
    g[i] = x
    while error(s,x) > epsilon:
        i += 1
        a = (s - x**2) / (2*x)
        x = x + a - (a**2) / (2*(x+a))
        v[i] = error(s,x)
        g[i] = x
        print(x,error(s,x))
    return x

v = np.zeros(10)
g = np.zeros(10)
t1 = np.arange(1,8,1)

plt.ylabel("Initial Estimate")
plt.xlabel("Iterations")
plt.title("Convergence of Square Root")

print(square_root(1000,.00005,500))
plt.plot(t1,v[t1],"r-o")

print(square_root(1000,.00005,775))
plt.plot(t1,v[t1],"b-o")

print(square_root(1000,.00005,3))
plt.plot(t1,v[t1],"g-o")

plt.show()
