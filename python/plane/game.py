from main import *
import pygame.time
from pygame.locals import *

#游戏开始
main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= SCREEN_WIDTH/2 - game_over_surface.get_width()/2 and pos[0] <= SCREEN_WIDTH/2 + game_over_surface.get_width()/2:
                if pos[1] >= SCREEN_HEIGHT/2 - game_over_surface.get_height()/2 and pos[1] <= SCREEN_HEIGHT/2 + game_over_surface.get_height()/2 + 50:
                    #继续游戏
                    main()
