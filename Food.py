import pygame
import random

class Food():
    def __init__(self,x, y,rol, speed, size, screen):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.speed = speed
        self.size = size
        self.image = pygame.image.load("./assets/food.png")
        self.image = pygame.transform.scale(self.image,(int(self.size*0.5),int(self.size*0.5)))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
        self.isvisible=True

    def createfood(foodlist, screen):
        foodspawn = random.randint(0,40)
        frol=0
        if foodspawn == 1:
            foodspawnin = random.randint(0,1)
            if foodspawnin == 0:
                foodnewx=-100
                frol=foodspawnin
            elif foodspawnin == 1:
                foodnewx=900
                frol=foodspawnin
            foodypos=random.randint(0,650)
            if foodypos == 0:
                frol=0
            elif foodypos==650:
                frol=1
            food = Food(foodnewx,foodypos,frol,5,100,screen)
            foodlist.append(food)
    def update(self, screen, foodlist):
        if self.isvisible:
            screen.blit(self.image,(self.x, self.y))
            if self.rol==0:
                self.x+=self.speed
                self.hitbox.x += self.speed
            elif self.rol==1:
                self.x-=self.speed
                self.hitbox.x -= self.speed
        else:
            foodlist.remove(self)