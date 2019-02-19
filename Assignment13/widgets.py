# dictionary that encodes table of machines named
f = {1:[0,2,5,6,7], 2:[0,1,3,6,7], 3:[0,1,4,5,8]}

#INPUT dictionary of machines--you can assume there are 3 machines
# number of total hours that must be greater than 0
#Return list of [t1,t2,t3,max] where t1 =(1,h1); t2=(2,h2); t3 = (3,h3)
#h1 is hours on machine 1, h2 is hours on machine 2, h3 is hours on machine 3
#max is maximum widgets

def mm(f,hours):
    max = [0,0,0,0] #init
    hrs1 = -1
    for i in f[1]:
        hrs1 += 1 #
        hrs2 = -1 #

        for j in f[2]:
            hrs2 += 1
            hrs3 = -1

            for k in f[3]:
                hrs3 += 1

                if (hrs1 + hrs2 + hrs3) <= 4:
                    if (i + j + k) > max[3]:
                        max = [hrs1,hrs2,hrs3,i+j+k]
    return max



print(mm(f,4))