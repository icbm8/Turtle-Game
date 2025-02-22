import pygame
import random
from image_loading import enemy_images
from image_loading import squid_image

#enemy class
class Enemy():

    #initialization
    def __init__(self,x, y,rol, speed, size, screen, enemytype):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.isvisible=True
        self.speed = speed
        self.size = size
        self.enemytype = enemytype
        if enemytype == "plastic":
            self.image = pygame.image.load(enemy_images[random.randint(0,1)])
        if enemytype == "squid":
            self.image = squid_image
        self.image = pygame.transform.smoothscale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)

    #creating the enemy and add to the enemy list
    def createenemy(enemylist, screen, enemytype, difficulty):
        if difficulty == "Easy":
            if enemytype == "plastic":
                spawndelay = 80
            elif enemytype == "squid":
                spawndelay = 120
        elif difficulty == "Medium":
            if enemytype == "plastic":
                spawndelay = 50
            elif enemytype == "squid":
                spawndelay = 90
        elif difficulty == "Hard":
            if enemytype == "plastic":
                spawndelay = 20
            elif enemytype == "squid":
                spawndelay = 60
        enemyspawn = random.randint(0,spawndelay)
        rol=0
        if enemyspawn == 1:
            lor = random.randint(0,1)
            if lor == 0:
                enemynewx=-100
                rol=lor
            elif lor == 1:
                enemynewx=1600
                rol=lor
            spawnypos=random.randint(0,975)
            if spawnypos <487.5:
                rol=0
                lor = rol
            elif spawnypos>487.5:
                rol=1
                lor=rol
            enemy = Enemy(enemynewx,spawnypos,rol,5,100, screen, enemytype)
            enemylist.append(enemy)

    #updating the enemy
    def update(self, screen, enemylist):
        if self.isvisible:
            screen.blit(self.image,(self.x, self.y))
            self.hitbox.topleft = (self.x,self.y)
            if self.rol==0:
                self.x+=self.speed
                self.hitbox.x += self.speed
            elif self.rol==1:
                self.x-=self.speed
                self.hitbox.x -= self.speed
        else:
            enemylist.remove(self)