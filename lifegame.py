import pygame,sys,random,time
import numpy as np

pygame.init()

tSize = 10
mapsizeX, mapsizeY = 40,40
width, height = mapsizeX*tSize, mapsizeY*tSize
screen = pygame.display.set_mode((width,height))

colorbg = 127,127,127


tiles = [[0 for i in range(mapsizeX)] for j in range(mapsizeY)]

tiles[20][21] = 1
tiles[20][20] = 1
tiles[20][19] = 1

# print(tiles)
screen.fill(colorbg)

def checkPos (pos):
    life = 0
    life += tiles[(pos[0]-1)%mapsizeX][(pos[1]-1)%mapsizeY]
    life += tiles[(pos[0]-1)%mapsizeX][(pos[1])%mapsizeY]
    life += tiles[(pos[0]-1)%mapsizeX][(pos[1]+1)%mapsizeY]
    life += tiles[(pos[0])%mapsizeX][(pos[1]-1)%mapsizeY]
    life += tiles[(pos[0])%mapsizeX][(pos[1]+1)%mapsizeY]
    life += tiles[(pos[0]+1)%mapsizeX][(pos[1]-1)%mapsizeY]
    life += tiles[(pos[0]+1)%mapsizeX][(pos[1])%mapsizeY]
    life += tiles[(pos[0]+1)%mapsizeX][(pos[1]+1)%mapsizeY]
    # for x in range(-1,2):
    #     for y in range(-1,2):
    #         if tiles[(pos[0]+x)%mapsizeX][(pos[1]+y)%mapsizeY] == 1 :
    #             if (x + y != 0) : life += 1
    return life

def draw ():
    for x in range(mapsizeX):
        for y in range(mapsizeY):  
            X = x*tSize
            Y = y*tSize
            pos = ((X+1,Y+1),(tSize-1,tSize-1))
            pygame.draw.rect(screen,[tiles[x][y]*255]*3,pos)

draw()
pygame.display.flip()
state = False
pause = False
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: pause = not pause
    newTiles = np.copy(tiles)

    # newState = pygame.mouse.get_pressed()[2]
    # if newState and newState != state:
    #     pause = not pause
    
    # state = newState
    if pause:
        if sum(pygame.mouse.get_pressed()) > 0 :
            posM = list(pygame.mouse.get_pos())
            posM[0] = int((posM[0])/tSize)
            posM[1] = int((posM[1])/tSize)
            tiles[posM[0]][posM[1]] = pygame.mouse.get_pressed()[0]

    else:
        for x in range(mapsizeX):
            for y in range(mapsizeY):
                life = checkPos((x,y))
                if life == 3:
                    newTiles[x][y] = 1
                elif newTiles[x][y] == 1 and life == 2:
                    newTiles[x][y] = 1
                else:
                    newTiles[x][y] = 0
        tiles = newTiles 

    draw()

    time.sleep(0.1)
    pygame.display.flip()
