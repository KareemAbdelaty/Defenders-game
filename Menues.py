#all menues are here
import pygame
from Initialize import *
def main_menu():
        mainmenu = True
        while mainmenu:
            Display.blit(background,(0,0))
            play_rect = display_text('Play',72,1,width/2,height*1/5,return_rect = 1)
            highscores_rect = display_text('Highscores',72,1,width/2,height*2/4,return_rect = 1)
            exit_rect = display_text('exit',72,1,width/2,height*3/4,return_rect = 1)

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    mainmenu = False
                    return 'quit'
                elif event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(mouse_pos):
                    mainmenu = False
                    return 'play'
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and highscores_rect.collidepoint(mouse_pos):
                    return 'highscores'
                elif event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(mouse_pos):
                    return 'quit'
            pygame.display.update()
            clock.tick(60)

##def settings(setting_level = 0):
##    if setting_level = 0:
##        pass
##
##def highscores():
##    pass
