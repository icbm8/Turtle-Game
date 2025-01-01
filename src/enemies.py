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
        self.image = pygame.transform.smoothscale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
    def createenemy(enemylist, screen):
        from main import difficulty
        if difficulty == "Easy":
            spawndelay = 80
        elif difficulty == "Medium":
            spawndelay = 50
        elif difficulty == "Hard":
            spawndelay = 20
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
class Squid():
    def __init__(self,x, y,rol, speed, size, screen):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.isvisible = True
        self.speed = speed
        self.size = size
        self.image = pygame.image.load("./assets/squid.png")
        self.image = pygame.transform.smoothscale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
    def createenemy(squidlist, screen):
        from main import difficulty
        if difficulty == "Easy":
            spawndelay = 100
        elif difficulty == "Medium":
            spawndelay = 70
        elif difficulty == "Hard":
            spawndelay = 40
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
            squid = Squid(enemynewx,spawnypos,rol,5,100, screen)
            squidlist.append(squid)
    def update(self, screen, squidlist):
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
            squidlist.remove(self)