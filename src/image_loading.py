import pygame

def load_images():
    #images
    fade_image = pygame.image.load("./assets/fade.png")

    #background
    background_image = pygame.image.load("./assets/background.jpg")
    background_image = pygame.transform.smoothscale(background_image,(1500,975))

    #play button image
    play_button = pygame.image.load("./assets/play.png")
    play_button = pygame.transform.smoothscale(play_button,(400,200))

    #settings button image
    settings_button = pygame.image.load("./assets/settings.png")
    settings_button = pygame.transform.smoothscale(settings_button,(210,200))

    #about button image
    about_button = pygame.image.load("./assets/about.png")
    about_button = pygame.transform.smoothscale(about_button,(200,200))

    #how to play button image
    how_to_play_button = pygame.image.load("./assets/howtoplay.png")
    how_to_play_button = pygame.transform.smoothscale(how_to_play_button,(400,200))

    #quit button image
    quit_button = pygame.image.load("./assets/quit.png")
    quit_button = pygame.transform.smoothscale(quit_button,(400,200))

    #easy button image
    easy_button = pygame.image.load("./assets/easy.png")
    easy_button = pygame.transform.smoothscale(easy_button,(338,225))

    #medium button image
    medium_button = pygame.image.load("./assets/medium.png")
    medium_button = pygame.transform.smoothscale(medium_button,(338,225))

    #hard button image
    hard_button = pygame.image.load("./assets/hard.png")
    hard_button = pygame.transform.smoothscale(hard_button,(338,225))

    #math button image
    math_button = pygame.image.load("./assets/math.png")
    math_button = pygame.transform.smoothscale(math_button,(338,225))

    #marine science button image
    marine_button = pygame.image.load("./assets/marinescience.png")
    marine_button = pygame.transform.smoothscale(marine_button,(338,225))

    #save highscore button image
    save_high_score_button = pygame.image.load("./assets/save_high_score.png")
    save_high_score_button = pygame.transform.smoothscale(save_high_score_button,(472,260))

    #yes button image
    yes_button = pygame.image.load("./assets/yes.png")
    yes_button = pygame.transform.smoothscale(yes_button,(150,100))

    #no button image
    no_button = pygame.image.load("./assets/no.png")
    no_button = pygame.transform.smoothscale(no_button,(150,100))

    #exit button image
    exit_button = pygame.image.load("./assets/x.png")
    exit_button = pygame.transform.smoothscale(exit_button,(125,100))

    return {
        "fade_image": fade_image, "background_image": background_image, "play_button": play_button, "settings_button": settings_button,
        "about_button": about_button, "how_to_play_button": how_to_play_button, "quit_button": quit_button, "easy_button": easy_button,
        "medium_button": medium_button, "hard_button": hard_button, "math_button": math_button, "marine_button": marine_button, "exit_button": exit_button,
        "save_high_score_button": save_high_score_button, "yes_button": yes_button, "no_button": no_button}
