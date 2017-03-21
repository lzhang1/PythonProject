# -*- coding:utf-8 -*-
import pygame
class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_image = pygame.image.load('images/space.jpg')
        self.bullet_speed_factor = 16
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 255,0,0
        self.bullets_allowed = 10
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.rain_speed_factor = 3
        self.rain_type = {'tiny':10, 'medium':20, 'large':30}

        self.ship_speed_factor = 8
        self.ship_limit = 3