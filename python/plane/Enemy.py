#敌机

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_surface, position):
        pygame.sprite.Sprite.__init__(self)
        #给精灵设置界面
        self.image = enemy_surface
        #给精灵设置位置
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.speed = 1
        self.down_index = 0

    def update(self, *args):
        self.rect.y += self.speed
        #子弹会飞出屏幕外面
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()
