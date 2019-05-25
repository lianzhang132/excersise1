import pygame

SCREEN_WIDEH = 480
SCREEN_HEIGHT = 800
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_surface,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.centerx = position[0]
        self.rect.y = position[1]-11
        self.speed = 6
    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.y<0:
            self.kill()