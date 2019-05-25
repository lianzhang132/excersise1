# -*- coding = utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from random import randint
from Plane import *
from Bullet import *
from Enemy import *
import time


SPEED = 10

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('我的第一个小游戏')

background_img = pygame.image.load('./resources/image/background.png')
hero_img = pygame.image.load('./resources/image/shoot.png')

plane1_rect = pygame.Rect(0,99,102,126)
plane2_rect = pygame.Rect(165,360,102,126)
bullet_rect = pygame.Rect(1004,987,9,21)
enemy_rect = pygame.Rect(534, 612, 57, 43)
enemy_down_rect = pygame.Rect(930, 697, 51, 43)

enemy_down_surface = []
enemy_down_surface.append(hero_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy_down_surface.append(hero_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy_down_surface.append(hero_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy_down_surface.append(hero_img.subsurface(pygame.Rect(930, 697, 57, 43)))

plane1_surface = hero_img.subsurface(plane1_rect)
plane2_surface = hero_img.subsurface(plane2_rect)
bullet_surface = hero_img.subsurface(bullet_rect)
enemy_surface = hero_img.subsurface(enemy_rect)

hero_surface = []
hero_surface.append(hero_img.subsurface(pygame.Rect(0, 99, 102, 126)))
hero_surface.append(hero_img.subsurface(pygame.Rect(165, 360, 102, 126)))
hero_surface.append(hero_img.subsurface(pygame.Rect(165, 234, 102, 126)))
hero_surface.append(hero_img.subsurface(pygame.Rect(330, 624, 102, 126)))
hero_surface.append(hero_img.subsurface(pygame.Rect(330, 498, 102, 126)))
hero_surface.append(hero_img.subsurface(pygame.Rect(432, 624, 102, 126)))

# 游戏结束图
gameover = pygame.image.load('resources/image/gameover.png') # new
hero_position = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+200)

def index():
    plane = Plane(plane1_surface, hero_position)
    clock = pygame.time.Clock()
    offset_x = offset_y = 0
    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemies_down = pygame.sprite.Group()
    i = 0
    score = 0
    while True:
        screen.blit(background_img,[0,0])
        i += 1
        clock.tick(60)

        if i%100 == 0:
            enemy_pos = [randint(0, SCREEN_WIDTH - enemy_surface.get_width()), 0]
            enemy = Enemy(enemy_surface,enemy_pos)
            enemy_group.add(enemy)

        enemy_group.update()
        enemy_group.draw(screen)

        if i % 30 >= 15:
            plane.image = plane1_surface
        else:
            plane.image = plane2_surface

        screen.blit(plane.image,plane.rect)

        if i%10 == 0:
            bullet = Bullet(bullet_surface, [plane.rect.x+plane.rect.width//2,plane.rect.y])
            bullet_group.add(bullet)

        # 控制子弹
        bullet_group.update()
        # 绘制子弹
        bullet_group.draw(screen)

        # 检测敌机与子弹的碰撞 *******************************************
        enemies_down.add(pygame.sprite.groupcollide(enemy_group, bullet_group, True, True))
        for enemy1_down in enemies_down:
            screen.blit(enemy_down_surface[enemy1_down.down_index], enemy1_down.rect)
            if i % 10 == 0:
                enemy1_down.down_index += 1
                if enemy1_down.down_index == 4:
                    score += 1
                    enemies_down.remove(enemy1_down)

        # ************************************************************
        enemy1_down_list = pygame.sprite.spritecollide(plane, enemy_group, True)
        if len(enemy1_down_list) > 0:
            break

        # 绘制得分
        score_font = pygame.font.Font(None, 50)
        score_text = score_font.render('score: ' + str(score), True, (0, 255, 0))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    offset_y = -1
                if event.key == pygame.K_DOWN:
                    offset_y = 1
                if event.key == pygame.K_LEFT:
                    offset_x = -1
                if event.key == pygame.K_RIGHT:
                    offset_x = 1

            if event.type == pygame.KEYUP:
                offset_x = offset_y = 0

        plane.move(offset_x,offset_y)
        pygame.display.update()


index()
screen.blit(gameover, (0, 0))

# 绘制得分
score_font1 = pygame.font.Font(None, 50)
score_text1 = score_font1.render(('reset'), True, (255, 255, 0))
text_rect1 = score_text1.get_rect()
text_rect1.topleft = hero_position
screen.blit(score_text1, text_rect1)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= text_rect1.x and pos[0] <= text_rect1.x+text_rect1.width and pos[1] >= text_rect1.y and pos[1] <= text_rect1.y+text_rect1.height:
                index()
                screen.blit(gameover, (0, 0))
                pygame.display.update()