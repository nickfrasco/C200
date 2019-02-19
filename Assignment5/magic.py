import numpy as np

#Got some help on this one from my brother

#parameter takes 2d numpy array
#returns True if magic square
def is_magic_square(x):
    Size = len(x[0])
    sumlist = []
    
    for column in range(Size):
        sumlist.append(sum(row [column] for row in x))
    
    sumlist.extend([sum (lines) for lines in x])
    
    linesResult = 0
    for i in range(0,Size):
        linesResult += x[i][i]
    sumlist.append(linesResult)  
    
    rowResult = 0
    for i in range(Size -1, -1, -1): 
        rowResult += x[i][i]
    sumlist.append(rowResult)

    if len(set(sumlist))>1:
        
        return False
    
    return True

#Code to get numbers from text file
magic_file = input("Magic number file: ")

lt = []


with open(magic_file, "r") as magic:
    all_lines = magic.read().splitlines()
    for line in all_lines:
      lt = lt + [[int(x) for x in line.split(" ")]]


#Build a 2d array
magic_size = len(lt)
ma = np.zeros((magic_size, magic_size), dtype = int)

#Populate the array from the list
for i in range(0,magic_size):
    for j in range(0, magic_size):
        ma[i][j] = lt[i][j]

#You can uncomment to print the array
print(ma)

print(is_magic_square(ma))
