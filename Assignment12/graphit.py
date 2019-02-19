import math
import pygame, sys
from pygame.locals import *
import numpy as np

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    def add_edge(self, pair):
        start, end = pair
        self.edges[start].append(end)
    def children(self, node):
        if node in self.nodes:
            return self.edges[node]
        else:
            return None
    def __str__(self):
        finalString = ""
        for n in self.nodes:
            finalString += str(n) + " -> " + str(self.edges[n]) + "\n"
        return finalString

#INPUT two loc of circles
#RETURN where to place line
def edge_loc(loc1,loc2):
    x1,y1 = loc1
    x2,y2 = loc2
    return ((x1+25,y1+25),(x2-25,y2-25))

#INPUT cloc is triangle that is rotated and nloc is new location
#RETURN a tuple that moves cloc to nloc
def translate(cloc,nloc):
    list = []
    for i in cloc:
        list.append((i[0]+nloc[0]-41,i[1]+nloc[1]-50))
    return tuple(list) #return as a tuple



#INPUT loc is tuple of points ((x1,y1),(x2,y2),...,(xn,yn)) and angle how much rotate (in degrees)
#RETURN a tuple of points that are each rotated ((rx1,ry1), (rx2,ry2), ... ,(rxn,ryn))
def rotate(loc,angle):
    angle = (math.pi*angle)/180
    rm = np.zeros((2,2),dtype = float)
    list = []
    for i in loc:
        ry = math.sin(angle-25)*i[0] + math.sin(angle+45)*i[1]
        rx = math.cos(angle+25)*i[0] - math.sin(angle-25)*i[1]

        list.append((rx,ry))
    return tuple(list)


#INPUT loc and width
#RETURN arrowhead location 
def arrow(loc,width):
    x,y = loc
    w = math.floor(width/2)
    h = math.floor((math.sqrt(3)/2)*width)
    return ((x+w,y),(x,y+h),(x+width,y+h))

#INPUT loc and font size
#RETURN where to place the font 
def label_loc(loc,font_size):
    x,y = loc
    return (x-font_size/4,y-font_size/2)

#COLORS
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#Setting up pygames
pygame.init()
pygame.font.init() 
pygame.display.set_caption('C200 Graphing')
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 30)
size = [640, 480]
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


#Draw (1,2)
loc1 = (100,100) #location of 1
loc2 = (250,250) #location of 2
pygame.draw.circle(screen, blue, loc1, 25, 1)
pygame.draw.circle(screen,blue, loc2, 25, 1)
#Something's not quite right...
e1, e2 = edge_loc(loc1,loc2)
pygame.draw.line(screen, black,e1,e2,2)
#Rotated and translated arrow
pygame.draw.polygon(screen,black, translate(rotate(arrow((0,0),30) ,10),loc2), 0)

#Write labels for nodes here
label1 = font_renderer.render("1",1,red)
label2 = font_renderer.render("2",1,red)

#Each label needs a blit call
screen.blit(label1, label_loc(loc1,30))
screen.blit(label2, label_loc(loc2,30))
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

