def f(x):
    return x**6 - x - 1

def secant(f,x0,x1,tau):
    n = 1
    while n <= tau:
        x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        if x2 - x1 < x1:
            return x2
        else: 
            x0 = x1
            x1 = x2
    print("{0: <2} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(n,x0,f(x0),f(x1),x0-x1))
    #n+=1
    return False


    
#print("{0: <2} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(n,x0,f(x0),f(x1),x0-x1))


secant(f,2.0,1.0,.0001)
