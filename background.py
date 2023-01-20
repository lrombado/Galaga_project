#This file handles the entire background, to include random star generation
import pygame
import constants as c
from star import Star
import random

class BG(pygame.sprite.Sprite): #inherit from Sprite object from pygame
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE) #create image for the entire screen size
        self.color = (0, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group() #create Sprite group of stars
        self.timer = random.randrange(1, 10)


    def update(self):
        self.stars.update() #we call the stars update function here
        for star in self.stars:
            if star.rect.y >= c.DISPLAY_HEIGHT:
                self.stars.remove(star)
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star) #add new star to group
            self.timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1