import pygame
pygame.init()

width, height = 400, 400
FPS = 30
screen = pygame.display.set_mode((width,height))
fpsClock = pygame.time.Clock()
class Player:
    position = list((0,0))
    velocity = 0,0
    size = 20,40
    color = 255,255,255
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color
    def draw(self):
        rect = pygame.Rect(self.position,self.size)
        rect.move_ip(-self.size[0]/2,-self.size[1]/2)
        pygame.draw.rect(screen,self.color,rect)
    def update(self):
        print(self.velocity)
        self.position = self.position[0]+self.velocity[0],self.position[1]+self.velocity[1]
        self.draw()
    def setvel(self, vel):
        print(vel)
        self.velocity = vel[0],vel[1]

player = Player((200,200),(20,40),[255]*3)
while True:
    screen.fill([0]*3)
    pygame.draw.line(screen,(255,0,0),(200,000),(200,400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                player.setvel((1,0))
            elif event.key == pygame.K_RIGHT:
                player.setvel((-1,0))
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                player.setvel((0,0))
            elif event.key == pygame.K_RIGHT:
                player.setvel((0,0))
    player.update()
    pygame.display.flip()
    fpsClock.tick(FPS)