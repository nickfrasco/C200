#created as Add New Item Python Package called mystuff
#parameter non-negative integer x
#return factorial of x 

def fact(x):
    result = 1
    for num in range(2, x+1, 1):
        result *= num
    return result

def pascal_number(row,column):
    return fact(row)/(fact(column)*fact(row-column))