import pygame
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner
from alert_box import AlertBox
from username import UsernameBox
#pygame.mixer.pre_init() #initialize sound functionality
#pygame.init()
pygame.mixer.init()
pygame.font.init()

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
alert_box_group = pygame.sprite.Group()
username_box_group = pygame.sprite.Group()


#Music setup
pygame.mixer.music.load('main_song.ogg')
pygame.mixer.music.set_volume(.1)
#pygame.mixer.music.play(loops=True)

intro = True
running = True
input_active = True
# Prompt user to enter name
alert_box = AlertBox("Enter your name username: ")
alert_box_group.add(alert_box)
user_text = ''
while intro:
    input_active = True
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            user_text = ''
        elif event.type == pygame.KEYDOWN and input_active: #conditions for if a key is pressed
            if event.key == pygame.K_RETURN:
                input_active = False
                intro = False
            elif event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
            #Display while username types their name
            username_box = UsernameBox(user_text)
            username_box_group.add(username_box)
    # Update all the objects
    bg_group.update()
    sprite_group.update()
    alert_box_group.update()
    username_box_group.update()

    #Display objects on intro screen
    display.fill(black)
    bg_group.draw(display)
    particle_spawner.particle_group.draw(display)
    alert_box_group.draw(display)
    username_box_group.draw(display)
    pygame.display.update()
    if not intro:
        alert_box_group.remove(alert_box)

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
    #Check for game over
    if not player.is_alive:
        enemy_spawner.clear_enemies()
        alert_box = AlertBox("GAME OVER")
        alert_box_group.add(alert_box)


    #Update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    particle_spawner.update()
    alert_box_group.update()

    #Check for collision between enemy and bullets
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        #Pass in the enemy's point value to update score
        player.hud.score.update_score(enemy[0].point_value)
        particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))

    #Check for collision between ship and enemy
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not player.is_invincible:
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
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)
    alert_box_group.draw(display)
    pygame.display.update()