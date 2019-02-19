p = {1:10,2:25,3:32,4:41,5:60,6:100,7:130,8:141}
#INPUT number of tons of ore
#OUTPUT minimum hours to process ore
def ore(n):
    print(n)

    min = p[n]

    if n == 1:  #base
        return 10

    else: 
        for i in range(1, n):
            temp = ore(n-i) + p[i] #come back to
            if temp < min: 
                min = temp  #compt
        return min 

#memoization
x = {1:10}

#INPUT Function to memoize
#OUTPUT a lambda expression that takes ore
def m(f):
    def entry(i): #implemented another function here
        if i not in x.keys():
            x[i] = f(i)
        return x[i]
    return entry

ore = m(ore)
print(ore(7))
print(x)
x = {1:10}
print(ore(8))
print(x)

#Answers to Questions
#For ore(7), what ore hours were not calculated?
#calculated all ore hours.

#For ore(8), what ore hours were not calculated?
#it doesn't calculate anything lower than eight (if you don't reset dic)
