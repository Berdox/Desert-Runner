'''import pygame  
import random
import math


pygame.init()  
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('uhhhh')  
done = False   
# Initialing Color
color = (255,0,0)
  

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

# Game Loop
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()  

    # Enemy Movement
    for i in range(enemyNum):
        # Game Over 
        if enemyY[i] > 200:
            for j in range(enemyNum):
                enemyY[j] = 1000
            dspGameOver()
            break
'''
from timeit import repeat
import pygame
from Background import backgroundDraw
from Character import Player

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
back = backgroundDraw(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
back.getResources()

def redraw(image):
    image.parent_screen.blit(image.loc, (image.x, image.y))
    pygame.display.flip()

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