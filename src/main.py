#imports
import pygame
import random
import time
import math
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
math_questions = ["filla tecst meth"]
marine_questions = ["filla tecst merone"]

#initialization and variable defining, also shows image and fade, etc.
pygame.init()

#booleans
running = True
game_start = False
settings_show = False
about_show = False
how_to_play_show = False
save_high_score_show = False
quit = False

#game screen
game_width = 1500
game_height = 975
screen = pygame.display.set_mode((game_width, game_height))

#variables
score = 0
highscore = 0
health = 100
score = 0
difficulty = "Medium"
subject = "Math"

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

#other
clock = pygame.time.Clock()
player = Player(screen,450)
enemylist = []
foodlist = []
squidlist = []
enemy_timer_max = 25
menu_show=True
enemy_timer = enemy_timer_max
fact_on_menu = str(random.choice(facts_for_game))
running_pause = 0

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
    screen.blit(background_image,(0,0))
    font = pygame.font.SysFont("sansserif", 45)
    font.set_bold(True)

    #showing the menu
    if menu_show:

        #blitting play button and label
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 160,125
        screen.blit(play_button,(160,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ Play ^", True, (0, 0, 0))
        screen.blit(text, (325,335))

        #blitting settings button and label
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 560,125
        screen.blit(settings_button,(560,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ Settings ^", True, (0, 0, 0))
        screen.blit(text, (605,335))

        #blitting about button and label
        about_button_hitbox = about_button.get_rect()
        about_button_hitbox.topleft = 770,125
        screen.blit(about_button,(770,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ About ^", True, (0, 0, 0))
        screen.blit(text, (820,335))

        #blitting how to play button and label
        how_to_play_button_hitbox = how_to_play_button.get_rect()
        how_to_play_button_hitbox.topleft = 970,125
        screen.blit(how_to_play_button,(970,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ How To Play ^", True, (0, 0, 0))
        screen.blit(text, (1080,335))
                
        #blitting quit button and label
        quit_button_hitbox = quit_button.get_rect()
        quit_button_hitbox.topleft = 560,360
        screen.blit(quit_button,(560,360))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ Quit ^", True, (0, 0, 0))
        screen.blit(text, (720,570))

        #titles and real facts

        #blitting main title
        font = pygame.font.SysFont("sansserif", 65)
        font.set_bold(True)
        text = font.render("Save The Turtles", True, (0, 0, 0))
        screen.blit(text, (560,20))

        #blitting subtitle
        font = pygame.font.SysFont("sansserif", 55)
        text = font.render("GaSTC Project by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (500,70))

        #blitting real facts
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Real Facts:", True, (0, 0, 0))
        screen.blit(text, (200, 600))
        font = pygame.font.SysFont("sansserif", 25)
        font.set_bold(True)
        text = font.render(str(fact_on_menu), True, (0, 0, 0))
        screen.blit(text, (380, 605.5))

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

        #blitting game title
        font = pygame.font.SysFont("sansserif", 25)
        font.set_bold(True)
        text = font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (10, 30))

        #blitting score, highscore and health
        font.set_bold(False)
        text = font.render("Score: " + str(score), True, (0, 0, 0))    
        screen.blit(text, (10, 50))
        text = font.render("High Score: " + str(highscore), True, (0, 0, 0))    
        screen.blit(text, (10, 75))
        text = font.render("Health: " + str(health), True, (0, 0, 0))
        screen.blit(text, (10,100))

        #blitting exit
        exit_button = pygame.image.load("./assets/x.png")
        exit_button = pygame.transform.smoothscale(exit_button,(125,100))
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))

        #exit button collision
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
        
        #enemy collision
        for enemy in enemylist:
            if player.rect.colliderect(enemy.hitbox):
                enemy.isvisible=False
                health-=10
            enemy.update(screen, enemylist)

        #squid collision
        for squid in squidlist:
            if player.rect.colliderect(squid.hitbox):
                squid.isvisible=False
                screen.blit(fade_image,(0,0))
                health-=20
            squid.update(screen, squidlist)

        #other
        player.update()
        Enemy.createenemy(enemylist, screen)
        Food.createfood(foodlist, screen)
        Squid.createenemy(squidlist, screen)
        if health == 0:
             game_start = False
             menu_show = True
        if score > highscore:
            highscore = score

    #if settings were clicked
    if settings_show:

        #blitting settings text
        font = pygame.font.SysFont("sansserif", 50)
        font.set_bold(True)
        text = font.render("Difficulty: " + difficulty, True, (0, 0, 0))
        screen.blit(text, (560, 20))
        text = font.render("Subject: " + subject, True, (0, 0, 0))
        screen.blit(text, (560, 350))

        #blitting the buttons

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
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Save The Turtles - a game by Jayden Wu. In this game, you will navigate a turtle through", True, (0, 0, 0))
        screen.blit(text, (20, 105))
        text = font.render("multiple plastic obstacles. If you hit plastic, you will lose some health.", True, (0, 0, 0))
        screen.blit(text, (20, 145))
        text = font.render("Every once in a while, the player is asked a question about a subject of their liking (e.g. math", True, (0, 0, 0))
        screen.blit(text, (20, 265))
        text = font.render(", marine life,) and if they get it wrong, they will lose points and if they get it right they won't", True, (0, 0, 0))
        screen.blit(text, (20, 305))
        text = font.render("lose any.", True, (0, 0, 0))
        screen.blit(text, (20, 345))
        text = font.render("This game is targeted to the younger age group (late elementary) to empower the earlier", True, (0, 0, 0))
        screen.blit(text, (20, 425))
        text = font.render("generation. The sooner people know, the better.", True, (0, 0, 0))
        screen.blit(text, (20, 465))

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
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Use WASD or arrow keys to navigate your turtle! You start with 100 health and each time you", True, (0, 0, 0))
        screen.blit(text, (20, 105))
        text = font.render("hit an obstacle, for example a plastic bag or bottle, you will lose 10 health. Each time you eat", True, (0, 0, 0))
        screen.blit(text, (20, 145))
        text = font.render("a fish, you gain 1 point and each 5 fish you eat you grow a tiny bit bigger.", True, (0, 0, 0))
        screen.blit(text, (20, 185))
        text = font.render("If you hit a squid, you will lose 20 health and have obscured vision for a few seconds.", True, (0, 0, 0))
        screen.blit(text, (20, 265))
        text = font.render("Survive as long as you can!", True, (0, 0, 0))
        screen.blit(text, (20, 305))

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
        
        screen.blit(save_high_score_button, (500,400))
        screen.blit(yes_button, (650,500))
        screen.blit(no_button, (750,500))
        if quit:
            pygame.quit()

    #final captions and text including FPS and caption
    font = pygame.font.SysFont("sansserif", 25)
    font.set_bold(True)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text, (10,10))
    text = font.render("v. 4.1  mobile is not supported ", True, (0, 0, 0))
    screen.blit(text, (90,10))
    pygame.display.flip()
    clock.tick(60) 
    if round(elapsed_time) < 60:
        pygame.display.set_caption("Save the Turtles - " + str(round(elapsed_time)) + " Seconds Played")
    elif round(elapsed_time) == 60:
        pygame.display.set_caption("Save the Turtles - 1 Minute Played")
    elif round(elapsed_time) > 60:
        pygame.display.set_caption("Save the Turtles - " + str(math.floor(math.floor(elapsed_time)/60)) + " Minutes and " + str(math.floor(elapsed_time) % 60) + " Seconds Played")
        if math.floor(elapsed_time) % 60 == 0:
            pygame.display.set_caption("Save the Turtles - " + str(math.floor(elapsed_time/60)) + " Minutes Played")
#end