import pygame
from image_loading import player_loadimage
from image_loading import player_loadflipped

#player class
class Player(pygame.sprite.Sprite):

    #player initialization
    def __init__(self,screen,size):
        self.x = 450
        self.y = 300
        self.angle = 25
        self.screen = screen
        self.size = size
        self.flip(screen,size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.speed = 10
        self.alive = True

    def flip(self,screen,size):
        self.player_image = pygame.transform.scale(player_loadimage,(int(self.size*0.15),int(self.size*0.125)))
        self.player_flipped = pygame.transform.scale(player_loadflipped,(int(self.size*0.15),int(self.size*0.125)))
        self.image = self.player_image

    #player growing
    def grow(self):
        self.size += 50
        self.flip(self.screen,self.size)
        self.image = pygame.image.load("./assets/playerturtle.png")
        self.image = pygame.transform.smoothscale(self.image,(int(self.size*0.15),int(self.size*0.125)))
        self.rect = self.image.get_rect()

    #player movement
    def move(self,x_movement,y_movement):
        if self.alive:
            self.x += self.speed * x_movement
            self.rect.x += self.speed * x_movement
            self.y += self.speed * y_movement
            self.rect.y += self.speed * y_movement
            self.rect.topleft = (self.x,self.y)

    #updating the player
    def update(self):
        self.screen.blit(self.image,(self.x,self.y))