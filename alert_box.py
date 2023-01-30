import pygame
import constants as c

class AlertBox(pygame.sprite.Sprite):
    def __init__(self, message):
        super(AlertBox, self).__init__()
        self.font = pygame.font.Font(None, 50) #set font to default Pygame font
        self.color = (255, 0, 0)
        self.message = message

        self.image = self.font.render(self.message, 0, self.color) #render font into an image for display
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2 - self.rect.width // 2 #put message into center
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2  # put message into center
        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

