import pygame

SCREEN_WIDEH = 480
SCREEN_HEIGHT = 800
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_surface,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.speed = 2
        self.down_index = 0

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y >SCREEN_HEIGHT:
            self.kill()