import pygame
from Globals import UTILITIES, DECKDEFS
class Card:
    def __init__(self,sorhori,rank=None):
        self.index=UTILITIES.index(sorhori,rank)
        self.name =UTILITIES.name(self.index)
        self.color=UTILITIES.color(self.index)
        self.suit =UTILITIES.suit(self.index)
        self.rank =UTILITIES.rank(self.index)
        self.isuit=UTILITIES.isuit(self.index)
        self.irank=UTILITIES.irank(self.index)
        self.fimg =UTILITIES.image(self.index)
        self.smallimg=UTILITIES.smallimage(self.index)
        self.bimg=DECKDEFS.backimage
        self.img=self.bimg
    def __eq__(self,cardorindex):
#        if cardorindex==None:
#            return None
        if type(cardorindex) is int:
            return self.index==cardorindex
        else:
            return self.index==cardorindex.index
    def __ne__(self,card):
        return not self.__eq__(card)
    def faceDown(self):
        self.img=self.bimg
    def faceUp(self):
        self.img=self.fimg
    def draw(self,surface,pos):
        surface.blit(self.img,pos)
    def drawFaceUpSmall(self,surface,pos):
        surface.blit(self.smallimg,pos)
    def getSurface(self):
        return pygame.Surface(self.img.get_rect().size).convert()

