import pygame
import Projectile
class Player():
    def __init__(self,picture='models/player.png.png',health=3,lvl=1,ammo= 10):
        self.__health_points = health
        self.__attack_level = lvl
        self.image = pygame.image.load(picture).convert()
        self.__inventory = [ammo,Projectile.Projectile()]
        
    def damage(self,i=1):
        self.__health_points = self.__health_points - i
    def heal(self,i=1):
        self.__health_points = self.__health_points + i
    def attack(self,i=1):
        self.__ammuntion = self.__ammuntion - i
    def restock(self,i=5):
        self.__ammuntion = self.__ammuntion + i
        
