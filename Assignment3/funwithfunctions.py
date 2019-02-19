import math


# function 1: investments 
def y(d,r,t):
    y = d * math.exp(r*t)
    return y
	
# function 2: bacteria growth
def N(n_0, m, t):
    N = n_0 * math.exp(m*t)
    return N

# function 3: alligator teeth	
def NumberTeeth(t):
    NumberTeeth = 71.8 * math.exp(-8.96 * (math.exp((-.0685)*t)))
    return NumberTeeth

# function 4: drug concentration
def K(t):
    K = ((9/2.6)*t)/(2*(t**2)+3)
    return K

# function 5: average rent
def r(t):
    r = 1.5207*(t**4) - 19.166*(t**3) + 62.91*(t**2) + 6.0726*(t) + 1026
    return r


# function 6: product profit	
def p(x):
    p = (4*(x**2)) - (100*x) - 1000

	
	
print(y(1000,.02,10))
print(N(500,100,4))
print(math.floor(NumberTeeth(1000)))
print(K(1))
print(r(4))
print(p(10))
