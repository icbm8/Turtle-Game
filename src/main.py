#imports
import pygame
import random
import time
import math
import json
import pygame.transform
from player import Player
from food import Food
from enemies import Enemy
from enemies import Squid
from image_loading import load_images

#starts time and adds facts
start_time = time.time()
facts_for_game = [
    "At least 1,000 sea turtles die each year due to plastic. Thats more than 1 turtle every 9 hours!",
    "By 2050, there will be more plastic than fish in the ocean!",
    "More than 100,000 marine animals die each year due to plastic."
    ]
fact_on_menu = str(random.choice(facts_for_game))
math_questions = ["filla tecst meth"]
marine_questions = ["filla tecst merone"]

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

#variables
FPS = 60
score = 0

#high score saving
def save_high_score(score, filename="high_score.json"):
    with open(filename, "w") as file:
        json.dump({"high_score": high_score}, file)
def load_high_score(filename="high_score.json"):
     with open(filename, "r") as file:
        data = json.load(file)
        return data.get("high_score", 0)
high_score = load_high_score()

#other variables
health = 100
score = 0
difficulty = "Medium"
subject = "Math"
blackout_show = False
blackout_var = 255
speed_change = 0
speed_change_time = 0

#image_loading
images = load_images()
fade_image = images["fade_image"]
background_image = images["background_image"]
play_button = images["play_button"]
settings_button = images["settings_button"]
about_button = images["about_button"]
how_to_play_button = images["how_to_play_button"]
quit_button = images["quit_button"]
easy_button = images["easy_button"]
medium_button = images["medium_button"]
hard_button = images["hard_button"]
math_button = images["math_button"]
marine_button = images["marine_button"]
save_high_score_button = images["save_high_score_button"]
yes_button = images["yes_button"]
no_button = images["no_button"]
exit_button = images["exit_button"]
blackout = images["blackout"]

#font_loading
main_title_font = pygame.font.SysFont("sansserif", 65, bold = True)
main_title_text = main_title_font.render("Save The Turtles", True, (0, 0, 0))
subtitle_font = pygame.font.SysFont("sansserif", 55)
subtitle_text = subtitle_font.render("GASTC Project by Jayden Wu", True, (0, 0, 0))
facts_title_font = pygame.font.SysFont("sansserif", 40, bold = True)
facts_title_text = facts_title_font.render("Real Facts:", True, (0, 0, 0))
facts_font = pygame.font.SysFont("sansserif", 25, bold = True)
facts_text = facts_font.render(str(fact_on_menu), True, (0, 0, 0))
settings_font = pygame.font.SysFont("sansserif", 50, bold = True)

about_font = pygame.font.SysFont("sansserif", 40)
about_text1 = about_font.render("Save The Turtles - a game by Jayden Wu. In this game, you will navigate a turtle through", True, (0, 0, 0))
about_text2 = about_font.render("multiple plastic obstacles. If you hit plastic, you will lose some health.", True, (0, 0, 0))
about_text3 = about_font.render("Every once in a while, the player is asked a question about a subject of their liking (e.g. math", True, (0, 0, 0))
about_text4 = about_font.render(", marine life,) and if they get it wrong, they will lose points and if they get it right they won't", True, (0, 0, 0))
about_text5 = about_font.render("lose any.", True, (0, 0, 0))
about_text6 = about_font.render("This game is targeted to the younger age group (late elementary) to empower the earlier", True, (0, 0, 0))
about_text7 = about_font.render("generation. The sooner people know, the better.", True, (0, 0, 0))
how_to_play_font = pygame.font.SysFont("sansserif", 40, bold = True)
how_to_play_text1 = how_to_play_font.render("Use WASD or arrow keys to navigate your turtle! You start with 100 health and each time you", True, (0, 0, 0))
how_to_play_text2 = how_to_play_font.render("hit an obstacle, for example a plastic bag or bottle, you will lose 10 health and slow down a little.", True, (0, 0, 0))
how_to_play_text3 = how_to_play_font.render("Each time you eat a fish, you gain 1 point and each 5 fish you eat you grow a tiny bit bigger.", True, (0, 0, 0))
how_to_play_text4 = how_to_play_font.render("If you hit a squid, you will lose 15 health and have obscured vision for a short time and also slown down.", True, (0, 0, 0))
how_to_play_text5 = how_to_play_font.render("Survive as long as you can!", True, (0, 0, 0))
display_caps_font = pygame.font.SysFont("sansserif", 25, bold = True)
version_text = display_caps_font.render("v. 4.92  mobile is not supported ", True, (0, 0, 0))

#labels
labels_font = pygame.font.SysFont("sansserif", 30)
play_label_text = labels_font.render("^ Play ^", True, (0, 0, 0))
settings_label_text = labels_font.render("^ Settings ^", True, (0, 0, 0))
about_label_text = labels_font.render("^ About ^", True, (0, 0, 0))
how_to_play_label_text = labels_font.render("^ How To Play ^", True, (0, 0, 0))
quit_label_text = labels_font.render("^ Quit ^", True, (0, 0, 0))

