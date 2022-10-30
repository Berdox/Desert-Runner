import pygame
from pygame.locals import *
from Background import backgroundDraw
from Character import *

pygame.init()
#setting icon
pygame.display.set_icon(pygame.image.load('./resource/pumpkin.png'))

#setting screen dimesions and setting up screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

#make background
back = backgroundDraw(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
back.getResources()

FPS = 60
clock = pygame.time.Clock()

def redraw(image):
    image.parent_screen.blit(image.loc, (image.x, image.y))

#player make
locP = pygame.image.load("./resource/block.jpg").convert()
xP = 250
yP = 100
player = Player(locP, xP, yP, screen)
redraw(player)

locZ = pygame.image.load("./resource/block.jpg").convert()
xZ = 250
yZ = 0
zombie = Zombie(locZ, xZ, yZ, screen)
redraw(zombie)


while running:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    running = False
                    
                if event.key == K_UP:
                    player.moveUp()
                
                if event.key == K_DOWN:
                    player.moveDown()
                
                if event.key == K_LEFT:
                    player.moveLeft()
                    
                if event.key == K_RIGHT:
                    player.moveRight()

        if event.type == KEYUP:
            player.resetXYChange()
                    
        if event.type == pygame.QUIT:
            running = False
    
    player.updatePlayer()

    back.run()
    redraw(player)
    zombie.moveDown()
    redraw(zombie)
    #pygame.display.flip()
    pygame.display.update()
    
pygame.quit()