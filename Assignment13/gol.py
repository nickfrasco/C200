import numpy as np
import random as rn
import pygame, sys
from pygame.locals import *

a = np. zeros ((32,24),dtype = list)
for i in range(0,32):
    for j in range(0,24):
        a[i][j] = [rn.randint(0,1),rn.randint(0,1)]

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640, 480))
#Ends
def terminate():
    pygame.quit()
    sys.exit()
#Draws cell at loc using color
def draw_at(loc,color):
    x,y = loc
    x = x*20
    y = y*20
    pygame.draw.rect(DISPLAYSURF, color,((x+1,y),(20-1,20-1)))

############################################################
#Generates 0,1 depending on rules
#needs fixing

def next(x,y):
    n = 0 
    active = False

    mid = a[x][y][0]
    
    if mid == 1:
        active = True

    try:
        top = a[x][y-1][0]
        if top == 1:
            n += 1
    except:
        pass

    try:
        bot = a[x][y+1][0]
        if bot == 1:
            n += 1
    except:
        pass

    try:
        leftmid = a[x-1][y][0] #lft
        if leftmid == 1:
            n += 1
    except:
        pass

    try:
        lefttop = a[x-1][y-1][0] #rule
        if lefttop == 1:
            n += 1
    except:
        pass

    try:
        leftbot = a[x-1][y+1][0] #rule
        if leftbot == 1:
            n += 1
    except:
        pass

    try:
        rightmid = a[x+1][y][0] #rght
        if rightmid == 1:
            n += 1
    except:
        pass

    try:
        righttop = a[x+1][y-1][0] #rght
        if righttop == 1:
            n += 1
    except:
        pass

    try:
        rightbot = a[x+1][y+1][0] #rght
        if rightbot == 1:
            n += 1
    except:
        pass
    
    if active:
        if n == 2 or n == 3:
            return 1
        else:
            return 0
    else:
        if n == 3:
            return 1
        else:
            return 0
    

############################################################
#Shifts the Boolean values in the list forward
def shift():
    for i in range(0,32):
        for j in range(0,24):
            a[i][j] = [a[i][j][1], next(i,j)]
    #print(a[0])
    
#Draws all the cells that have [1,x] 
def draw_all():
    for i in range(0,32):
        for j in range(0,24):
            if a[i][j][0]:
                draw_at((i,j),RED)

myclock = pygame.time.Clock()    
while True:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            terminate()
        else:
            pygame.event.clear()
            DISPLAYSURF.fill(BGCOLOR)
            draw_all()
            pygame.display.update()
            pygame.event.clear()
            myclock.tick(2)
            shift()