##Contains starting variables and cross-module Functions


import pygame,time
#Intializing Pygame
pygame.init()

# Setting Display size,Caption,Logo,background,width and height
Display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Earth Defender")
background = pygame.image.load("models/nasa-53884-unsplash.jpg").convert()
pygame.display.set_icon(pygame.image.load("models/Enemy.png").convert_alpha())
clock = pygame.time.Clock()
displayinfo = pygame.display.Info()
width = displayinfo.current_w
height = displayinfo.current_h
#Defining Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#this Function is used to display text on screen
def display_text(text,size,font,x,y,color = WHITE,aa = True,backgroundtextcolor= None,return_rect =0):
    fontsdict = {1:"Inkfree.ttf",2 :"ARLRDBD.TTF",3:"BRUSHSCI.TTF"}
    message = pygame.font.Font(fontsdict[font],size)
    message_surface = message.render(text,aa,color,backgroundtextcolor)
    rect = message_surface.get_rect()
    rect.center = (x,y)
    Display.blit(message_surface,rect)
    if return_rect == 1:
        return rect
