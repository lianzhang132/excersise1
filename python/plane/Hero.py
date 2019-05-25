#我方飞机

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_surface, position):
        pygame.sprite.Sprite.__init__(self)
        #给精灵设置界面
        self.image = hero_surface
        #给精灵设置位置
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.speed = 5

    def move(self,offset_x,offset_y):
        if self.rect.x + offset_x*self.speed < 0:
            self.rect.x = 0
        elif self.rect.x + offset_x*self.speed > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.x = self.rect.x + offset_x*self.speed

        if self.rect.y + offset_y*self.speed < 0:
            self.rect.y = 0
        elif self.rect.y + offset_y*self.speed > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.y = self.rect.y + offset_y*self.speed
