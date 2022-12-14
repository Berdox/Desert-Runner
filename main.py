import pygame
from pygame.locals import *
from pygame import mixer
from Background import backgroundDraw
from Character import *
import utili

pygame.init()
pygame.mixer.init()
#setting icon
pygame.display.set_icon(pygame.image.load('./resource/pumpkin.png'))
pygame.display.set_caption('Desert Runner')

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
    
rumble = pygame.mixer.Sound("./resource/sound/rumble.wav")
rumble.set_volume(0.0)

# Background Music
mixer.music.load('./resource/sound/background.wav')
mixer.music.play(-1)

#end game screen
def show_Game_Over():
    font = pygame.font.Font('./resource/over.ttf', 80)
    text = font.render("GAME OVER", True, (255,0,0))
    screen.blit(text, (100, 350))

def show_Play_Again():
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Play Again? Press 1, or ESC to leave", True, (0,0,0))
    screen.blit(text, (35, 450))

spawn = Spawner(SCREEN_WIDTH)

over = False
while running:
    
    clock.tick(FPS)
    back.run()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
                
            if event.key == K_ESCAPE:
                running = False

            if over == True:
                if event.key == K_1:
                    over = False
                    score_value = 0
                    
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
    if over != True:
        score_value += 1
    back.run()
    utili.redraw(player)
    #pygame.mixer.Sound.play(rumble)
    
    if over != True:
        spawn.spawnZombie(utili.resize(pygame.image.load("./resource/zombie1.png").convert_alpha(), 0.3), screen)
        zombie_Sound = pygame.mixer.Sound('./resource/sound/zombie.wav')
        zombie_Sound.play()
        zombie_Sound.set_volume(0.2)
    else:
        #player_Crash = pygame.mixer.Sound('./resource/sound/explosion.wav')
        #player_Crash.play()
        show_Game_Over()
        spawn.chance = 600
        show_Play_Again()

    for i in spawn.zombiesList:
        i.moveDown()
        utili.redraw(i)
        if utili.find_collision_rect(player, i):
            for i in spawn.zombiesList:
                spawn.zombiesList.remove(i)
            over = True
            break
        if i.y > SCREEN_HEIGHT:
            spawn.zombiesList.remove(i)
    
    if (score_value/1000) % 1 == 0:
        print("score", score_value)
        spawn.changeSpawnRate(1.5)
        #changeSpeed(1)
        #back.backgSpeed(1)     
    #if not utili.find_collision_window(player, SCREEN_WIDTH, SCREEN_HEIGHT):        
    #pygame.display.flip()
    show_score(xS, yS)
    pygame.display.update()
    
    
pygame.quit()