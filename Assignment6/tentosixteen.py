#number n in base 10 to base 16

def d(n,b):
    n = hex(n).split('x')[-1] #built-in hex function
    n = n.upper() #make upper case
    return n

print(d(200,16))
print(d(689,16))
