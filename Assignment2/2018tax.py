# 1 Finish this function
# Calculates the taxes an unmarried person owes for 2018
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def unmarriedTax(income):
    if income > 0 and income < 9525:
        unmarriedTax = (.10 * income)
        return unmarriedTax

    elif income > 9525 and income < 38700:
        unmarriedTax = (.12 * income)
        return unmarriedTax

    elif income > 38700 and income < 157500:
        unmarriedTax = (.22 * income)
        return unmarriedTax

    elif income > 157500 and income < 200000:
        unmarriedTax = (.24 * income) 
        return unmarriedTax

    elif income > 200000 and income <500000:
        unmarriedTax = (.35 * income) 
        return unmarriedTax

    else: 
        unmarriedTax = (.37 * income)
        return unmarriedTax
        


# 2 Finish this function
# Calculates the taxes a married person owes for 2018
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)

def marriedTax(income):
    if income > 0 and income < 19050:
        marriedTax = (.10 * income)
        return marriedTax

    elif income > 19050 and income < 77400:
        marriedTax = (.12 * income) 
        return marriedTax

    elif income > 77400 and income < 315000:
        marriedTax = (.22 * income)
        return marriedTax

    elif income > 315000 and income < 400000:
        marriedTax = (.24 * income) 
        return marriedTax

    elif income > 400000 and income < 600000:
        marriedTax = (.35 * income) 
        return marriedTax

    else: 
        marriedTax = (.37 * income)
        return marriedTax

# Calculates the taxes an individual owes for 2018
# Input Parameters: amount of income in USD income and marital status
#  Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
    if(maritalStatus):
        return marriedTax(income)
    else:
        return unmarriedTax(income)

############################
# DATA
############################
Ursala_married = True
Ursala_income = 252225

Kaiser_married = False
Kaiser_income = 375000

Shilah_married = True
Shilah_income = 77399

############################
# TESTS
############################
print("Ursala owes ", tax(Ursala_income, Ursala_married))
print("Kaiser owes ", tax(Kaiser_income, Kaiser_married))
print("Shilah owes ", tax(Shilah_income, Shilah_married))
