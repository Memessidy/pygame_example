import pygame
from gun import Gun
import controls
from pygame.sprite import Group
import settings
from stats import Stats


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

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, ufos, bullets)
        controls.update_bullets(screen, ufos, bullets)
        controls.update_ufos(stats, screen, gun, ufos, bullets)


run()

# TODO: Пушка должна стрелять нажатием
