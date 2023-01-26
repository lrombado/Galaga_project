import pygame
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner

#pygame.mixer.pre_init() #initialize sound functionality
#pygame.init()
pygame.mixer.init()


#Display setup
display = pygame.display.set_mode((c.DISPLAY_SIZE))
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

#Object setup
bg = BG()
player = Ship() #create Ship object

# We want to keep the background sprite group and other sprite groups separate (per pygame documentation)
bg_group = pygame.sprite.Group()
bg_group.add(bg)
#Create sprite group to control/update all sprites at once instead of individually
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()



#Music setup
pygame.mixer.music.load('main_song.ogg')
pygame.mixer.music.set_volume(.1)
#pygame.mixer.music.play(loops=True)


running = True
while running:
    #Tick clock
    clock.tick(fps)
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN: #conditions for if a key is pressed
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP: #conditions for if a key is released
            if event.key == pygame.K_a:
                player.vel_x = 0
            elif event.key == pygame.K_d:
                player.vel_x = 0

    #Update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    particle_spawner.update()

    #Check for collision

    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        enemy[0].hp = 0
        enemy[0].get_hit()
        player.get_hit()


    #Render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display) #draw hud to the screen
    player.hud.health_bar_group.draw(display) #draw health_bar on top of the screen
    pygame.display.update()