# input parameter: a string x
# Return value: True if x is a palindrome, False otherwise

def palindrome(x):
    x = x
    y = x[::-1]
     
    if x == y:
        return True
    else:
        return False

print(palindrome("aba"))
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama"))
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))