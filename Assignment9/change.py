import pygame
import sys
import numpy as np
import random as rn

pygame.init()
 
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
GREEN = (0,100,0)
RED =   (255,0,0)
YELLOW = (255,255,0)

class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
    
    def change_color_green(self,color):
        self.color = GREEN
    def change_color_red(self,color):
        self.color = RED
    def change_color_blue(self,color):
        self.color = BLUE
    def change_color_yellow(self,color):
        self.color = YELLOW

        
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("C200 CHANGE")


r = Rectangle(RED, [0, 0, 20, 20])


while True:
    
    pygame.time.wait(40)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
 
    screen.fill(WHITE)
 
    r.my_draw(screen)
    
    if r.loc[0] > 280:
        xd = -rn.randint(1,3)
        r.change_color_green(GREEN)
    if r.loc[1] > 280:
        yd = -rn.randint(1,3)
        r.change_color_blue(BLUE)
    if r.loc[0] < 10:
        xd = rn.randint(1,3)
        r.change_color_red(RED)
    if r.loc[1] < 10:
        yd = rn.randint(1,3)
        r.change_color_yellow(YELLOW)
    r.my_move(xd,yd)



    pygame.display.flip()
