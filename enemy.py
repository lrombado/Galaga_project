import random
import pygame
import constants as c

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()  //50, self.image.get_height() //50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height #spawns just above screen display
        self.snd_explode = pygame.mixer.Sound('enemy_explode.ogg')
        self.point_value = 5
        self.hp = 3
        self.vel_x = 0
        self.vel_y = random.randrange(3,5) #pixels per frame

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()


    def destroy(self):
        #self.snd_explode.play()

        self.kill()
