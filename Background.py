from turtle import width
import pygame

class backgroundDraw:
    
    width = 0
    height = 0
    yValue = 0
    index = 0
    index2 = 1
    background = []
    
    def __init__(self, widthScreen, heightScreen, window):
        self.width = widthScreen
        self.height = heightScreen
        self.screen = window
    
    def getResources(self):
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0178.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0197.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0213.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0232.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0250.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0268.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0286.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0304.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0322.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0340.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0358.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0377.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0396.png"), (self.width, self.height)))
        self.background.append(pygame.transform.scale(pygame.image.load("./resource/repeat/0411.png"), (self.width, self.height)))
        
        
    def run(self):
        self.screen.blit(self.background[self.index], [0,self.yValue])
        if self.yValue == self.height:
            self.yValue = 0
            self.index +=1
            self.index2 +=1
        else:
            self.yValue += 1
        if self.index == len(self.background) - 1:
            self.index2 = 0
        if self.index2 == 1:
            self.index = 0
        self.screen.blit(self.background[self.index2], [0, -self.height+self.yValue])

        pygame.display.update()
            

