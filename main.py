import pygame
import random
import time

#######################

start_time = time.time()

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
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)
        self.screen.blit(self.image,(self.x,self.y))
class Enemy():
    def __init__(self,x, y,rol, speed, size, screen):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.isvisible=True
        self.speed = speed
        self.size = size
        self.image = pygame.image.load("./assets/plasticbag.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
    def createenemy(enemylist):
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
            enemy = Enemy(enemynewx,spawnypos,rol,5,100,screen)
            enemylist.append(enemy)
    def update(self, screen):
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
class Enemy_Squid():
    def __init__(self,x, y,rol, speed, size, screen):
        self.x = x
        self.y = y
        self.rol=rol
        self.screen = screen
        self.isvisible=True
        self.speed = speed
        self.size = size
        self.image = pygame.image.load("./assets/squid.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.hitbox = self.image.get_rect()
        self.hitbox.topleft = (self.x,self.y)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
    def createenemy(enemylist):
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
            enemy = Enemy(enemynewx,spawnypos,rol,5,100,screen)
            enemylist.append(enemy)
    def update(self, screen):
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

    def createfood(foodlist):
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
    def update(self, screen):
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

###########################

pygame.init()
score = 0
lives = 3
score = 0
lives = 3
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
running = True
fade_image = pygame.image.load("./assets/fade.png")
screen.blit(fade_image,(0,0))
backgroundimage = pygame.image.load("./assets/background.jpg")
screen.blit(backgroundimage,(0,0))
inimi_2_remove = []
clock = pygame.time.Clock()
player = Player(screen,450)
enemylist = []
foodlist = []
squidlist = []
enemy_timer_max = 25
enemy_timer = enemy_timer_max

##########################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    mouse_x,mouse_y = pygame.mouse.get_pos()       
    keys = pygame.key.get_pressed()

########################

    if keys[pygame.K_w]:
        player.Move(0,-1)
    if keys[pygame.K_s]:
        player.Move(0,1)
    if keys[pygame.K_a]:
        player.Move(-1,0)
    if keys[pygame.K_d]:
        player.Move(1,0)
    if keys[pygame.K_SPACE]:
        print("pause game")
    if keys[pygame.K_n]:
        print("powerup")
    if pygame.mouse.get_pressed()[0]:
        print("idk what to put here")

#########################

    elapsed_time = time.time()-start_time
    screen.blit(backgroundimage,(0,0))
    backgroundimage = pygame.transform.scale(backgroundimage,(1101,667))
    font = pygame.font.SysFont("timesnewroman", 25)
    text = font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
    screen.blit(text, (15, 15))
    for food in foodlist:
        if player.rect.colliderect(food.hitbox):
            food.isvisible=False
            score+=1
            if score % 10 == 0:
                player.size += 50
                player.image = pygame.image.load("./assets/playerturtle.png")
                player.image = pygame.transform.scale(player.image,(int(player.size*0.125),int(player.size*0.125)))
                player.rect = player.image.get_rect()
        food.update(screen)
    text = font.render("Score: " + str(score) + "Size" + str(player.size), True, (0, 0, 0))    
    screen.blit(text, (15, 40))
    text = font.render("Time Played: " + str(round(elapsed_time)) + " seconds", True, (0, 0, 0))
    screen.blit(text, (15, 65))
    text = font.render("Lives: " + str(lives), True, (0, 0, 0))
    screen.blit(text, (15,90))
    player.update()
    Enemy.createenemy(enemylist)
    Food.createfood(foodlist)
    for enemy in enemylist:
        if player.rect.colliderect(enemy.hitbox):
            enemy.isvisible=False
            lives-=1
        enemy.update(screen)
    pygame.display.flip()
    clock.tick(50) 
    pygame.display.set_caption("Save the Turtles: GaSTc Project by Jayden Wu             FPS: " + str(round(clock.get_fps())))

#######################