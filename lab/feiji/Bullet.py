import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self,img,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
        self.speed = 8
        self.down_index = 0


    def update(self, *args):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()
