import pygame
import constants as c

class UsernameBox(pygame.sprite.Sprite):

    def __init__(self, message):
        super(UsernameBox, self).__init__()
        self.font = pygame.font.Font(None, 50) #set font to default Pygame font
        self.color = (255, 255, 255)
        self.width = 350
        self.height = 100
        self.size = (self.width, self.height)
        self.status = True
        #create surface for username text display
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0,110,0))
        self.message = message

        self.image_text = self.font.render(self.message, True, self.color) #render font into an image for display
        self.image.blit(self.image_text, self.image_text.get_rect(center = self.image.get_rect().center))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2 - self.rect.width // 2 #put message into center
        self.rect.y = c.DISPLAY_HEIGHT // 2 + 100 - self.rect.height // 2  # put message into center
        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if not self.status:
            self.kill()
