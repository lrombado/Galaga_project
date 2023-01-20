import random
import pygame
from enemy import Enemy
import constants as c

class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120) #.5 secs and 2 secs

    def update(self):
        self.enemy_group.update()
        for enemy in self.enemy_group:
            if enemy.rect.y >= c.DISPLAY_HEIGHT:
            #if enemy.rect.y <= 0:
                self.enemy_group.remove(enemy)
        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(30,120)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
        new_enemy = Enemy()
        self.enemy_group.add(new_enemy)