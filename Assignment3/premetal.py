import math

# Data $/ounce
gold = 1341.30
silver = 17.19
platinum = 1005.00
palladium = 1057.95


# function 1 
# Parameters gold oz g_oz, silver oz s_oz, platinum oz pl_oz, palladium oz pa_oz
# Return the $ amount of the holdings
def cost(g_oz, s_oz, pl_oz, pa_oz):
    cost = (g_oz * 1341.30, s_oz * 17.19, pl_oz * 1005.00, pa_oz * 1057.95)
    return cost

# function 2 
# Parameters $/oz of metal value and $ amount to spend money
# Return the most WHOLE ounces that can be purchased with the money 
def how_many_oz(value, money):
    how_many_oz = money / value
    return how_many_oz


# function 3
# Parameters number of ounces of a metal metal_oz, and the metal 
# Return the amount of $ the amount is worth
def value(metal_oz, metal):
    value = metal_oz * metal
    return value

print(cost(3,0,0,0))
print(cost(0,2,0,0))
print(cost(0,0,3,0))
print(cost(0,0,0,2))
print(cost(3,1,4,5))
print(cost(2,400,3,4))


print(how_many_oz(gold,2.5*gold))
print(how_many_oz(silver,4*silver))
print(how_many_oz(platinum,math.pi*platinum))
print(how_many_oz(palladium,10/2*palladium))

print(value(10, "Au"))
print(value(10, "Ag"))
print(value(10, "Pd"))
print(value(10, "Pt"))
