import pygame
import constants as c
from health_bar import HealthBar

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load('hud.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (500, 60))
        self.rect = self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar()
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 10
        self.health_bar_group  = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)

    def update(self):
        self.health_bar_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
