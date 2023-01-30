import pygame
import constants as c
from bullet import Bullet
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__() #to initalize Sprite module as well
        self.image = pygame.image.load('ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() *.1, self.image.get_height()*.1))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 #sets starting x location
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height*2.5 #sets starting y location
        self.bullets = pygame.sprite.Group() #create bullet sprite group
        self.snd_shoot = pygame.mixer.Sound('snd_bullet.ogg')
        self.lives = 2
        self.max_hp = 3


        self.hp = self.max_hp
        self.hud = HUD(self.hp, self.lives) #player gets their own HUD, receives ship's hp value
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.is_invincible = False
        self.max_invincible_timer = 100
        self.invincible_timer = 0
        self.is_alive = True


        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

    def update(self): #to update the position of the ship
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0: #if above top of display screen
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        #restrict left and right boundaries of screen
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y

        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        else:
            self.is_invincible = False



    def shoot(self):
        #self.snd_shoot.play()
        if self.is_alive:
            new_bullet = Bullet()
            #New bullet location should be location of the ship
            new_bullet.rect.x = self.rect.x + (self.rect.width // 2 - 2 ) #offset bullet start location to center of ship
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet) #add new bullet to bullets sprite group

    def get_hit(self):
        if self.is_alive:
            self.hp -=1
            self.hud.health_bar.decrease_hp_val()

            if self.hp <= 0:
                self.hp = 0
                self.death()


    def death(self):
        self.lives -= 1
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0,0)) #set ship image to invisible surface
        self.hp = self.max_hp #reset hp
        self.hud.health_bar.reset_health_to_max()
        #decrease lives count
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH // 2 #sets starting x location
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer
