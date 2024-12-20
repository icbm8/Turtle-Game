import pygame
import random
import time
import pygame.transform
from player import Player
from food import Food
from plastic_enemies import Enemy
#######################
start_time = time.time()
facts_for_game = [
    "At least 1,000 sea turtles die each year due to plastic — thats more than 1 turtle every 9 hours!",
    "By 2050, there will be more plastic than fish in the ocean!",
    "More than 100,000 marine animals die each year due to plastic."
    ]
###########################
pygame.init()
score = 0
health = 100
score = 0
game_width = 1000
game_height = 650
game_start = False
screen = pygame.display.set_mode((game_width, game_height))
running = True
fade_image = pygame.image.load("./assets/fade.png")
screen.blit(fade_image,(0,0))
backgroundimage = pygame.image.load("./assets/background.jpg")
screen.blit(backgroundimage,(0,0))
inimi_2_remove = []
clock = pygame.time.Clock()
player = Player(screen,450)
enemylist = []
foodlist = []
enemy_timer_max = 25
enemy_timer = enemy_timer_max
menu_show = True
fact_on_menu = str(random.choice(facts_for_game))
##########################
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    mouse_x,mouse_y = pygame.mouse.get_pos()       
    keys = pygame.key.get_pressed()
########################
    if keys[pygame.K_w]:
        player.Move(0,-1)
    if keys[pygame.K_s]:
        player.Move(0,1)
    if keys[pygame.K_a]:
        player.Move(-1,0)
    if keys[pygame.K_d]:
        player.Move(1,0)
    if keys[pygame.K_SPACE]:
        print("pause game")
#########################
    elapsed_time = time.time() - start_time
    screen.blit(backgroundimage,(0,0))
    font = pygame.font.SysFont("timesnewroman", 45)
    font.set_bold(True)
    if menu_show:
        play_button = pygame.image.load("./assets/play.png")
        play_button = pygame.transform.scale(play_button,(400,200))
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 200,200
        screen.blit(play_button,(200,100))
        settings_button = pygame.image.load("./assets/settings.png")
        settings_button = pygame.transform.scale(settings_button,(200,200))
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 400,200
        screen.blit(settings_button,(600,100))
        text = font.render("Welcome to Save The Turtles", True, (0, 0, 0))
        screen.blit(text, (200,0))
        font = pygame.font.SysFont("timesnewroman", 40)
        text = font.render("GaSTc Project by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (275,50))
        font = pygame.font.SysFont("timesnewroman", 35)
        font.set_bold(True)
        text = font.render("Real Facts:", True, (0, 0, 0))
        screen.blit(text, (400, 325))
        font.set_bold(False)
        font = pygame.font.SysFont("timesnewroman", 20)
        text = font.render(str(fact_on_menu), True, (0, 0, 0))
        screen.blit(text, (200, 375))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_hitbox.collidepoint(event.pos):
            game_start = True
            menu_show = False
#############################
    backgroundimage = pygame.transform.scale(backgroundimage,(1101,667))
    if game_start:
        font = pygame.font.SysFont("timesnewroman", 25)
        font.set_bold(True)
        text = font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (15, 15))
        for food in foodlist:
            if player.rect.colliderect(food.hitbox):
                food.isvisible=False
                score+=1
                if score % 5 == 0:
                    player.size += 50
                    player.image = pygame.image.load("./assets/playerturtle.png")
                    player.image = pygame.transform.scale(player.image,(int(player.size*0.15),int(player.size*0.125)))
                    player.rect = player.image.get_rect()
            food.update(screen, foodlist)
        font.set_bold(False)
        text = font.render("Score: " + str(score), True, (0, 0, 0))    
        screen.blit(text, (15, 40))
        text = font.render("Time Played: " + str(round(elapsed_time)) + " seconds", True, (0, 0, 0))
        screen.blit(text, (15, 65))
        text = font.render("Health: " + str(health), True, (0, 0, 0))
        screen.blit(text, (15,90))
        player.update()
        Enemy.createenemy(enemylist, screen)
        Food.createfood(foodlist, screen)
        for enemy in enemylist:
            if player.rect.colliderect(enemy.hitbox):
                enemy.isvisible=False
                health-=10
            enemy.update(screen, enemylist)
    font = pygame.font.SysFont("timesnewroman", 15)
    font.set_bold(True)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text, (0,0))
    pygame.display.flip()
    clock.tick(50) 
    pygame.display.set_caption("Save the Turtles")
#######################