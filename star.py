import pygame
import constants as c
import random

class Star(pygame.sprite.Sprite): #inherit from Sprite object from pygame
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = random.randrange(1, 4)
        self.size = (self.width, self.height)
        # Things that show up on screen are called surfaces
        self.image = pygame.Surface(self.size)
        self.color = (255, 255, 255)
        self.image.fill(self.color) #color the stars white
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH) #addign random x coordinate to new stars
        self.vel_x = 0
        self.vel_y = random.randrange(4, 25) #pixels per frame speed

    def update(self):
        #These lines update the rect coordinates of the object each frame by += the velocities
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y