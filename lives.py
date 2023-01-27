import pygame
import constants as c

class Lives(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()
        self.num_lives = num_lives
        self.width = 100
        self.height = 80
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0,0,0))
        self.ship_image = pygame.image.load("ship.png").convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (self.ship_image.get_width() * .08, self.ship_image.get_height() * .08))
        #blit is used to place an image to a specific coordinate on a specified surface (here its self.image)

        self.image.blit(self.ship_image, (5,5)) #place ship icon onto surface
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)
        self.font_color = (255, 255, 255)
        self.lives_counter = self.font.render(f'x{self.num_lives}', False, self.font_color, False)
        #Place the lives counter in the specified font onto the image
        self.image.blit(self.lives_counter, (45,15))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def decrement_life(self):
        #Each time life is decremented, the "x lives" image must be re-rendered on screen
        self.num_lives -= 1
        #Prevent from going to negative lives
        if self.num_lives < 0:
            self.num_lives = 0
        else:
            self.image = pygame.Surface(self.size)
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.ship_image, (5, 5))  # place ship icon onto surface
            self.lives_counter = self.font.render(f'x{self.num_lives}', False, self.font_color, False)
            # Place the lives counter in the specified font onto the image
            self.image.blit(self.lives_counter, (45, 15))