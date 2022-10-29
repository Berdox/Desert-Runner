
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
        self.playerY_change -= 2
    def  moveDown(self):
        self.playerY_change += 2
    def  moveLeft(self):
        self.playerX_change -= 2
    def  moveRight(self):
        self.playerX_change += 2
    def  updatePlayer(self):
        self.x += self.playerX_change 
        self.y += self.playerY_change
    def  resetXYChange(self):
        self.playerX_change = 0
        self.playerY_change = 0



class Zombie(Character):
    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)
        pass
    
    def  moveDown(self):
        if(self.y > 800):
            self.y = 0
        else:
            self.y += 1;  