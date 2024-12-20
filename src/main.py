#imports
import pygame
import random
import time
import pygame.transform
from player import Player
from food import Food
from plastic_enemies import Enemy

#starts time and adds facts
start_time = time.time()
facts_for_game = [
    "At least 1,000 sea turtles die each year due to plastic — thats more than 1 turtle every 9 hours!",
    "By 2050, there will be more plastic than fish in the ocean!",
    "More than 100,000 marine animals die each year due to plastic."
    ]

#initialization and variable defining, also shows image and fade, etc.
pygame.init()
score = 0
health = 100
score = 0
game_width = 1000
game_height = 650
game_start = False
settings_show = False
difficulty = "Normal"
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

#while loop land below
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    mouse_x,mouse_y = pygame.mouse.get_pos()       
    keys = pygame.key.get_pressed()

#keys
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

#screen blitting the menu
    elapsed_time = time.time() - start_time
    screen.blit(backgroundimage,(0,0))
    font = pygame.font.SysFont("timesnewroman", 45)
    font.set_bold(True)
    if menu_show:
        play_button = pygame.image.load("./assets/play.png")
        play_button = pygame.transform.scale(play_button,(400,200))
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 200,125
        pygame.draw.rect(screen, (255,0,0), play_button_hitbox, 2)
        screen.blit(play_button,(200,125))
        settings_button = pygame.image.load("./assets/settings.png")
        settings_button = pygame.transform.scale(settings_button,(200,200))
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 600,125
        pygame.draw.rect(screen, (255,0,0), settings_button_hitbox, 2)
        screen.blit(settings_button,(600,125))
        text = font.render("Welcome to Save The Turtles", True, (0, 0, 0))
        screen.blit(text, (200,0))
        font = pygame.font.SysFont("timesnewroman", 40)
        text = font.render("GaSTc Project by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (275,50))
        font = pygame.font.SysFont("timesnewroman", 35)
        font.set_bold(True)
        text = font.render("Real Facts:", True, (0, 0, 0))
        screen.blit(text, (25, 350))
        font.set_bold(False)
        font = pygame.font.SysFont("timesnewroman", 20)
        text = font.render(str(fact_on_menu), True, (0, 0, 0))
        screen.blit(text, (225, 362.5))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_hitbox and play_button_hitbox.collidepoint(event.pos):
                game_start = True
                menu_show = False
                play_button_hitbox = None  # Delete the hitbox after click
            
            if settings_button_hitbox and settings_button_hitbox.collidepoint(event.pos):
                settings_show = True
                menu_show = False
                settings_button_hitbox = None

#playing and showing the game
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
    if settings_show:
        font = pygame.font.SysFont("timesnewroman", 25)
        font.set_bold(True)
        text = font.render("Difficulty", True, (0, 0, 0))
        screen.blit(text, (265, 60))
        easy_button = pygame.image.load("./assets/easy.png")
        easy_button = pygame.transform.scale(easy_button,(150,100))
        easy_button_hitbox = easy_button.get_rect()
        easy_button_hitbox.topleft = (50,100)
        pygame.draw.rect(screen, (255,0,0), easy_button_hitbox, 2)
        screen.blit(easy_button,(50,100))
        medium_button = pygame.image.load("./assets/medium.png")
        medium_button = pygame.transform.scale(medium_button,(150,100))
        medium_button_hitbox = medium_button.get_rect()
        medium_button_hitbox.topleft = (50,100)
        pygame.draw.rect(screen, (255,0,0), medium_button_hitbox, 2)
        screen.blit(medium_button,(250,100))
        hard_button = pygame.image.load("./assets/hard.png")
        hard_button = pygame.transform.scale(hard_button,(150,100))
        hard_button_hitbox = hard_button.get_rect()
        hard_button_hitbox.topleft = (50,100)
        pygame.draw.rect(screen, (255,0,0), hard_button_hitbox, 2)
        screen.blit(hard_button,(450,100))

    font = pygame.font.SysFont("timesnewroman", 15)
    font.set_bold(True)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text, (0,0))
    pygame.display.flip()
    clock.tick(50) 
    pygame.display.set_caption("Save the Turtles")
#end