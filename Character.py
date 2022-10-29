  
class Character:
    
    def __init__(self, resourceLocation, x, y, parent_Screen):
        self.loc = resourceLocation
        self.x = x
        self.y = y
        self.parent_screen = parent_Screen
        
class Player(Character):
    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)