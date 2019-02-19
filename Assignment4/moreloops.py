# Input Parameter: a list of numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(x):
    highest_num = x[0]

    for num in x:
        if num > highest_num:
            highest_num = num
    return highest_num


# Input Parameter: a list of numbers x
# Returns: the minimal number value in list x (does not have to be unique)
def minFor(x):
    lowest_num = x[0]

    for num in x:
        if num < lowest_num:
            lowest_num = num
    return lowest_num


# Input Parameters: a number x and a list of numbers lst
# Returns: the list lst with all occurrences of x removed
def myRemove(x, lst):
    if x == int():
        if x == lst[0] or lst[1] or lst[2] or lst[3] or lst[4] or lst[5] or lst[6] or lst[7] or lst[8] or lst[9] or lst[10] or lst[11]:
            lst = [w.replace(x,'') for w in lst]
        return lst
    else:
        if x == lst[0] or lst[1] or lst[2] or lst[3] or lst[4] or lst[5] or lst[6] or lst[7]:
            lst = [w.replace(x,'') for w in lst]
        return lst



# Input Parameters: a number oldX, a number newX and a list of numbers lst
# Return Value: the list lst with all occurrences of oldX replaced with newx
def myReplace(oldx, newX, lst):
  # if type(lst) == str:
  #      lst = [w.replace(oldx, newX) for w in lst]
  # return lst
  for i in range(len(lst)):
      if (lst[i]==oldx):
          lst[i]=newX
  return lst



# Input Parameters: two lists x and y, x = [x1, x2, x3, ..., xk] and y = [y1, y2, y3, ..., yk]
# Returns: a new list with the following structure [x1, y1, x2, y2, x3, y3, ..., xk, yk]
# Note: assume that both lists are same length
def myLeftMerge(x, y): 
    new_list = []
    for numA in x:
        for numB in y:
            new_list = [numA] + [numB]
    return new_list

# Input Parameter: takes a list of lists of numbers [[x1, x2, x3, ..., xn], [y1, y2, y3, ..., ym],...]
# Returns: a single list of numbers where each element is product of the 
# inner list at that position, [x1*x2*x3**xn, y1*y2*y3**ym, ...]
def listProducts(x):
    product1 = 1
    for num in x[0]:
        product1 *= num 
   
    product2 = 1
    for num in x[1]:
        product2 *= num

    product3 = 1
    for num in x[2]:
        product3 *= num
    return [product1, product2, product3]



# Input Parameter: a list x of objects [x1, x2, x3,..., xn]
# Returns: a list with the string objects removed
def removeString(x):
    y = []
    for str in range(1,len(x)):
        x[str] = y
    return x
    

# Input Parameter: a string x
# Returns: the string with all vowels, upper and lower case removed
def removeVowels(x):
   # y = "a"
   # t = "e"
   # z = "i"
   # b = "o"
   # c = "u"

   # if y or t or z or b or c in x:
    #    x[y] = '_'
    #    x[t] = '_'
    #    x[z] = '_'
    #    x[b] = '_'
    #    x[c] = '_'
    #return x
    srt = ""

    for n, i in enumerate(a):
        for i in x:
            srt+= i 
        if i == 'a' or 'e' or 'i' or 'o' or 'u':
            x[n] = '0'


# Data
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b","a","c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]


for i in nlst:
    print(minFor(i))
    print(maxFor(i))

print(myRemove("a",a))
print(myRemove("b",a))
print(myRemove("z",a))
#print(myRemove(1,b))
#print(myRemove(2,b))
#print(myRemove("a",b))
print(myReplace("a",":)",a))
print(myReplace(1,0,b))
#print(removeVowels("the lazy brown fox jumped over the eager dog"))
print(listProducts([[1],[2,3,4],[10,10,10,10]]))
print(removeString(["This",1, "is", "very", 3, [4], "exciting"]))
print(myLeftMerge(a,b))
print(myLeftMerge(['aa','bb'],[1,2]))