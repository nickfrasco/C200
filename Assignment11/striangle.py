import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    x,y = loc
    z = math.sqrt((width**2) - (width/2)**2)
    t = [x + (width/2),y]

    l = [x,y+z]

    r = [x + width,z+y]

    return [t,l,r]

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, BLUE , (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    z = math.sqrt((width**2) - (width/2)**2)
    if width > 1:
        x,y = loc
        draw_triangle(loc,width)
        s((x+(width/4),y),width/2)
        s((x,z/2+y),width/2)
        s(((x+width/4), z/2 + y), width/2)
    else:
        return 


s((0,0),440)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()