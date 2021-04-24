import pygame,sys,random,time
import numpy as np
#cambio
pygame.init()

tSize = 10
mapsizeX, mapsizeY = 40,40
width, height = mapsizeX*tSize, mapsizeY*tSize
screen = pygame.display.set_mode((width,height))

colorbg = 127,127,127

tiles = [[0 for i in range(mapsizeX)] for j in range(mapsizeY)]
mode = 1

# print(tiles)
screen.fill(colorbg)

def checkPos (pos, type):
    life = 0
    life += tiles[(pos[0]-1)%mapsizeX][(pos[1]-1)%mapsizeY]
    life += tiles[(pos[0])%mapsizeX][(pos[1]-1)%mapsizeY]
    life += tiles[(pos[0]+1)%mapsizeX][(pos[1]-1)%mapsizeY]
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
            tiles[posM[0]][posM[1]] = mode if pygame.mouse.get_pressed()[0] == 1 else 0
        draw()
    else:
        for x in range(mapsizeX):
            for y in range(mapsizeY):
                life = checkPos((x,y),newTiles(x,y))
        tiles = newTiles 
        draw()
        time.sleep(0.1)
    
    pygame.display.flip()
