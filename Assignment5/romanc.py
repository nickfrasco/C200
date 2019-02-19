# input paramter: a roman numeral as a string
# return the number equivalent 

def roman_to_number(n):
    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0

    for i in range(len(n)):
        if i > 0 and roman_value[n[i]] > roman_value[n[i-1]]:
            integer_value += roman_value[n[i]] - 2 * roman_value[n[i-1]]
        else: 
            integer_value += roman_value[n[i]]
    return integer_value 

n = ["XCIX", "LXXXVIII", "XII", "IX", "XXXVIII", "XXXIX"]

for i in n:
    print(roman_to_number(i))

