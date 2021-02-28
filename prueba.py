import pygame,sys,random,time
import numpy as np

pygame.init()

width, height = 400,400
screen = pygame.display.set_mode((width,height))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    pygame.draw.point(screen,255,(200,200))
    pygame.display.flip()