def s(n):
    #sums numbers. find the limit  on your system of the recursion depth
    if n == 0:
        sum = 0
    else:
        sum = s(n-1) + n
    return sum

def s1(n):
    if n == 0:
        sum = 0
    else:
        sum = n*(n+1)/2
    return sum

def p(n):
    if n == 0:
        years = 10000
    else:
        years = p(n-1) + 0.2*p(n-1)
    return years

def p1(n):
    if n == 0:
        years = 10000
    else: 
        years = (1.02)**n * 10000
    return years

def b(n):
    if n == 1:
        number = 2
    elif n == 2:
        number = 3
    else:
        number = b(n-1) + b(n-2)
    return number

def c(n):
    if n == 1:
        number = 9
    else:
        number = 9 * c(n-1) + 10**(n-1) - c(n-1)
    return number

def d(n):
    if n == 0:
        number = 1
    else:
        number = 3 * d(n-1) + 1
    return number

def d1(n):
    if n == 0:
        number = 1
    else: 
        number = (3**(n+1) + 1) / 2
    return number 


print(s(2))
print(s1(2))
print(p(2))
print(p1(2))
print(b(2))
print(c(2))
print(d(2))
print(d1(2))


