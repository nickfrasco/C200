def min(x,y):
    if x < y:
        return x
    else:
        return y

def MIN(lst):
#TO DO: Implement function
    if range(0,lst,1) == 1:
        return lst[0]
    else:
        return min(x,MIN(lst))


# for loop and index into list
def min1(x):
    small = x[0]
    for i in range(1,len(x)):
        if x[i] < small:
            small = x[i]
    return small


# for loop and list iteration
def min2(x):
    small = x[0]
    for i in x[1:]:
        if i < small:
            small = i
    return small


# while loop and index
def min3(x):
    small = x[0]
    i = 0
    while (i < len(x)):
        if x[i] < small:
            small = x[i]
        i = i + 1
    return small


# while loop list iteration
def min4(x):
    small = x[0]
    r = x[1:]
    while (r):
        if r[0] < small:
            small = r[0]
        r = r[1:]
    return small

# for loop reverse index
def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

x = [1,42,-1,22,0,12]

mf = [MIN, min1, min2, min3, min4, min5]

for f in mf:
    print("{0}({1}) = {2}".format(f.__name__,x,f(x)))
