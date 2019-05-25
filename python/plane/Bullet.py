#我方子弹

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_surface, position):
        pygame.sprite.Sprite.__init__(self)
        #给精灵设置界面
        self.image = bullet_surface
        #给精灵设置位置
        self.rect = self.image.get_rect()
        self.rect.centerx = position[0]
        self.rect.y = position[1]-10
        self.speed = 5

    def update(self, *args):
        self.rect.y -= self.speed
        #子弹会飞出屏幕外面
        if self.rect.y < 0:
            self.kill()
