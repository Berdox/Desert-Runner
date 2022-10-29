  
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
        pass
    def  moveDown(self):
        pass            
    def  moveLeft(self):
        pass
    def  moveRight(self):
        pass