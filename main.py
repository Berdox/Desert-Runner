import pygame
from pygame.locals import *
from Background import backgroundDraw
from Character import *
import utili

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

#player make
locP = utili.resize(pygame.image.load("./resource/cartrans.png").convert_alpha(), 0.18)
xP = 250
yP = 700
player = Player(locP, xP, yP, screen)
utili.redraw(player)

#make score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
xS = 10
yS = 10

def show_score(xS, yS):
    score1 = score_value/1000
    score = font.render("Kilometers: " + str(score1), True, (0,0,0))
    screen.blit(score, (xS, yS))

spawn = Spawner(SCREEN_WIDTH)

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
    score_value += 1
    back.run()
    utili.redraw(player)
    
    spawn.spawnZombie(pygame.image.load("./resource/block.jpg").convert(), screen)

    for i in spawn.zombiesList:
        print(i.x)
        i.moveDown()
        utili.redraw(i)
        if utili.find_collision_rect(player, i):
            running = False
        if i.y > SCREEN_HEIGHT:
            spawn.zombiesList.remove(i)
            print("delete")
            
    #if not utili.find_collision_window(player, SCREEN_WIDTH, SCREEN_HEIGHT):        
    #pygame.display.flip()
    show_score(xS, yS)
    pygame.display.update()
    
pygame.quit()