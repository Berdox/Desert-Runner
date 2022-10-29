import pygame
from Background import backgroundDraw
from Character import Player

pygame.init()
#setting icon
pygame.display.set_icon(pygame.image.load('./resource/pumpkin.png'))
#setting screen dimesions and setting up screen
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

#make background
back = backgroundDraw(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
back.getResources()

def redraw(image):
    image.parent_screen.blit(image.loc, (image.x, image.y))
    pygame.display.flip()

#player make
locA = pygame.image.load("./resource/block.jpg").convert()
xP = 250
yP = 100
player = Player(locA, xP, yP, screen)
redraw(player)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    redraw(player)
    back.run()