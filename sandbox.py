import pygame
import sys
import random
import numpy as np
# cambio
FPS = 15
tSize = 5
mapsizeX, mapsizeY = 100, 100
# width, height = mapsizeX*tSize, mapsizeY*tSize
# screen = pygame.display.set_mode((width, height))
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((mapsizeX*tSize, mapsizeY*tSize),flags)
game_screen = pygame.Surface((mapsizeX, mapsizeY))
colorbg = 127, 127, 127
colors = {
        0: (0, 0, 0),
        1: (255, 0, 0),
        2: (255, 255, 0)
        }
tiles = [[0 for i in range(mapsizeX)] for j in range(mapsizeY)]
mode = 2
"""
0-nada
1-tierra
2-arena
"""

screen.fill(colorbg)
clock = pygame.time.Clock()
pixels = pygame.PixelArray(game_screen)

def checkPos(x, y, newtiles):
    global tiles
    if y < mapsizeY-1 and newtiles[x][y] == 1:
        if newtiles[x][y+1] == 0:
            newtiles[x][y+1] = 1
            newtiles[x][y] = 0

    if y < mapsizeY-1 and newtiles[x][y] == 2:
        if newtiles[x][y+1] == 0:
            newtiles[x][y+1] = 2
            newtiles[x][y] = 0
        elif x > 0 and newtiles[x-1][y+1] == 0 :
            newtiles[x-1][y+1] = 2
            newtiles[x][y] = 0
        elif x < mapsizeX-1 and newtiles[x+1][y+1] == 0 :
            newtiles[x+1][y+1] = 2
            newtiles[x][y] = 0


def draw():
    for x in range(mapsizeX):
        for y in range(mapsizeY):
            # X = x*tSize
            # Y = y*tSize
            # pos = ((X+1, Y+1), (tSize-1, tSize-1))
            color = colors[tiles[x][y]]
            # pygame.draw.rect(screen, color, pos)
            pixels[x][y] = color


draw()
pygame.display.flip()
state = False
painting = False
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            painting = 1
        if event.type == pygame.MOUSEBUTTONUP:
            painting = 0
    
    if painting == 1:
        posM = list(pygame.mouse.get_pos())
        posM[0] = int((posM[0])/tSize)
        posM[1] = int((posM[1])/tSize)
        tiles[posM[0]][posM[1]] = mode

    newTiles = np.copy(tiles)
    for x in range(mapsizeX):
        for y in range(mapsizeY):
            checkPos(x, mapsizeY-y, newTiles)

    tiles = newTiles 
    draw()
    clock.tick(FPS)
    # pygame.transform.scale(game_screen, screen.get_size())
    screen.blit(pygame.transform.scale(game_screen, screen.get_size()), (0, 0))
    pygame.display.flip()
