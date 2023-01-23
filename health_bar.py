import pygame
import constants as c


class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar, self).__init__()
        self.image = pygame.image.load('health_bar.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 30))
        self.rect = self.image.get_rect()
        #self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y