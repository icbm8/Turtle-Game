#imports
import pygame
import random
import time
import pygame.transform
from player import Player
from food import Food
from enemies import Enemy

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
score = 0
health = 100
score = 0
game_width = 1500
game_height = 975
game_start = False
settings_show = False
about_show = False
howtoplay_show = False
difficulty = "Medium"
subject = "Math"
screen = pygame.display.set_mode((game_width, game_height))
running = True
fade_image = pygame.image.load("./assets/fade.png")
screen.blit(fade_image,(0,0))
backgroundimage = pygame.image.load("./assets/background.jpg")
backgroundimage = pygame.transform.smoothscale(backgroundimage,(1500,975))
inimi_2_remove = []
clock = pygame.time.Clock()
player = Player(screen,450)
enemylist = []
foodlist = []
enemy_timer_max = 25
enemy_timer = enemy_timer_max
menu_show = True
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

#screen blitting the menu buttons + labels
    elapsed_time = time.time() - start_time
    screen.blit(backgroundimage,(0,0))
    font = pygame.font.SysFont("sansserif", 45)
    font.set_bold(True)
    if menu_show:
        play_button = pygame.image.load("./assets/play.png")
        play_button = pygame.transform.smoothscale(play_button,(400,200))
        play_button_hitbox = play_button.get_rect()
        play_button_hitbox.topleft = 160,125
        screen.blit(play_button,(160,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ Play ^", True, (0, 0, 0))
        screen.blit(text, (325,335))
        settings_button = pygame.image.load("./assets/settings.png")
        settings_button = pygame.transform.smoothscale(settings_button,(210,200))
        settings_button_hitbox = settings_button.get_rect()
        settings_button_hitbox.topleft = 560,125
        screen.blit(settings_button,(560,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ Settings ^", True, (0, 0, 0))
        screen.blit(text, (605,335))
        about_button = pygame.image.load("./assets/about.png")
        about_button = pygame.transform.smoothscale(about_button,(200,200))
        about_button_hitbox = about_button.get_rect()
        about_button_hitbox.topleft = 770,125
        screen.blit(about_button,(770,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ About ^", True, (0, 0, 0))
        screen.blit(text, (820,335))
        howtoplay_button = pygame.image.load("./assets/howtoplay.png")
        howtoplay_button = pygame.transform.smoothscale(howtoplay_button,(400,200))
        howtoplay_button_hitbox = howtoplay_button.get_rect()
        howtoplay_button_hitbox.topleft = 970,125
        screen.blit(howtoplay_button,(970,125))
        font = pygame.font.SysFont("sansserif", 30)
        text = font.render("^ How To Play ^", True, (0, 0, 0))
        screen.blit(text, (1080,335))

#titles and real facts
        font = pygame.font.SysFont("sansserif", 65)
        font.set_bold(True)
        text = font.render("Save The Turtles", True, (0, 0, 0))
        screen.blit(text, (560,20))
        font = pygame.font.SysFont("sansserif", 55)
        text = font.render("GaSTC Project by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (500,70))
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Real Facts:", True, (0, 0, 0))
        screen.blit(text, (200, 375))
        font = pygame.font.SysFont("sansserif", 25)
        font.set_bold(True)
        text = font.render(str(fact_on_menu), True, (0, 0, 0))
        screen.blit(text, (380, 382.5))
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
            if howtoplay_button_hitbox and howtoplay_button_hitbox.collidepoint(event.pos):
                howtoplay_show = True
                menu_show = False
                howtoplay_button_hitbox = None

#playing and showing the game
    if game_start:
        font = pygame.font.SysFont("sansserif", 25)
        font.set_bold(True)
        text = font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
        screen.blit(text, (10, 30))
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
        font.set_bold(False)
        text = font.render("Score: " + str(score), True, (0, 0, 0))    
        screen.blit(text, (10, 50))
        text = font.render("Health: " + str(health), True, (0, 0, 0))
        screen.blit(text, (10,75))
        exit_button = pygame.image.load("./assets/x.png")
        exit_button = pygame.transform.smoothscale(exit_button,(125,100))
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                game_start = False
                menu_show = True
        player.update()
        Enemy.createenemy(enemylist, screen)
        Food.createfood(foodlist, screen)
        if health == 0:
             game_start == False
        for enemy in enemylist:
            if player.rect.colliderect(enemy.hitbox):
                enemy.isvisible=False
                health-=10
            enemy.update(screen, enemylist)

#if settings were clicked
    if settings_show:
        font = pygame.font.SysFont("sansserif", 50)
        font.set_bold(True)
        text = font.render("Difficulty: " + difficulty, True, (0, 0, 0))
        screen.blit(text, (560, 20))
        text = font.render("Subject: " + subject, True, (0, 0, 0))
        screen.blit(text, (560, 350))
        font = pygame.font.SysFont("sansserif", 30)
        font.set_bold(False)
        text = font.render("Math", True, (0, 0, 0))
        screen.blit(text, (150, 450))
        math_hitbox = text.get_rect()
        math_hitbox.topleft = (150,450)
        text = font.render("Marine Science", True, (0, 0, 0))
        screen.blit(text, (400, 450))
        marine_hitbox = text.get_rect()
        marine_hitbox.topleft = (400,450)
        easy_button = pygame.image.load("./assets/easy.png")
        easy_button = pygame.transform.smoothscale(easy_button,(338,225))
        easy_button_hitbox = easy_button.get_rect()
        easy_button_hitbox.topleft = (200,75)
        screen.blit(easy_button,(200,75))
        medium_button = pygame.image.load("./assets/medium.png")
        medium_button = pygame.transform.smoothscale(medium_button,(338,225))
        medium_button_hitbox = medium_button.get_rect()
        medium_button_hitbox.topleft = (600,75)
        screen.blit(medium_button,(600,75))
        hard_button = pygame.image.load("./assets/hard.png")
        hard_button = pygame.transform.smoothscale(hard_button,(338,225))
        hard_button_hitbox = hard_button.get_rect()
        hard_button_hitbox.topleft = (1000,75)
        screen.blit(hard_button,(1000,75))
        exit_button = pygame.image.load("./assets/x.png")
        exit_button = pygame.transform.smoothscale(exit_button,(125,100))
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
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
            if math_hitbox.collidepoint(event.pos):
                subject = "Math"
            if marine_hitbox.collidepoint(event.pos):
                subject = "Marine Science"

#if about was clicked
    if about_show:
        exit_button = pygame.image.load("./assets/x.png")
        exit_button = pygame.transform.smoothscale(exit_button,(125,100))
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                    about_show = False
                    menu_show = True
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Save The Turtles - a game by Jayden Wu. In this game, you will navigate", True, (0, 0, 0))
        screen.blit(text, (20, 105))
        text = font.render("a turtle through mulitple plastic obstacles. If you hit plastic, you will", True, (0, 0, 0))
        screen.blit(text, (20, 145))
        text = font.render("lose some health.", True, (0, 0, 0))
        screen.blit(text, (20, 185))
        text = font.render("Every once in a while, the player is asked a question about a subject of ", True, (0, 0, 0))
        screen.blit(text, (20, 265))
        text = font.render("their liking (e.g. math, marine life,) and if they get it wrong, they will", True, (0, 0, 0))
        screen.blit(text, (20, 305))
        text = font.render("lose points and if they get it right they won't lose any.", True, (0, 0, 0))
        screen.blit(text, (20, 345))
        text = font.render("This game is targeted to the younger age group (late elementary) to", True, (0, 0, 0))
        screen.blit(text, (20, 425))
        text = font.render("empower the earlier generation. The sooner people know, the better.", True, (0, 0, 0))
        screen.blit(text, (20, 465))

#if howtoplay was clicked
    if howtoplay_show:
        exit_button = pygame.image.load("./assets/x.png")
        exit_button = pygame.transform.smoothscale(exit_button,(125,100))
        exit_button_hitbox = exit_button.get_rect()
        exit_button_hitbox.topleft = (1380,0)
        screen.blit(exit_button,(1380,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_hitbox.collidepoint(event.pos):
                    howtoplay_show = False
                    menu_show = True
        font = pygame.font.SysFont("sansserif", 40)
        font.set_bold(True)
        text = font.render("Use WASD or arrow keys to navigate your turtle! You start with 100", True, (0, 0, 0))
        screen.blit(text, (20, 105))
        text = font.render("health and each time you hit an obstacle, for example a plastic", True, (0, 0, 0))
        screen.blit(text, (20, 145))
        text = font.render("bag or bottle, you will lose 10 health.", True, (0, 0, 0))
        screen.blit(text, (20, 185))
        text = font.render("Each time you eat a fish, you gain 1 point and each 5 fish you", True, (0, 0, 0))
        screen.blit(text, (20, 265))
        text = font.render("eat you grow a tiny bit bigger.", True, (0, 0, 0))
        screen.blit(text, (20, 305))

#final captions and text including FPS and caption
    font = pygame.font.SysFont("sansserif", 25)
    font.set_bold(True)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text, (10,10))
    pygame.display.flip()
    clock.tick(60) 
    pygame.display.set_caption("Save the Turtles - " + str(round(elapsed_time)) + " seconds played")

#end