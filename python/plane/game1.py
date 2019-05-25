import pygame
from pygame.locals import *
from random import *
# https://www.cnblogs.com/wuzhanpeng/p/4271312.html
# https://www.pygame.org/docs/ref/surface.html
class Bullet(pygame.sprite.Sprite):

     def __init__(self, bullet_surface, bullet_init_pos):
         pygame.sprite.Sprite.__init__(self)
         self.image = bullet_surface
         self.rect = self.image.get_rect()
         self.rect.topleft = bullet_init_pos
         self.speed = 8

     # 控制子弹移动
     def update(self):
         self.rect.top -= self.speed
         if self.rect.top < -self.rect.height:
             self.kill()


WIDTH = 480
HEIGHT = 800
# 飞机个数
ticks = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('我的游戏')

background = pygame.image.load('resources/image/background.png')

plane_img = pygame.image.load('resources/image/shoot.png')

hero1_rect = pygame.Rect(0, 99, 102, 126)
hero2_rect = pygame.Rect(165, 360, 102, 126)

hero1 = plane_img.subsurface(hero1_rect)
hero2 = plane_img.subsurface(hero2_rect)
#飞机起始点
hero_pos = [200, 300]
#移动的距离
offset_x = offset_y = 0
dis = 3
clock = pygame.time.Clock()
#子弹图片
bullet1_surface = plane_img.subsurface(pygame.Rect(1004, 987, 9, 21))
while True:
    # Player((randint(0, WIDTH), randint(0, HEIGHT)))
    bullet = Bullet(bullet1_surface,(randint(0, WIDTH), randint(0, HEIGHT)))
    print(bullet)
    bullet.update()
    clock.tick(0)
    screen.blit(background,(0,0))
    # screen.blit(hero1, hero_pos)

    #让飞机动起来
    if ticks%50 < 25:
        screen.blit(hero1, hero_pos)
    else:
        screen.blit(hero2, hero_pos)
    pygame.display.update()
    ticks+=1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                offset_x=-1*dis
            elif event.key == pygame.K_d:
                offset_x = dis
            elif event.key == pygame.K_w:
                offset_y = -1*dis
            elif event.key == pygame.K_s:
                offset_y = dis
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                offset_x=0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                offset_y = 0

    if hero_pos[0] + offset_x < 0:
        hero_pos[0] = 0
    elif hero_pos[0] + offset_x > WIDTH - hero1_rect.width:
            hero_pos[0] = WIDTH - hero1_rect.width
    else:
            hero_pos[0] = hero_pos[0] + offset_x

    if hero_pos[1] < 0:
        hero_pos[1] = 0
    elif hero_pos[1] > HEIGHT - hero1_rect.height:
        hero_pos[1] = HEIGHT - hero1_rect.height
    else:
        hero_pos[1] = hero_pos[1] + offset_y



