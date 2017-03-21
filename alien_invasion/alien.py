# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.speed_factor = self.ai_settings.alien_speed_factor
        self.fleet_direction = self.ai_settings.fleet_direction

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.height >= screen_rect.height:
            return True
        elif self.rect.height <= 0:
            return True

    def update(self):
        self.x -= self.speed_factor * self.fleet_direction
        self.rect.x = self.x