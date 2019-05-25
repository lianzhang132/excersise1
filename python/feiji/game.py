from main import *
import pygame.time
from  pygame.locals import *
import pygame.mixer
# music1 = pygame.mixer.music.load("music.mp3")
# pygame.mixer.music.play()

main()

# pygame.mixer_music.queue("music.mp3")


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= SCREEN_WIDEH/2 - game_res_surface.get_width()/2 and pos[0]<= SCREEN_WIDEH/2 + game_res_surface.get_width()/2:
                if pos[1] >=SCREEN_HEIGHT/2 - game_res_surface.get_height()/2 and pos[1]<= SCREEN_HEIGHT/2 + game_res_surface.get_height()/2 +50:
                    main()
