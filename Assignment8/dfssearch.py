from os import listdir
from os.path import isfile, join, isdir


wd = input("Working directory: ")
wdList = [join(wd,f) for f in listdir(wd) if isdir(join(wd,f))]

def show_directories(wdList):
    while wdList:
        x = wdList[0]
        wdList.remove(x)
        print(x)
        xList = [join(x,f) for f in listdir(x) if isdir(join(x,f))]
        
        if xList == true:
           xList.extend(wdList) 



show_directories(wdList)
