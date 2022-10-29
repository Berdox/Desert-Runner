import pygame  
import random
import math

pygame.init()  
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('uhhhh')  
done = False  

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

def dspGameOver():
    game_over = game_over_font.render("GAME OVER", True,(255, 255, 255))

# Game Loop
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    # Enemy Movement
    for i in range(enemyNum):
        # Game Over 
        if enemyY[i] > 200:
            for j in range(enemyNum):
                enemyY[j] = 1000
            dspGameOver()
            break

    pygame.display.flip()  