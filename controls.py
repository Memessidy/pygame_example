import pygame
import sys
from bullet import Bullet
from ufo import Ufo
import settings


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, ufos, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.output()
    ufos.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Обновлене позиций пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_ufos(ufos):
    """Обновляет позицию пришельцев"""
    ufos.update()

def create_army(screen, ufos):
    """создание армии пришельцев"""
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    ufo_count = int((settings.display_width - 2 * ufo_width) / ufo_width)
    ufo_height = ufo.rect.height
    ufo_count_y = int((settings.display_height - 100 - 2 * ufo_height) / ufo_height)
    ufo_count_y -= 3

    for row_index in range(ufo_count_y):
        for index in range(ufo_count):
            ufo = Ufo(screen)
            ufo.x = ufo_width + ufo_width * index
            ufo.y = ufo_height + ufo_height * row_index
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.rect.height + ufo.rect.height * row_index
            ufos.add(ufo)
