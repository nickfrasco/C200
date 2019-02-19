
# get library for log function
import math

# get user inputs
APR = float(input("What is your APR: %"))
C = float(input("What is the amount owed on the credit card: $"))
p = float(input("What is the monthly payment made: $"))

i = APR/12
n = -math.log10(1-(i*C/p)) / math.log10(i+1)

print("You'll make ", math.ceil(n), " payments.")

