import pygame
from gun import Gun
import controls
from pygame.sprite import Group
import settings
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((settings.display_width, settings.display_height))
    pygame.display.set_caption("Space invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ufos = Group()
    controls.create_army(screen, ufos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, ufos, bullets)
            controls.update_bullets(screen, stats, sc, ufos, bullets)
            controls.update_ufos(stats, screen, gun, ufos, bullets)


run()
