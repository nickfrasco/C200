f = lambda x: x**6 - x - 1
fp = lambda x: 6*(x**5) - 1
y = "lambda x: "

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)

def newton(f,fp,x,tau):
    def n(x,i):
        while f(x) > tau:
            print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
            x = x - f(x)/fp(x)
            i += 1
        return x
    n(x,0)

def function(function, tau, x0, iterations):
    function = input("Function: ")
    tau = input("Tau: ")
    x0 = input("x0: ")
    iterations = input("Iterations: ")
    
    print(newton(eval(y + function),fp,eval(x0),eval(tau)))
    

print(function(f,.0001,100,29))


#newton(f,fp,1.5,.0001)
#newton(f,fpa(f),1.5,.0001)