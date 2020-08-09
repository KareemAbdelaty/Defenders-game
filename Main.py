
#Importing Modules
import pygame,time,Menues,Levels
from Initialize import *



#variable cotrolling game state
_state = 'main menu'


#This function runs intro
def intro():
    Display.blit(background,(0,0))
    display_text('Welcome Defender',100,2,width/2,height/2)
    pygame.display.update()
    time.sleep(3)
            
            
        
def game():
    global _state
    stop = False
    while not stop:
        if _state == 'main menu':
            _state = Menues.main_menu()
        elif _state == 'play':
            _state = Levels.play('l','d')
        elif _state == 'highscores':
##            _state = Menues.highscores()
            pass
        elif  _state == 'quit':
            pygame.quit()
            quit()
        elif _state == 'settings':
##            _state = Menues.settings()
            pass
if __name__ == '__main__':                    
    ## Functions Call
    intro()
    game()


   
