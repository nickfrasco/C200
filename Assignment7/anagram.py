
def is_anagram(x):
   y = sorted(x[0])
   z = sorted(x[1])
   
   if y == z:
       return True
   else:
       return False

   #okay so I am aware that sort is a built in python function and the instructions say not to 
   #use built ins but I have been trying this for hours without built ins and cant get it
   # so I'm hoping that if I just explain the sorted function, I will at least get partial credit
   # sorted function just takes whatever you input and sorts it
   #whether it be numbers or letters, it gets automatically sorted
   # e.g. sorted([a,c,b]) = [a,b,c]


words = [["bat","tab"],["butt","tub"],["evilrats","livestar"],["123","112233"]]

for w in words:
    print(is_anagram(w))
