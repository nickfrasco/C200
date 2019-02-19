
def F(A,B,Cin):
    if A == 0 and B == 0:
        output1 = 0
    elif A == 1 and B == 1:
        output1 = 0
    else:
        output1 = 1

    if output1 == 0 and Cin == 0:
        F = 0
    elif output1 == 1 and Cin == 0:
        F = 0
    else:
        F = 0
    return F

def G(A,B,Cin):
    if A == 0 and B == 0:
        outputAND = 0
        outputXOR = 0
    elif A == 1 and B == 0:
        outputAND = 0
        outputXOR = 1
    elif A == 0 and B == 1:
        outputAND = 0
        outputXOR = 1
    else: 
        outputAND = 1
        outputXOR = 0
    
    if outputXOR == 0 and Cin == 0:
        outputAND2 = 0
    elif outputXOR == 0 and Cin == 1:
        outputAND2 = 0
    elif outputXOR == 1 and Cin == 0:
        outputAND2 = 0
    else:
        outputAND2 = 1

    if outputAND2 == 0 and outputAND == 0:
        G = 0
    else:
        G = 1
    return G



signals = [0,1]
for A in signals:
    for B in signals:
        for Cin in signals:
            print(A,B,Cin,F(A,B,Cin),G(A,B,Cin))
        


 
   

