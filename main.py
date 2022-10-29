'''import pygame  
import random
import math

# Initialize pygame
pygame.init()  

# Create Screen
screen = pygame.display.set_mode((480,800))

# Caption
pygame.display.set_caption('uhhhh')

# Icon
icon = pygame.image.load('./resource/pumpkin.png')
pygame.display.set_icon(icon)

# Background

# Sound

# Player
playerImg = pygame.image.load('./resource/block.jpg')
playerX = 220
playerY = 600
playerX_change = 0
playerY_change = 0

"""
# Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyNum = 10

for i in range(enemyNum):
    enemyImg.append(pygame.image.load('./resource/block.jpg'))
    enemyX.append(random.randint(0, 340))

# Game Over
game_over_font = pygame.font.SysFont('Comic Sans MS', 24)

def dspGameOver():
    game_over = game_over_font.render("GAME OVER", True,(255, 255, 255))

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
done = False 
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()  

        # Check Keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change


    screen.fill((0, 0, 0))

    player(playerX, playerY)
    pygame.display.update()
"""
    # Enemy Movement
    for i in range(enemyNum):
        # Game Over 
        if enemyY[i] > 200:
            for j in range(enemyNum):
                enemyY[j] = 1000
            dspGameOver()
            break
'''
import pygame
from pygame.locals import *
from Background import backgroundDraw
from Character import *

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
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
                    
                if event.key == K_UP:
                    player.moveUp()
                
                if event.key == K_DOWN:
                    player.moveDown()
                
                if event.key == K_LEFT:
                    player.moveLeft()
                    
                if event.key == K_RIGHT:
                    player.moveRight()
                    
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    redraw(player)
    zombie.moveDown()
    redraw(zombie)
    back.run()