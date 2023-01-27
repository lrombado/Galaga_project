import pygame
import constants as c

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.font_size = 25
        self.x_pad = 20
        self.y_pad = 40
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size) #create pygame font object
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color, None) #generate the font image
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - self.y_pad

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        #We need to recreate a new score image each time the score value is updated.
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color, None)  # generate the font image
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - self.y_pad
