import pygame
import random

class Enemy():
    def __init__(self,x, y,rol, speed, size, screen):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.isvisible=True
        self.speed = speed
        self.size = size
        images = ["./assets/plasticbag.png","./assets/plasticbottle.png"]
        self.image = pygame.image.load(images[random.randint(0,1)])
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
    def createenemy(enemylist, screen):
        spawndelay=30
        enemyspawn = random.randint(0,spawndelay)
        rol=0
        if enemyspawn == 1:
            lor = random.randint(0,1)
            if lor == 0:
                enemynewx=-100
                rol=lor
            elif lor == 1:
                enemynewx=1000
                rol=lor
            spawnypos=random.randint(0,650)
            if spawnypos <325:
                rol=0
                lor = rol
            elif spawnypos>325:
                rol=1
                lor=rol
            enemy = Enemy(enemynewx,spawnypos,rol,5,100, screen)
            enemylist.append(enemy)
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