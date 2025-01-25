import pygame
pygame.init()
pygame.display.set_mode()

#images
fade_image = pygame.image.load("./assets/fade.png").convert_alpha()
player_loadimage = pygame.image.load("./assets/playerturtle.png")
player_loadflipped = pygame.transform.flip(player_loadimage, True, False)


#background
background_image = pygame.image.load("./assets/background.jpg").convert_alpha()
background_image = pygame.transform.smoothscale(background_image,(1500,975))

#play button image
play_button = pygame.image.load("./assets/play.png").convert_alpha()
play_button = pygame.transform.smoothscale(play_button,(400,200))

#settings button image
settings_button = pygame.image.load("./assets/settings.png").convert_alpha()
settings_button = pygame.transform.smoothscale(settings_button,(210,200))

#about button image
about_button = pygame.image.load("./assets/about.png").convert_alpha()
about_button = pygame.transform.smoothscale(about_button,(200,200))

#how to play button image
how_to_play_button = pygame.image.load("./assets/howtoplay.png").convert_alpha()
how_to_play_button = pygame.transform.smoothscale(how_to_play_button,(400,200))

#quit button image
quit_button = pygame.image.load("./assets/quit.png").convert_alpha()
quit_button = pygame.transform.smoothscale(quit_button,(400,200))

#easy button image
easy_button = pygame.image.load("./assets/easy.png").convert_alpha()
easy_button = pygame.transform.smoothscale(easy_button,(338,225))
#medium button image
medium_button = pygame.image.load("./assets/medium.png").convert_alpha()
medium_button = pygame.transform.smoothscale(medium_button,(338,225))
#hard button image
hard_button = pygame.image.load("./assets/hard.png").convert_alpha()
hard_button = pygame.transform.smoothscale(hard_button,(338,225))
#math button image
math_button = pygame.image.load("./assets/math.png").convert_alpha()
math_button = pygame.transform.smoothscale(math_button,(338,225))
#marine science button image
marine_button = pygame.image.load("./assets/marinescience.png").convert_alpha()
marine_button = pygame.transform.smoothscale(marine_button,(338,225))
#save highscore button image
save_high_score_button = pygame.image.load("./assets/save_high_score.png").convert_alpha()
save_high_score_button = pygame.transform.smoothscale(save_high_score_button,(944,520))
#yes button image
yes_button = pygame.image.load("./assets/yes.png").convert_alpha()
yes_button = pygame.transform.smoothscale(yes_button,(200,200))
#no button image
no_button = pygame.image.load("./assets/no.png").convert_alpha()
no_button = pygame.transform.smoothscale(no_button,(200,200))
#exit button image
exit_button = pygame.image.load("./assets/x.png").convert_alpha()
exit_button = pygame.transform.smoothscale(exit_button,(125,100))
#blackout image
blackout = pygame.image.load("./assets/black.png").convert_alpha()
blackout = pygame.transform.smoothscale(blackout,(2000,1000))