import pygame
from Globals import DECKDEFS,COLORS,UTILITIES
class Effects:
    def drawTrace(self,screen,img,pos0,pos1,nsteps,step0=0,step1=None):
        if step1==None:
            step1=nsteps
        surf=pygame.Surface(img.get_rect().size).convert()
        surf.blit(img,(0,0))
        oldscreen=screen.copy()
        for istep in range(step0,step1):
            xx=pos0[0]+istep*(pos1[0]-pos0[0])/nsteps
            yy=pos0[1]+istep*(pos1[1]-pos0[1])/nsteps
            screen.blit(surf,(xx,yy))
            pygame.display.flip()
            screen.blit(oldscreen,(0,0))
            pygame.display.flip()
    def drawCongrats(self,screen):
        font=pygame.font.SysFont('verdana',80)
        scrrect=screen.get_rect()
        cardimg=DECKDEFS.backimage
        cardrect=cardimg.get_rect()
        fontimg=font.render("Bridget 0.1a",1,COLORS['black'])
        fontrect=fontimg.get_rect()
        fontpos=(scrrect.centerx-fontrect.width/2,scrrect.centery-fontrect.height/2)
        used=[]
        x,y,dx,dy=0,0,17,17
        while 1:
            new=1
            for uu in used:
                if uu[0]==x and uu[1]==y:
                    new=0
                    break
            if new==0:
                break
            used.append((x,y))
            screen.blit(cardimg,(x,y))
            oldscreen=screen.copy()
            screen.blit(fontimg,fontpos)
            pygame.display.flip()
            screen.blit(oldscreen,(0,0))
            x+=dx
            y+=dy
            if x+cardrect.right>scrrect.right or x<scrrect.left:
                dx=-dx
                x+=dx
            if y+cardrect.bottom>scrrect.bottom or y<scrrect.top:
                dy=-dy
                y+=dy
        UTILITIES.pause()
        screen.fill(COLORS['table'])
    def drawSimpleIntro(self,screen):
        font=pygame.font.SysFont('verdana',50)
        scrrect=screen.get_rect()
        cardimg=DECKDEFS.backimage
        cardrect=cardimg.get_rect()
        data=['Bridget 0.1a']
        yy=30
        for datum in data:
            fontimg=font.render(datum,1,COLORS['black'])
            fontrect=fontimg.get_rect()
            fontpos=(scrrect.centerx-fontrect.width/2,yy)
            screen.blit(fontimg,fontpos)
            yy+=60
        x0,dx=20,10 ; x=x0
        while 1:
            b=scrrect.centerx-cardrect.width/2
            c=scrrect.bottom-cardrect.height*3/2
            y=(x0-c)*pow(b-x,2)/pow(x0-b,2)+c
            if x+x0+cardrect.width>scrrect.right:
                break
            screen.blit(cardimg,(x,y))
            pygame.display.flip()
            x+=dx
        UTILITIES.pause()
        screen.fill(COLORS['table'])
EFFECTS=Effects()

