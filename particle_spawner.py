import pygame
from particle import Particle
import random

class ParticleSpawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()

    def spawn_particles(self, position):
        random_number = random.randrange(3,7)
        for num_particles in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = position[0]
            new_particle.rect.y = position[1]

            self.particle_group.add(new_particle)