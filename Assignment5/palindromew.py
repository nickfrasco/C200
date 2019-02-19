# input parameter: a string x
# Return value: True if x is a palindrome, False otherwise

def palindromew(x):
    x = x
    y = x[::-1]

    while x == y:
        return "True" 
    while x != y:
        return "False"

print(palindromew("aba"))
print(palindromew("a"))
print(palindromew("abba"))
print(palindromew("amanaplanacanalpanama"))
print(palindromew("abca"))
print(palindromew("ac"))
print(palindromew("adabbba"))
print(palindromew("amandaplanacanalpanama"))
