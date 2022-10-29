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