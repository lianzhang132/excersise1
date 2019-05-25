import pygame.time
from  Mou import Hero
from  Bou import Bullet
from  Ene import Enemy
from  random import randint
import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "1400,150"

SCREEN_WIDEH = 480
SCREEN_HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDEH,SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")
surface_img = pygame.image.load("E:\\feiji\\resources\image\\background.png")
many_surface = pygame.image.load("E:\\feiji\\resources\image\\shoot.png")
gameover_surface = pygame.image.load("E:\\feiji\\resources\image\\gameover.png")

hero_rect = pygame.Rect(0,99,102,126)
hero_surface = many_surface.subsurface(hero_rect)

hero_rect1 = pygame.Rect(165,360,102,126)
hero_surface1 = many_surface.subsurface(hero_rect1)

hero_position = [SCREEN_WIDEH//2-hero_rect.width//2,SCREEN_HEIGHT - hero_rect.height - SCREEN_HEIGHT//10]

bou_rect = pygame.Rect(1004, 987,9,21)
bou_surface = many_surface.subsurface(bou_rect)

enemy_rect = pygame.Rect(534, 612,57, 43)
enemy_surface = many_surface.subsurface(enemy_rect)


enemy1_down1_surface = many_surface.subsurface(pygame.Rect(267, 347,57, 51))
enemy1_down2_surface = many_surface.subsurface(pygame.Rect(873, 697,57, 51))
enemy1_down3_surface = many_surface.subsurface(pygame.Rect(267, 296,57, 51))
enemy1_down4_surface = many_surface.subsurface(pygame.Rect(930, 697,57, 51))

enemy1_down_surface = [enemy1_down1_surface,enemy1_down2_surface,enemy1_down3_surface,enemy1_down4_surface]

game_res_font = pygame.font.Font("E:\练习\python\\feiji\\resources\\font\simhei.ttf",70)
game_res_surface = game_res_font.render("再来一次",1,(100,255,0))
birth_sai_font = pygame.font.Font("E:\练习\python\\feiji\\resources\\font\simhei.ttf",30)
birth_sai = birth_sai_font.render("小的提前祝老婆生日快乐",1,(100,255,0))


# print(hero_position)
bou1let_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_down_group = pygame.sprite.Group()


def main():

    offset_x = offset_y = 0
    ticks = 0
    score = 0
    hero = Hero(hero_surface, hero_position)
    while 1:
        screen.blit(surface_img,[0,0])
        if ticks&50 < 25:
            hero = Hero(hero_surface,hero.rect)
        else:
            hero = Hero(hero_surface1,hero.rect)
        screen.blit(hero.image,hero.rect)

        if ticks %15 ==0:
            bou1let = Bullet(bou_surface,[hero.rect.x+hero.rect.width//2,hero.rect.y])
            bou1let_group.add(bou1let)
        bou1let_group.update()
        bou1let_group.draw(screen)

        if ticks %50 ==0:
            enemy_position =[randint(0,SCREEN_WIDEH-enemy_rect.width),-enemy_rect.height]
            enemy = Enemy(enemy_surface,enemy_position)
            enemy_group.add(enemy)
        enemy_group.update()
        enemy_group.draw(screen)

        enemy_down_group.add(pygame.sprite.groupcollide(enemy_group,bou1let_group,True,True))
        for enemy_down in enemy_down_group:
            screen.blit(enemy1_down_surface[enemy_down.down_index],enemy_down.rect)
            if ticks%10 ==0:
                enemy_down.down_index+=1
                if enemy_down.down_index >= 3:
                    enemy_down_group.remove(enemy_down)
                    score += 1

        hero_down_res = pygame.sprite.spritecollide(hero,enemy_group,True)
        if  len(hero_down_res) > 0:
            break
        ticks += 1

        score_font = pygame.font.Font("E:\练习\python\\feiji\\resources\\font\simhei.ttf",30)
        score_surface = score_font.render("得分是:"+str(score),1,(50,255,10))
        screen.blit(score_surface,[20,20])




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    offset_x = -1
                if event.key == pygame.K_d or  event.key == pygame.K_RIGHT:
                    offset_x = 1
                if event.key ==  pygame.K_w or  event.key == pygame.K_UP:
                    offset_y = -1
                if event.key ==  pygame.K_s or  event.key == pygame.K_DOWN:
                    offset_y = 1
            if event.type == pygame.KEYUP:
                offset_x = offset_y = 0
        hero.move(offset_x,offset_y)
        pygame.display.update()

    screen.blit(gameover_surface,[0,0])

    screen.blit(game_res_surface,[SCREEN_WIDEH/2 -game_res_surface.get_width()/2,
                                  SCREEN_HEIGHT/2-game_res_surface.get_height()/2 +50])
    screen.blit(birth_sai,[SCREEN_WIDEH/2 -game_res_surface.get_width()/2,
                                  SCREEN_HEIGHT/2-game_res_surface.get_height()/2])
    pygame.display.update()


















