import pygame
import sys
import random
import numpy as np
# cambio
FPS = 15
tSize = 5
mapsizeX, mapsizeY = 100, 100
size = mapsizeX*tSize, mapsizeY*tSize
UIspace = 60
# width, height = mapsizeX*tSize, mapsizeY*tSize
# screen = pygame.display.set_mode((width, height))
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((size[0]+UIspace, size[1]),flags)
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

pygame.font.init()

pixels = pygame.PixelArray(game_screen)
check = 5
def checkPos(x, y, newtiles):
    global tiles
    global check
    if(check > 0 and y == 0):
        check -= 1
        print(y)
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

class Button :
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")

button1 = Button("Arena",(size[0]+8,20),20,bg=colors[1],feedback="hola")
draw()
pygame.display.flip()
register = False
painting = False
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                painting = 1
            if event.button == 3:
                register = 1
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                painting = 0
            if event.button == 3:
                register = 0
        button1.click(event)
    posM = list(pygame.mouse.get_pos())
    posM[0] = int((posM[0])/tSize)
    posM[1] = int((posM[1])/tSize)
    if painting == 1:
        tiles[posM[0]][posM[1]] = mode

    if register == 1:
        print(str(posM) + " "+ str(tiles[posM[0]][posM[1]]))


    newTiles = np.copy(tiles)
    for x in range(mapsizeX):
        for y in range(mapsizeY):
            checkPos(x, mapsizeY-y-1, newTiles)

    tiles = newTiles 
    draw()
    clock.tick(FPS)
    # pygame.transform.scale(game_screen, screen.get_size())
    screen.blit(pygame.transform.scale(game_screen, size), (0, 0))
    button1.show()

    pygame.display.flip()
