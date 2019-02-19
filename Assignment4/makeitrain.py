# input parameter: dollar amount x
# return value: list of quarters, dimes, nickels, and pennies
# (in that order)



def dollars(x):
    cent = x*100
    
    quarters = cent/25
        
    dimes = cent%25 / 10
        
    nickels = cent%25%10 / 5

    pennies = cent%25%10%5
   

    dollars_list = [int(quarters), int(dimes), int(nickels), int(pennies)]
    return dollars_list

print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))


