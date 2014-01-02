import pygame
from ImageBox import ImageBox
from Score import Score
from Globals import COLORS,FONTS,UTILITIES
class ScoreBox(ImageBox):
    def __init__(self,screen,score=Score()):
        self.pos=(10,5)
        self.dx=60
        self.dy=15
        self.dyline=5
        self.dxline=5
        self.size=(2*self.dx+self.dxline,5*self.dy+self.dyline+15)
        self.fgcolor=COLORS['yellow']
        self.font=FONTS[14]
        ImageBox.__init__(self,self.pos,self.size,COLORS['tabledark'],self.fgcolor,self.font)
        self.draw(screen,score)
    def clear(self,screen):
        self.draw(screen,Score())
    def draw(self,screen,score):
        self.erase()
        screen.blit(self.surf,self.rect.topleft)
        self.drawHeaders()
        self.drawLines()
        self.drawScore(score)
        self.show(screen)
    def drawHeaders(self):
        self.addText('N/S',(self.dx/2,self.dy/2))
        self.addText('E/W',(self.size[0]-self.dx/2,self.dy/2))
    def drawScore(self,score):
        self.addText(str(score.scores[0].over),(self.dx/2,3*self.dy/2))
        self.addText(str(score.scores[1].over),(self.size[0]-self.dx/2,3*self.dy/2))
        for iunder in range(len(score.scores[0].under)):
            under=score.scores[0].under[iunder]
            if not under==None:
                pos=(self.dx/2,5*self.dy/2+self.dyline+iunder*self.dy)
                self.addText(str(under),pos)
            if iunder>0:
                yy=5*self.dy/2+self.dyline+iunder*self.dy-self.dy/2
                start,end=(10,yy),(self.size[0]/2-10,yy)
                pygame.draw.line(self.surf,COLORS['darkyellow'],start,end,1)
        for iunder in range(len(score.scores[1].under)):
            under=score.scores[1].under[iunder]
            if not under==None:
                pos=(self.size[0]-self.dx/2,5*self.dy/2+self.dyline+iunder*self.dy)
                self.addText(str(under),pos)
            if iunder>0:
                yy=5*self.dy/2+self.dyline+iunder*self.dy-self.dy/2
                start,end=(self.size[0]/2+10,yy),(self.size[0]-10,yy)
                pygame.draw.line(self.surf,COLORS['darkyellow'],start,end,1)
    def drawLines(self):
        UTILITIES.drawHorLine(self.surf, 2*self.dy+self.dyline/2,self.fgcolor,5)
        UTILITIES.drawVerLine(self.surf, self.size[0]/2,         self.fgcolor,5)

