import pygame
from Globals import DECKDEFS,COLORS,UTILITIES
class TrickWinner():
    def __init__(self):
        self.pos=((0,-95),(90,0),(0,95),(-90,0))
        self.dirs=('d','l','u','r')
        self.surf=pygame.Surface((10,10),1).convert()
        self.rect=self.surf.get_rect()
        self.colorfg=COLORS['yellow']
    def getPos(self,screen,iseat):
        screenrect=screen.get_rect()
        pos=[screenrect.centerx,screenrect.centery]
        pos[0]+=(self.pos[iseat])[0]-self.rect.width/2
        pos[1]+=(self.pos[iseat])[1]-self.rect.height/2
        return pos
    def clear(self,screen):
        self.surf.fill(COLORS['table'])
        for iseat in range(DECKDEFS.nseats):
            screen.blit(self.surf,self.getPos(screen,iseat))
    def draw(self,screen,trickwinner):
        self.clear(screen)
        for iseat in range(DECKDEFS.nseats):
            if iseat==trickwinner:
                UTILITIES.drawArrowHead2(self.surf,self.colorfg,self.dirs[(iseat+2)%4])
                #self.drawArrow(self.dirs[iseat])
                screen.blit(self.surf,self.getPos(screen,iseat))
                break
    def drawArrow(self,direction):
        UTILITIES.drawArrow(self.surf,self.colorfg,direction,3)

