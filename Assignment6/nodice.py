import random as rn
import time
start_time = time.time()



def die_roll(n):
    rolls = []
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    
    for i in range(n):
        two_dice = rn.randint(1,6) + rn.randint(1,6)
        rolls.append(two_dice)
 
    if rolls[0] == 2:
        count2 += 1
    elif rolls[0] == 3:
        count3 += 1
    elif rolls[0] == 4:
        count4 += 1
    elif rolls[0] == 5:
        count5 += 1
    elif rolls[0] == 6:
        count6 += 1
    elif rolls[0] == 7:
        count7 += 1
    elif rolls[0] == 8:
        count8 += 1
    elif rolls[0] == 9:
        count9 += 1
    elif rolls[0] == 10:
        count10 += 1
    elif rolls[0] == 11:
        count11 += 1
    else:
        count12 += 1



    return count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12



print(die_roll(1000000))
print("{0} sec".format(time.time() - start_time))
