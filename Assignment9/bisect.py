f = lambda x: x**6 - x - 1

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def bisect(f,a,b,tau):
    c = (a+b)/2
    while (b-a)/2 > tau: 
        print("{0: .5f} {1: .5f} {2: .5f} {3: .5f} {4: .5f}".format(a,b,c,b-c,f(c)))
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0 :
            b = c
        else:
            a = c
        c = (a+b)/2
    return c
   
#print("{0: <7} {1: <7} {2: <7} {3: <7} {4: <7}".format(a,b,c,b-c,f(c)))
bisect(f,1.0,2.0,.001)

