X = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True

#1#################
if b:
    print("Happy")
elif y:
    print("Valentines")
else:
    print("day!")

###################


#2#################

if (z > a):
    print("C200")
elif 2*a > z:
    print("C200")
else:
    print("is bliss")

###################


#3#################
if x and y:
    print(a)
if not x and y:
    print(a)
if not X:
    print(a)
if not y:
    print(a) 

#if not (not (x and y) or not x):
 #   print(a)

###################



#4#################

if (2 > z):
    print("1")
if X:
    print("1")
if 2 == 1:
    print("2")
if y and not x:
    print("3")
else:
    print("4")

###################


#5########################

def f(x):
    return (x==4)*100 + (x==3)*10 + (x==2)*1000 + (x!=4)*(x!=3)*(x!=2)* 100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))
#########################
