#imports
import pygame
import random
import time
import math
import json
import sys
import pygame.transform
from player import Player
from food import Food
from enemies import Enemy
from text_loading import *
from image_loading import *
from question import InputBox

#starts time and adds facts
start_time = time.time()

#initialization and screen defining
pygame.init()
pygame.mixer.init()
game_width = 1500
game_height = 975
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
player = Player(screen,450)

#booleans
running = True
menu_show = True
game_start = False
settings_show = False
about_show = False
how_to_play_show = False
save_high_score_show = False
quit = False

#high score saving
def save_high_score(score, filename = get_asset_path("high_score.json")):
    with open(filename, "w") as file:
        json.dump({"high_score": high_score}, file)

#loading the high score
def load_high_score(filename = get_asset_path("high_score.json")):
     with open(filename, "r") as file:
        data = json.load(file)
        return data.get("high_score", 0)
high_score = load_high_score()

#variables
FPS = 60
score = 0
health = 100
score = 0
difficulty = "Medium"
subject = "Math"
blackout_show = False
blackout_var = 255
blackout_change = 0
speed_change = 0
speed_change_time = 0
diff_question = 0
show_question = False

#lists
enemylist = []
foodlist = []

#other variables
enemy_timer_max = 25
enemy_timer = enemy_timer_max
running_pause = 0

