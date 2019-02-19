import math

def speed(d, t):
    speed = d/t
    return speed

def distance (s, t):
    distance = s*t
    return distance


def time (s, d):
    time = d/s
    return time


def hours_to_min(hours):
    numberHours = hours*60
    return numberHours


def min_to_sec(min):
    numberMin = min*60
    return numberMin


def feet_to_mile(feet):
    numberFeet = feet/5280
    return numberFeet


def miles_to_kilometers(miles):
    numberMiles = miles*1.60934
    return numberMiles

def k_to_m(k):
    numberKilometers = k/1.60934
    return numberKilometers


def miles_to_feet(miles):
    numberMiles = miles*5280
    return numberMiles


def degrees_to_radians(degrees):
    numberDegrees = degrees * (math.pi/180)
    return numberDegrees


def loc_c(a,b,gamma):
    lengthA = a
    lengthB = b
    lenghtC = gamma * (math.pi/180)
    return lenghtC

def c_to_f(celcius):
    numberDegreesF = celcius * 9/5 + 32 
    return numberDegreesF


def f_to_c(fahrenheit):
    numberDegreesC = (fahrenheit - 32) / (9/5)
    return numberDegreesC


def k_to_f(kelvin):
    numberKelvin = kelvin * (9/5) - 459.67
    return numberKelvin


def pc(price,value):
    if price < 0:
        priceChange = -(1-((price+value)/price))
        return priceChange
 
    else:
        priceChange = ((price + value)/price) - 1
        return priceChange


def p_to_k(parsecs):
    numberParsecs = parsecs/(3.086 * (10*10*10*10*10*10*10*10*10*10*10*10*10))
    return numberParsecs


def ly_to_p(lightyear):
    numberLightYears = lightyear * 3.26
    return numberLightYears


#####################################
# DATA                              #
#####################################
s1 = 75      # miles/hours
t1 = 4       # hours
t2 = 2020    # min
t3 = 414241  # sec
d1 = 100     # miles
d2 = 1442412 # feet

#Tests

print(speed(d1,t1), "miles/hour")
print(miles_to_kilometers(speed(d1,t1)), "kilometers/hour")
print(miles_to_kilometers(speed(d1,t1))/min_to_sec(hours_to_min(1)), "kilometers/sec")
print(c_to_f(-30), "Fahrenheit")
print(min_to_sec(hours_to_min(1)), "seconds")
print(f_to_c(-22), "Celcius")
print(c_to_f(20), "Fahrenheit")
print(k_to_f(293), "Fahrenheit")
print(f_to_c(k_to_f(293)), "Celcius")
print(loc_c(8,11,37), " units")
print(degrees_to_radians(30), "radians")
print(pc(170.90,3.31), "percent change")
print(pc(170.90,-3.31), "percent change")
print(p_to_k(231), "kilometers")
print(k_to_m(p_to_k(ly_to_p(3.5))), "miles")
print(feet_to_mile(d2), "miles")

