import pygame
import constants as c


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(HealthBar, self).__init__()
        self.max_hp = hp #receive initial value
        print(self.max_hp)
        self.hp = self.max_hp #assign current to max at beginning
        self.original_image = pygame.image.load('health_bar.png').convert() #load in health bar image
        self.original_image = pygame.transform.scale(self.original_image, (100, 30)) #resize to screen fitting size
        self.image = self.original_image
        print("image width: " + str(self.image.get_width()))
        self.max_width = self.image.get_width() #max health bar width (at full health)
        print("max width: "+ str(self.max_width))

        #self.image = pygame.transform.scale(self.image, (100, 30))
        self.rect = self.image.get_rect()
        #self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def decrease_hp_val(self):
        self.hp -= 1
        print("dec hp val")
        print(self.hp)

        self.image = pygame.transform.scale(self.image, (self.max_width * self.hp // self.max_hp, self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y