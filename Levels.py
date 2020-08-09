#play and levels
import pygame,Player,Enemy
from Initialize import *

def play(level,difficulty):
    playmenu = True
    le =level
    de = difficulty
    #while playmenu:
    Display.blit(background,(0,0))
    player_character = Player.Player()
    Enemies = [Enemy.Enemy()for i in range(3)]
    Display.blit(player_character.image,(width/2,height*3/5))
    Display.blit(Enemies[0].get_image(),(width/2,height*1/5))
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            playmenu = False
            return 'quit'
    pygame.display.update()
    time.sleep(3)
    return 'main menu'
        #clock.tick(60)

