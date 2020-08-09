import pygame
class Enemy():
    def __init__(self,level =1,x=100,y=100, health=1,strength=1):
        model = {1:'models/Transparent/Enemy (1).png',2:'models/Transparent/Enemy (2).png',3:'models/Transparent/Enemy (3).png',4:'models/Transparent/Enemy (4).png',5:'models/Transparent/Enemy (5).png',
                 6:'models/Transparent/Enemy (6).png',7:'models/Transparent/Enemy (7).png',8:'models/Transparent/Enemy (8).png'}
        self.__image = pygame.image.load(model[level]).convert()
        self.__health_points = health
        self.__attack_power = strength
        self.__coordinates = (x,y)
        self.__projectiles = []
    def attack():
        pass
    def move():
        pass
    def get_image(self):
        return self.__image
    
        
        
