  
class Character:
    
    def __init__(self, resourceLocation, x, y, parent_Screen):
        self.loc = resourceLocation
        self.x = x
        self.y = y
        self.parent_screen = parent_Screen
        
class Player(Character):
    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)
        pass
    
    def  moveUp(self):
        self.y -= 0.2
    def  moveDown(self):
        self.y += 0.2
    def  moveLeft(self):
        self.x -= 0.2
    def  moveRight(self):
        self.x += 0.2