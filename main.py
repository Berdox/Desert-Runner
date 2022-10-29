import pygame  
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
    enemyImg.append(pygame.image.load('enemy.jpg'))
    enemyX.append(random.randint(0, 340))

# Game Over
game_over_font = pygame.font.Font('over.ttf', 32)
"""
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

    pygame.display.flip()  
"""