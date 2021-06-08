import pygame
import sys
import random
import numpy as np
pygame.font.init()

tSize = 5
mapsizeX, mapsizeY = 100, 100
size = mapsizeX*tSize, mapsizeY*tSize
UIspace = 60
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((size[0]+UIspace, size[1]),flags)
game_screen = pygame.Surface((mapsizeX, mapsizeY))
pixels = pygame.PixelArray(game_screen)
clock = pygame.time.Clock()
FPS = 15

colorbg = 127, 127, 127
colors = {
        0: (0, 0, 0),
        1: (109, 46, 18),
        2: (255, 255, 0)
        }
tiles = [[0 for i in range(mapsizeX)] for j in range(mapsizeY)]
mode = 2
"""
0-nada
1-tierra
2-arena
"""

def checkPos(x, y, newtiles):
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
    global mode
    global colors
    for x in range(mapsizeX):
        for y in range(mapsizeY):
            color = colors[tiles[x][y]]
            pixels[x][y] = color

class Button :
    def __init__(self, text,  pos, bg="black", mode=1):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", 20)
        self.mode = mode
        self.textRaw = text
        self.bg = bg
        self.pressed = 0
        self.change(bg)

    def change(self, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(self.textRaw, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        if mode == self.mode:
            self.change(self.bg)
        else:
            self.change()
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        global mode
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    mode = self.mode

buttons = list()
buttons.append(Button("Tierra",(size[0]+8,20),bg=colors[1],mode=1))
buttons.append(Button("Arena",(size[0]+8,60),bg=colors[2],mode=2))

screen.fill(colorbg)
draw()
pygame.display.flip()

register = False
painting = False
while True:    
    screen.fill(colorbg)
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
        buttons[0].click(event)
        buttons[1].click(event)
    posM = list(pygame.mouse.get_pos())
    posM[0] = int((posM[0])/tSize)
    posM[1] = int((posM[1])/tSize)
    if painting == 1:
        if posM[0] < mapsizeX:
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
    screen.blit(pygame.transform.scale(game_screen, size), (0, 0))

    font = pygame.font.SysFont(None, 24)
    img = font.render(str(mode), True, colors[0])
    screen.blit(img, (size[0], 0))
    buttons[0].show()
    buttons[1].show()

    pygame.display.flip()