#music loading and playing
pygame.mixer.music.load(get_asset_path("assets/menu_music.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)

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
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0,-1)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0,1)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-1,0)
        player.image = player.player_flipped
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(1,0)
        player.image = player.player_image
        

    #other
    elapsed_time = time.time() - start_time

    #blitting background image
    screen.blit(background_image,(0,0))

    #showing the menu
    if menu_show:

        #blitting play button and label
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 160,150
        screen.blit(play_button,(160,150))
        screen.blit(play_label_text, (315,360))

        #blitting settings button and label
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 560,150
        screen.blit(settings_button,(560,150))
        screen.blit(settings_label_text, (595, 360))

        #blitting about button and label
        about_button_hitbox = about_button.get_rect()
        about_button_hitbox.topleft = 770,150
        screen.blit(about_button,(770,150))
        screen.blit(about_label_text, (810, 360))

        #blitting how to play button and label
        how_to_play_button_hitbox = how_to_play_button.get_rect()
        how_to_play_button_hitbox.topleft = 970,150
        screen.blit(how_to_play_button,(970,150))
        screen.blit(how_to_play_label_text, (1070, 360))
                
        #blitting quit button and label
        quit_button_hitbox = quit_button.get_rect()
        quit_button_hitbox.topleft = 560,410
        screen.blit(quit_button,(560,410))
        screen.blit(quit_label_text, (710,620))

        #titles and real facts

        #blitting main title
        screen.blit(main_title_text, (560,5))

        #blitting subtitle
        screen.blit(subtitle_text, (500, 75))

        #blitting real facts
        screen.blit(facts_title_text, (200, 660))
        screen.blit(facts_text, (392, 672))

        #hitbox collisions
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_hitbox and play_button_hitbox.collidepoint(event.pos):
                game_start = True
                menu_show = False
                play_button_hitbox = None  # Delete the hitbox after click
            if settings_button_hitbox and settings_button_hitbox.collidepoint(event.pos):
                settings_show = True
                menu_show = False
                settings_button_hitbox = None
            if about_button_hitbox and about_button_hitbox.collidepoint(event.pos):
                about_show = True
                menu_show = False
                about_button_hitbox = None
            if how_to_play_button_hitbox and how_to_play_button_hitbox.collidepoint(event.pos):
                how_to_play_show = True
                menu_show = False
                how_to_play_button_hitbox = None
            if quit_button_hitbox and quit_button_hitbox.collidepoint(event.pos):
                menu_show = False
                save_high_score_show = True
    
    #playing and showing the game
    if game_start:

        #blitting game title, score, high score, health
        screen.blit(game_title_text, (10, 32.5))
        score_text = game_labels_font.render("Score: " + str(score), True, (0, 0, 0))    
        high_score_text = game_labels_font.render("High Score: " + str(high_score), True, (0, 0, 0))
        health_text = game_labels_font.render("Health: " + str(health), True, (0, 0, 0)) 
        screen.blit(score_text, (10, 57.5))
        screen.blit(high_score_text, (10, 82.5))
        screen.blit(health_text, (10,107.5))

        #blitting exit button and exit button collision
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                game_start = False
                menu_show = True

        #weight system and food collisions
        for food in foodlist:
            if player.rect.colliderect(food.hitbox):
                food.isvisible=False
                score+=1
                if score % 5 == 0:
                    player.grow()
                if score % diff_question == 0:
                    show_question = True
            food.update(screen, foodlist)
        
        #speed reduction
        if difficulty == "Easy":
            speed_change = 0.5
            speed_change_time += 0.004
        elif difficulty == "Medium":
            speed_change = 1
            speed_change_time += 0.002
        elif difficulty == "Hard":
            speed_change = 1.5
            speed_change_time += 0.001
        if speed_change_time > 1:
            player.speed = 10

        #enemy collision
        for enemy in enemylist:
            if player.rect.colliderect(enemy.hitbox):
                enemy.isvisible=False
                if enemy.enemytype == "plastic":
                    player.speed -= speed_change
                    health-=10
                elif enemy.enemytype == "squid":
                    player.speed -= speed_change * 1.25
                    blackout_show = True
                    health-=15
            enemy.update(screen, enemylist)

        #other

        #difficulty for the question
        if difficulty == "Easy":
            diff_question = 15
        if difficulty == "Medium":
            diff_question = 10
        if difficulty == "Hard":
            diff_question = 5

        #blackout
        if blackout_show:
            if difficulty == "Easy":
                blackout_change = 25
            if difficulty == "Medium":
                blackout_change = 15
            if difficulty == "Medium":
                blackout_change = 5
            if blackout_var >= 0:
                blackout_var -= blackout_change
                blackout.set_alpha(blackout_var)
                screen.blit(blackout,(0,0))
        if blackout_var <= 0:
            blackout_show = False
            blackout_var = 255

        player.update()
        Enemy.createenemy(enemylist, screen, "plastic", difficulty)
        Enemy.createenemy(enemylist, screen, "squid", difficulty)
        Food.createfood(foodlist, screen,difficulty)
        if score > high_score:
            high_score = score

    #question show
    if show_question:
        input_box = InputBox(5, 160, 800, 40)
        question_random = random.randint(0,len(math_questions)-1)
        question_text = str(math_questions[question_random])
        question_answer = math_answers[question_random]
        game_start = False

        result_is_correct = input_box.draw(screen, question_text, question_answer)
        if result_is_correct:
            score += 3
            health += 10
        show_question = False
        game_start = True

    #if game is lost
    if health <= 0 and menu_show == False and about_show == False and how_to_play_show == False and settings_show == False:
        screen.blit(you_lost_text1,(600,10))
        screen.blit(you_lost_text2,(20,100))
        screen.blit(you_lost_text3,(20,150))
        screen.blit(you_lost_text4,(20,200))
        screen.blit(you_lost_text5,(20,250))
        screen.blit(you_lost_text6,(20,300))
        game_start = False
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))

        #
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                menu_show = True
                game_start = True
                health = 100
                score = 0
                player.x = 5
                player.y = 450
        if keys[pygame.K_r]:
            game_start = True
            health = 100
            score = 0
            player.x = 5
            player.y = 450

    #if settings were clicked
    if settings_show:

        #blitting settings text
        difficulty_text = settings_font.render("Difficulty: " + difficulty, True, (0, 0, 0))
        subject_text = settings_font.render("Subject: " + subject, True, (0, 0, 0))
        screen.blit(difficulty_text, (560, 20))
        screen.blit(subject_text, (560, 350))

        #blitting easy button
        easy_button_hitbox = easy_button.get_rect()
        easy_button_hitbox.topleft = (200,75)
        screen.blit(easy_button,(200,75))

        #blitting medium button
        medium_button_hitbox = medium_button.get_rect()
        medium_button_hitbox.topleft = (600,75)
        screen.blit(medium_button,(600,75))

        #blitting hard button
        hard_button_hitbox = hard_button.get_rect()
        hard_button_hitbox.topleft = (1000,75)
        screen.blit(hard_button,(1000,75))

        #blitting math button
        math_button_hitbox = math_button.get_rect()
        math_button_hitbox.topleft = (400,400)
        screen.blit(math_button,(400,400))

        #blitting marine science button
        marine_button_hitbox = marine_button.get_rect()
        marine_button_hitbox.topleft = (750,400)
        screen.blit(marine_button,(750,400))

        #blitting exit button
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))

        #button hitbox collisions
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button_hitbox.collidepoint(event.pos):
                difficulty = "Easy"
            if medium_button_hitbox.collidepoint(event.pos):
                difficulty = "Medium"
            if hard_button_hitbox.collidepoint(event.pos):
                difficulty = "Hard"
            if exit_button_hitbox.collidepoint(event.pos):
                settings_show = False
                menu_show = True
            if math_button_hitbox.collidepoint(event.pos):
                subject = "Math"
            if marine_button_hitbox.collidepoint(event.pos):
                subject = "Marine Science"

    #if about was clicked
    if about_show:

        #exit button blit and label
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                    about_show = False
                    menu_show = True

        #about text
        screen.blit(about_text1, (20, 105))
        screen.blit(about_text2, (20, 145))
        screen.blit(about_text3, (20, 265))
        screen.blit(about_text4, (20, 305))
        screen.blit(about_text5, (20, 345))
        screen.blit(about_text6, (20, 425))
        screen.blit(about_text7, (20, 465))

    #if how_to_play was clicked
    if how_to_play_show:

        #blitting exit button and creating hitbox
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                    how_to_play_show = False
                    menu_show = True

        #how to play text
        screen.blit(how_to_play_text1, (20, 105))
        screen.blit(how_to_play_text2, (20, 145))
        screen.blit(how_to_play_text3, (20, 185))
        screen.blit(how_to_play_text4, (20, 265))
        screen.blit(how_to_play_text5, (20, 305))
        screen.blit(how_to_play_text6, (20, 345))

    #if quit was clicked it will sask player to save high score
    if save_high_score_show:
        
        #exit button blit and label
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                    save_high_score_show = False
                    menu_show = True
        
        screen.blit(save_high_score_button, (300,100))
        yes_button_hitbox = yes_button.get_rect()
        yes_button_hitbox.topleft = (400,360)
        screen.blit(yes_button, (400,360))
        no_button_hitbox = no_button.get_rect()
        no_button_hitbox.topleft = (900,360)
        screen.blit(no_button, (900,360))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if yes_button_hitbox.collidepoint(event.pos):
                save_high_score(high_score)
                pygame.quit()
                sys.exit()
            if no_button_hitbox.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    #final captions and text including FPS and caption
    clock.tick(FPS)
    fps_text = display_caps_font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(fps_text, (10,10))
    screen.blit(version_text, (110,10))
    pygame.display.flip()
    
    #time played caption
    if round(elapsed_time) < 60:
        pygame.display.set_caption("Save the Turtles - " + str(round(elapsed_time)) + " Seconds Played")
    elif round(elapsed_time) == 60:
        pygame.display.set_caption("Save the Turtles - 1 Minute Played")
    elif round(elapsed_time) > 60:
        pygame.display.set_caption("Save the Turtles - " + str(math.floor(math.floor(elapsed_time)/60)) + " Minutes and " + str(math.floor(elapsed_time) % 60) + " Seconds Played")
        if math.floor(elapsed_time) % 60 == 0:
            pygame.display.set_caption("Save the Turtles - " + str(math.floor(elapsed_time/60)) + " Minutes Played")
#end