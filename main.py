import pygame
import random
import time
from Player import Player
from Food import Food
from Enemy import Enemy

#######################

start_time = time.time()

###########################

pygame.init()
score = 0
lives = 3
score = 0
lives = 3
game_width = 1000
game_height = 650
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
    if keys[pygame.K_n]:
        print("powerup")
    if pygame.mouse.get_pressed()[0]:
        print("idk what to put here")

#########################

    elapsed_time = time.time()-start_time
    screen.blit(backgroundimage,(0,0))
    backgroundimage = pygame.transform.scale(backgroundimage,(1101,667))
    font = pygame.font.SysFont("timesnewroman", 25)
    text = font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
    screen.blit(text, (15, 15))
    for food in foodlist:
        if player.rect.colliderect(food.hitbox):
            food.isvisible=False
            score+=1
            if score % 10 == 0:
                player.size += 50
                player.image = pygame.image.load("./assets/playerturtle.png")
                player.image = pygame.transform.scale(player.image,(int(player.size*0.125),int(player.size*0.125)))
                player.rect = player.image.get_rect()
        food.update(screen, foodlist)
    text = font.render("Score: " + str(score), True, (0, 0, 0))    
    screen.blit(text, (15, 40))
    text = font.render("Time Played: " + str(round(elapsed_time)) + " seconds", True, (0, 0, 0))
    screen.blit(text, (15, 65))
    text = font.render("Lives: " + str(lives), True, (0, 0, 0))
    screen.blit(text, (15,90))
    player.update()
    Enemy.createenemy(enemylist, screen)
    Food.createfood(foodlist, screen)
    for enemy in enemylist:
        if player.rect.colliderect(enemy.hitbox):
            enemy.isvisible=False
            lives-=1
        enemy.update(screen, enemylist)
    pygame.display.flip()
    clock.tick(50) 
    pygame.display.set_caption("Save the Turtles: GaSTc Project by Jayden Wu             FPS: " + str(round(clock.get_fps())))

#######################