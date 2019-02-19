#Input Parameter: a decimal value n
# Return value: a string containing the roman numeral representation of n
def roman(n):
   number = ""
   while n > 0:
       if n >= 90:
           number += "XC"
           n-= 90
       elif n >= 50:
           number += "L"
           n-= 50 
       elif n >= 40:
           number += "XL"
           n -= 40 
       elif n >= 10:
           number += "X"
           n -= 10
       elif n == 9:
           number += "IX"
           n -= 9
       elif n >= 5:
           number += "V" 
           n -= 5
       elif n == 4:
           number += "IV"
           n -= 4
       elif n == 3:
            number += "III"
            n -= 3
       else:
           number += "I"
           n -= 1

   return number

for i in range(1,100):
    if i % 5 == 0:
        print()
    print(i, roman(i), ", ", end="")
 