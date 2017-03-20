# -*- coding:utf-8 -*-
import pygame
class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        #self.bg_color = (230,230,230)
        self.bg_image = pygame.image.load('images/space.jpg')
        self.ship_speed_factor = 8
        self.bullet_speed_factor = 16
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,0,0
        self.bullets_allowed = 10