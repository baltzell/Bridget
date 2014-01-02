import pygame
from Box import Box
class ImageBox(Box):
    def __init__(self,pos,size,colorbg,colorfg,font):
        self.font=font
        self.colorfg=colorfg
        Box.__init__(self,size,pos,colorbg)
    def addImage(self,pos,img):
        imgrect=img.get_rect()
        imgrect.centerx=pos[0]
        imgrect.centery=pos[1]
        self.surf.blit(img,imgrect.topleft)
    def addText(self,text,pos):
        img=self.font.render(text,1,self.colorfg)
        self.addImage(pos,img)

