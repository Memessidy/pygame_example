import pygame
from settings import gun_speed


class Gun:

    def __init__(self, screen):
        """Инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load('images/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.step = gun_speed

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.step

        if self.mleft and self.rect.left > 0:
            self.center -= self.step

        self.rect.centerx = self.center