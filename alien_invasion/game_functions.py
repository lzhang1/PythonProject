# -*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
from rain import Rain
import random
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_SPACE:
        new_bullet = fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets, rains):
    screen.blit(ai_settings.bg_image,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    rains.draw(screen)
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(ai_settings, screen, aliens, ship, bullets):
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.x >= screen_rect.right:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) < 13:
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_y(ai_settings, alien_height):
    available_space_y = ai_settings.screen_height - 2*alien_height
    number_aliens_y = int(available_space_y/(2*alien_height))
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_height= alien.rect.height
    alien.y = alien_height + 2*alien_height*alien_number
    alien.rect.y = alien.y
    alien.x = ai_settings.screen_width + (alien.rect.width + 2 * alien.rect.width * row_number)
    alien.rect.x = alien.x
    aliens.add(alien)

def get_number_rows(ai_settings, ship_width, alien_width):
    available_space_x = (ai_settings.screen_width - (2 * alien_width) - ship_width)
    number_rows = int(available_space_x/(2*alien_width))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_y = get_number_aliens_y(ai_settings, alien.rect.height)
    number_rows = get_number_rows(ai_settings, ship.rect.width, alien.rect.width)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_y):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_drop_speed *= -1

def update_aliens(ai_settings, screen, aliens, ship, stats, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    screen_rect = screen.get_rect()
    for alien in aliens.copy():
        if alien.rect.x < 0:
            aliens.remove(alien)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def update_rains(ai_settings, rains, screen):
    rains.update()
    screen_rect = screen.get_rect()
    for rain in rains.copy():
        if rain.rect.y >= screen_rect.height:
            rains.remove(rain)
            create_raindrop(ai_settings, screen, rains)


def create_rains(ai_settings, screen, rains, type):
    numbers = ai_settings.rain_type[type]
    for rainnum in range(numbers):
        create_raindrop(ai_settings, screen, rains)

def create_raindrop(ai_settings, screen, rains):
    rain = Rain(ai_settings, screen)
    rain.y = -random.randint(1,600)
    rain.rect.y = rain.y
    rain.x = random.randint(5, int(600))
    rain.rect.x = rain.x
    rains.add(rain)

def update_ship(ai_settings, ship, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        print ("Ship hit!!!")
        sys.exit()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        sleep(0.5)
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)
    else:
        stats.game_active = False