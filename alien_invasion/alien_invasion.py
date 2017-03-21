# -*- coding:utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from rain import Rain
from gamestats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    rains = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    type = ['tiny','medium','large']
    gf.create_rains(ai_settings, screen, rains, type[1])
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_rains(ai_settings, rains, screen)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, rains)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets)
            gf.update_aliens(ai_settings, screen, aliens, ship, stats, bullets)
        gf.update_ship(ai_settings, ship, aliens)


run_game()


