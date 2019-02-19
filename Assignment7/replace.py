# x is not a container
# replace(1,3,1) = 3
# replace(1,3,2) = 2

def replace(new,old,x):
    for i in range(len(x)):
        if x[i] == old:
            x[i] = new
    return x

#lst is a lister container
# you must call replace
def REPLACE(new,old,lst):
    for i in range(len(lst)):
        if x[i] == old:
            replace(new,old,lst)
            return lst
        else:
            return lst


x = [1,3,2,4,2,1,1,2,2,1]
print(REPLACE(10,1,x))
print(REPLACE(1,3,REPLACE(1,3,x)))


print("Not sure why this code isnt working")