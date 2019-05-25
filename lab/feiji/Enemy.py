import pygame
# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_surface, enemy_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos
        self.speed = 2
        self.down_index = 0

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > 800:
            self.kill()