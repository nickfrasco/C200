

def parse(x):
    if len(x) >= 3 and len(x) <= 4:
        return False
    else:
        return True




s = [":)",":-(!", ":--)", "><:", ":+(!!!!!!", ":)!!!", ":)!("]

for i in s: 
    print(parse(i))
