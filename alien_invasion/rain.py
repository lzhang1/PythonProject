# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, ai_settings, screen):
        super(Rain, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/rain.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.speed_factor = self.ai_settings.rain_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y