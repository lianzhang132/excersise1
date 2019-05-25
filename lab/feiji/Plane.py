import pygame
from pygame.locals import *
from Bullet import *
class Plane(pygame.sprite.Sprite):
    def __init__(self,plane_surface,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = plane_surface
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 5

    def move(self,offset_x,offset_y):

        x = self.rect.x + offset_x*self.speed
        y = self.rect.y + offset_y*self.speed

        if x + self.rect.width > 480:
            self.rect.x = 480 - self.rect.width
        elif x < 0:
            self.rect.x = 0
        else:
            self.rect.x = x

        if y + self.rect.height > 800:
            self.rect.y = 800 - self.rect.height
        elif y < 0:
            self.rect.y = 0
        else:
            self.rect.y = y

        # print(self.rect.left)


