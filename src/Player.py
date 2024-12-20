import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,screen,size):
        self.x = 0
        self.y = 250
        self.angle = 25
        self.screen = screen
        self.size = size
        self.image = pygame.image.load("./assets/playerturtle.png")
        self.image = pygame.transform.scale(self.image,(int(self.size*0.15),int(self.size*0.125)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.speed = 10
        self.alive = True
    def Move(self,x_movement,y_movement):
        if self.alive:
            self.x += self.speed * x_movement
            self.rect.x += self.speed * x_movement
            self.y += self.speed * y_movement
            self.rect.y += self.speed * y_movement
            self.rect.topleft = (self.x,self.y)
    def update(self):
        self.screen.blit(self.image,(self.x,self.y))