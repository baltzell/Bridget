import pygame
from Globals import COLORS,UTILITIES
class Box():
    def __init__(self,size,pos=None,bgcolor=COLORS['table']):
        self.surf=pygame.Surface(size,1).convert()
        self.rect=self.surf.get_rect()
        screenrect=pygame.display.get_surface().get_rect()
        if pos==None:
            self.rect.centerx=screenrect.centerx
            self.rect.centery=screenrect.centery
        else:
            if pos[0]<0:
                self.rect.centerx=screenrect.centerx
            else:
                self.rect.left=pos[0]
            if pos[1]<0:
                self.rect.centery=screenrect.centery
            else:
                self.rect.top=pos[1]
        self.bgcolor=bgcolor
        self.visible=False
        self.erase()
    def erase(self):
        self.surf.fill(self.bgcolor)
    def show(self,screen):
        self.visible=True
        screen.blit(self.surf,self.rect.topleft)
    def hide(self,screen):
        self.visible=False
        surf=self.surf.copy()
        surf.fill(COLORS['table'])
        screen.blit(surf,self.rect.topleft)
    def transient(self,screen):
        if self.visible:
            self.hide(screen)
        else:
            surf=screen.copy()
            screen.blit(self.surf,self.rect.topleft)
            pygame.display.flip()
            UTILITIES.pause()
            screen.blit(surf,(0,0))
        pygame.display.flip()
    def toggle(self,screen):
        if self.visible:  self.hide(screen)
        else:             self.show(screen)

