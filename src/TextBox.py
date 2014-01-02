import pygame
from Box import Box
from Globals import FONTS,COLORS
class TextBox(Box):
    def __init__(self,data=None,pos=None,size=None,fontsize=14,colorbg=COLORS['white'],colorfg=COLORS['tablelight']):
        self.data=data
        self.pos=pos
        self.size=[-1,-1]
        self.fontsize=fontsize
        self.colorbg=colorbg
        self.colorfg=colorfg
        self.alpha=1000
        self.updated=False
        self.centeredx=False
        self.centeredy=True
        self.font=FONTS[self.fontsize]
        if size==None:
            self.size[0]=125
            self.size[1]=int(5*self.fontsize*len(self.data)/4+len(self.data))
        else:
            if size[0]>0:
                self.size[0]=size[0]
            else:
                self.size[0]=125
            if size[1]>0:
                self.size[1]=size[1]
            else:
                self.size[1]=int(5*self.fontsize*len(self.data)/4+len(self.data))
        Box.__init__(self,self.size,pos,self.colorbg)
        self.surf.set_alpha(self.alpha)
        if data:
            self.update(data)
    def update(self,data=None):
        self.updated=True
        self.surf.fill(self.colorbg)
        if not data==None:
            self.data=data
        yy,dy=0,int(25*self.fontsize/18)
        for datum in self.data:
            img=self.font.render(str(datum),1,self.colorfg)
            rect=img.get_rect()
            rect.top=yy
            rect.left=2
            if self.centeredx:
                rect.centerx=self.surf.get_rect().centerx
            if self.centeredy:
                rect.centery=self.surf.get_rect().centery
            else:
                rect.centery+=3
            yy+=dy
            self.surf.blit(img,rect.topleft)
    def draw(self,screen,data=None):
        self.update(data)
        self.show(screen)