#game labels
game_labels_font = pygame.font.SysFont("sansserif", 25, bold = True)
game_title_text = game_labels_font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
you_lost_font1 = pygame.font.SysFont("sansserif", 80, bold = True)
you_lost_font2 = pygame.font.SysFont("sansserif", 25, bold = True)
you_lost_text1 = you_lost_font1.render("You Lost!", True, (0, 0, 0))
you_lost_text2 = you_lost_font2.render("Thousands of turtles have died due to plastic like you just did.", True, (0, 0, 0))
you_lost_text3 = you_lost_font2.render("However, we can put a stop to this. Donating to fundraising campaigns", True, (0, 0, 0))
you_lost_text4 = you_lost_font2.render("that want to stop ocean pollution, for example #TeamSeas, is a great way to help.", True, (0, 0, 0))
you_lost_text5 = you_lost_font2.render("Press R to Restart, or press the exit button to go back to the menu.", True, (0, 0, 0))

#lists
enemylist = []
foodlist = []
squidlist = []

#other variables
enemy_timer_max = 25
enemy_timer = enemy_timer_max
running_pause = 0

#music loading and playing
pygame.mixer.music.load("./assets/menu_music.mp3")
pygame.mixer.music.set_volume(0)
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
        player.Move(0,-1)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.Move(0,1)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.Move(-1,0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.Move(1,0)

    #other
    elapsed_time = time.time() - start_time

    #blitting background image
    screen.blit(background_image,(0,0))

    #showing the menu
    if menu_show:

        #blitting play button and label
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 160,125
        screen.blit(play_button,(160,125))
        screen.blit(play_label_text, (325,335))

        #blitting settings button and label
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 560,125
        screen.blit(settings_button,(560,125))
        screen.blit(settings_label_text, (605,335))

        #blitting about button and label
        about_button_hitbox = about_button.get_rect()
        about_button_hitbox.topleft = 770,125
        screen.blit(about_button,(770,125))
        screen.blit(about_label_text, (820,335))

        #blitting how to play button and label
        how_to_play_button_hitbox = how_to_play_button.get_rect()
        how_to_play_button_hitbox.topleft = 970,125
        screen.blit(how_to_play_button,(970,125))
        screen.blit(how_to_play_label_text, (1080,335))
                
        #blitting quit button and label
        quit_button_hitbox = quit_button.get_rect()
        quit_button_hitbox.topleft = 560,360
        screen.blit(quit_button,(560,360))
        screen.blit(quit_label_text, (720,570))

        #titles and real facts

        #blitting main title
        screen.blit(main_title_text, (560,20))

        #blitting subtitle
        screen.blit(subtitle_text, (500,70))

        #blitting real facts
        screen.blit(facts_title_text, (200, 600))
        screen.blit(facts_text, (380, 605.5))

        #hitbox collisions
        from main import event
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
        screen.blit(game_title_text, (10, 30))
        score_text = game_labels_font.render("Score: " + str(score), True, (0, 0, 0))    
        high_score_text = game_labels_font.render("High Score: " + str(high_score), True, (0, 0, 0))
        health_text = game_labels_font.render("Health: " + str(health), True, (0, 0, 0)) 
        screen.blit(score_text, (10, 50))
        screen.blit(high_score_text, (10, 75))
        screen.blit(health_text, (10,100))

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
                    player.size += 50
                    player.image = pygame.image.load("./assets/playerturtle.png")
                    player.image = pygame.transform.smoothscale(player.image,(int(player.size*0.15),int(player.size*0.125)))
                    player.rect = player.image.get_rect()
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
                player.speed -= speed_change
                health-=10
            enemy.update(screen, enemylist)

        #squid collision
        for squid in squidlist:
            if player.rect.colliderect(squid.hitbox):
                squid.isvisible=False
                player.speed -= speed_change * 1.25
                blackout_show = True
                health-=15
            squid.update(screen, squidlist)

        #other

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
        Enemy.createenemy(enemylist, screen)
        Food.createfood(foodlist, screen)
        Squid.createenemy(squidlist, screen)
        if score > high_score:
            high_score = score

    #if game is lost
    if health <= 0 and menu_show == False and about_show == False and how_to_play_show == False and settings_show == False:
        screen.blit(you_lost_text1,(200,300))
        screen.blit(you_lost_text2,(200,400))
        screen.blit(you_lost_text3,(200,425))
        screen.blit(you_lost_text4,(200,450))
        screen.blit(you_lost_text5,(200,475))
        game_start = False
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
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
            if no_button_hitbox.collidepoint(event.pos):
                pygame.quit()

    #final captions and text including FPS and caption
    clock.tick(FPS)
    fps_text = display_caps_font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(fps_text, (10,10))
    screen.blit(version_text, (90,10))
    pygame.display.flip()
    if round(elapsed_time) < 60:
        pygame.display.set_caption("Save the Turtles - " + str(round(elapsed_time)) + " Seconds Played")
    elif round(elapsed_time) == 60:
        pygame.display.set_caption("Save the Turtles - 1 Minute Played")
    elif round(elapsed_time) > 60:
        pygame.display.set_caption("Save the Turtles - " + str(math.floor(math.floor(elapsed_time)/60)) + " Minutes and " + str(math.floor(elapsed_time) % 60) + " Seconds Played")
        if math.floor(elapsed_time) % 60 == 0:
            pygame.display.set_caption("Save the Turtles - " + str(math.floor(elapsed_time/60)) + " Minutes Played")
#end