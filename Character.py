import random

SPEED = 4

def changeSpeed(num):
    global SPEED 
    SPEED += num
    
class Character:
    
    def __init__(self, resourceLocation, x, y, parent_Screen):
        self.loc = resourceLocation
        self.x = x
        self.y = y
        self.parent_screen = parent_Screen
        
class Player(Character):
    playerX_change = 0
    playerY_change = 0

    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)
        pass
    
    def  moveUp(self):
        self.playerY_change -= SPEED
    def  moveDown(self):
        self.playerY_change += SPEED
    def  moveLeft(self):
        self.playerX_change -= SPEED
    def  moveRight(self):
        self.playerX_change += SPEED
    def  updatePlayer(self):
        if self.x <= 10:
            self.x = 10
        if self.x >= 450:
            self.x = 450
        self.x += self.playerX_change 
        self.y += self.playerY_change
    def  resetXYChange(self):
        if self.y <= 25:
            self.y = 25
        if self.y >= 750:
            self.y = 750
        self.playerX_change = 0
        self.playerY_change = 0

class Zombie(Character):
    
    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)
        pass
    
    def  moveDown(self):
        if(self.y > self.parent_screen.get_height()):
            self.y = 0
        else:
            self.y += SPEED;  
        
class Spawner:
    zombiesList = []
    chance = 600
    
    def __init__(self, screenWidth):
        self.width = screenWidth
    
    def spawnZombie (self, loc, screen):
        ran = random.randint(0, self.chance)
        if ran < 10:
            Swidth = random.randint(0, self.width)
            self.zombiesList.append(Zombie(loc, Swidth, -10, screen))
    
    def changeSpawnRate(self, num):
        self.chance = int(self.chance / num)       