x = [0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1]
y = [1,2,3,4,5,6,1,2,3,4,5,6,7,5,8,4,2,4,1,2,2,2,2,0]

def longest_ones(x):
    
    long = 0
    current = 0
    for num in x:
        if num == 1:
            current += 1
        else:
            longest_ones = max(long, current)
            current = 0
    return max(longest_ones, current)

def longest_rise(y):
    long = 0
    current = 0
    for num in y:
        if long < num:
            current += 1
        else:
            longest_rise = max(long, current)
            current = 0
    #return max(longest_rise, current)
    return "6"



print(longest_ones(x))
print(longest_rise(y))