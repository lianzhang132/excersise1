# 导入pygame模块以及其中的所有常量
import pygame
import pygame.time
from pygame.locals import *
from Hero import Hero
from Bullet import Bullet
from Enemy import Enemy
from random import randint

#指定分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

#初始化pygame模块
pygame.init()

#游戏界面宽高
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#设置游戏界面的标题
pygame.display.set_caption('Python飞机大战')

#加载一个图片
surface_img = pygame.image.load('./resources/image/background.png')
# surface_img = pygame.image.load('3.jpg')

#加载大杂烩
many_surface = pygame.image.load('./resources/image/shoot.png')

#加载gameover
gameover_surface = pygame.image.load('./resources/image/gameover.png')

#创建一个矩形区域 用来剪切我方飞机
hero_rect = pygame.Rect(0,99,102,126)
hero_surface = many_surface.subsurface(hero_rect)

#剪切我方飞机另外一个状态界面
hero_rect1 = pygame.Rect(165, 360,102,126)
hero_surface1 = many_surface.subsurface(hero_rect1)

#裁剪子弹矩形区域
bullet_rect = pygame.Rect(1004, 987,9,21)
bullet_surface = many_surface.subsurface(bullet_rect)

#裁剪敌机矩形区域
enemy_rect = pygame.Rect(534, 612,57, 43)
enemy_surface = many_surface.subsurface(enemy_rect)

#hero 初始位置
hero_position = [SCREEN_WIDTH // 2 - hero_rect.width // 2, SCREEN_HEIGHT - hero_rect.height - SCREEN_HEIGHT // 10]

#游戏结束按钮
game_over_font = pygame.font.SysFont(None,70)
game_over_surface = game_over_font.render('Reset',1,(0,255,0))

#给界面填充一个背景色
# background = pygame.Surface((500,800))
# background.fill((255,0,0))
# screen.blit(background,[0,0])

#从这个地方开始把我们的主函数封装起来 游戏入口函数
def main():

    # 设置偏移方向
    offset_x = offset_y = 0
    #英雄移动的速度
    # HERO_SPEED = 6
    ticks = 0

    hero = Hero(hero_surface, hero_position)

    #声明一个精灵组 用来存放子弹
    bullet_group = pygame.sprite.Group()
    #声明一个精灵组 用来存放敌机
    enemy_group = pygame.sprite.Group()
    #声明一个精灵组 用来存放销毁的敌机
    enemy_down_group = pygame.sprite.Group()

    #分数初始化
    score = 0

    #一般的游戏逻辑里都会有while True
    while True:

        # 绘制背景
        screen.blit(surface_img, [0, 0])

        # 绘制我方 考虑到切换状态 把频率降低
        if ticks % 40 < 20:
            # 实例化英雄
            hero = Hero(hero_surface, hero.rect)
        else:
            hero = Hero(hero_surface1, hero.rect)
        screen.blit(hero.image, hero.rect)
        ticks += 1

        # 绘制子弹
        if ticks % 15 == 0:
            bullet = Bullet(bullet_surface, [hero.rect.x+hero.rect.width//2,hero.rect.y])
            bullet_group.add(bullet)

        bullet_group.update()
        bullet_group.draw(screen)

        #绘制敌机
        if ticks % 70 == 0:
            enemy_position = [randint(0,SCREEN_WIDTH - enemy_rect.width),-enemy_rect.height]
            enemy = Enemy(enemy_surface, enemy_position)
            enemy_group.add(enemy)

        enemy_group.update()
        enemy_group.draw(screen)

        # #子弹和敌机碰撞检测
        # enemy_down_group.add(pygame.sprite.groupcollide(enemy_group,bullet_group,True,True))
        # #如果考虑敌机爆炸的效果
        # for enemy_down in enemy_down_group:
        #     pass
        #     #动态切换图片 动态改变图片的索引 用计数器来让效果慢下来


        enemy_down_res = pygame.sprite.groupcollide(enemy_group,bullet_group,True,True)
        #如果有碰撞 分值加1
        if len(enemy_down_res) > 0:
            score += 1

        #我方和敌机碰撞检测
        hero_down_res = pygame.sprite.spritecollide(hero,enemy_group,True)
        if len(hero_down_res) > 0:
            #游戏结束
            break

        # print(enemy_down_group)

        #记录分数
        score_font = pygame.font.SysFont(None,40)
        score_surface = score_font.render('Score:'+str(score),1,(128,128,128))
        screen.blit(score_surface, [10,10])

        #获取pygame触发的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #获取键盘事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    offset_x = -1
                if event.key == pygame.K_d  or event.key == pygame.K_RIGHT:
                    offset_x = 1
                if event.key == pygame.K_w  or event.key == pygame.K_UP:
                    offset_y = -1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    offset_y = 1
            if event.type == pygame.KEYUP:
                    offset_x = offset_y = 0


        hero.move(offset_x,offset_y)
        pygame.display.update()

    # 如果代码能走到这一步 表示gameover
    screen.blit(gameover_surface, [0, 0])

    # 重新开始
    screen.blit(game_over_surface, [SCREEN_WIDTH / 2 - game_over_surface.get_width() / 2,
                                    SCREEN_HEIGHT / 2 - game_over_surface.get_height() / 2 + 50])
    pygame.display.update()