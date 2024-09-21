import pygame
import random
import time

#######################

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.x = 0
        self.y = 250
        self.angle = 25
        self.screen = screen
        self.image = pygame.image.load("./assets/turtle.png")
        self.image = pygame.transform.scale(self.image,(156,104))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.speed = 10
        self.alive = True
    def Move(self,x_movement,y_movement):
        if self.alive:
            test_rect = self.rect
            test_rect.x += self.speed * x_movement
            test_rect.y += self.speed * y_movement
            collision = False
            if not collision:
                self.x += self.speed * x_movement
                self.y += self.speed * y_movement
    def update(self):
        self.screen.blit(self.image,(self.x,self.y))
class Enemy():
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("../assets/Fish02_A.png")
        self.pic2 = pygame.image.load("../assets/Fish02_B.png")
        self.speed = speed
        self.size = size
        self.pic = pygame.transform.scale(self.pic,(int(self.size*1.25),self.size))
        self.pic2 = pygame.transform.scale(self.pic2,(int(self.size*1.25),self.size))
        self.hitbox = pygame.Rect(self.x,self.y,int(self.size*1.25),self.size)
        self.animation_timer_max = 16
        self.swimming_timer = self.animation_timer_max
        self.swimming_frame = 0
        
        if self.speed < 0:
            self.pic = pygame.transform.flip (self.pic, True, False)
            self.pic2 = pygame.transform.flip (self.pic2, True, False)
        
    def update(self, screen):
        self.swimming_timer -=1
        if self.swimming_timer <= 0:
            self.swimming_timer = self.animation_timer_max
            self.swimming_frame += 1
            if self.swimming_frame > 1:
                self.swimming_frame = 0
        self.x += self.speed
        self.hitbox.x += self.speed
       # pygame.draw.rect(screen, (50,150,250), self.hitbox)
        if self.swimming_frame == 0:
            screen.blit(self.pic,(self.x, self.y))
        else:
            screen.blit(self.pic2,(self.x,self.y))

###########################

pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
backgroundimage = pygame.image.load("./assets/background.jpg")
screen.blit(backgroundimage,(0,0))
protoimage = pygame.image.load("./assets/plasticbag.png")
protoimage = pygame.transform.scale(protoimage,(125,125))
inimi_2_remove = []
clock = pygame.time.Clock()
running = True
player = Player(screen)
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
        
    screen.blit(backgroundimage,(0,0))
    screen.blit(protoimage,(900,0))
    backgroundimage = pygame.transform.scale(backgroundimage,(1101,667))
    player.update()
    pygame.display.flip()
    clock.tick(40) 
    pygame.display.set_caption("Save the Turtles by Jayden Wu Project          FPS: " + str(clock.get_fps()))

#######################
"""
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    projectname_text = font.render("Welcome to Save the Turtles by Jayden Wu", 1,(255,0,0))
    displaytime_text = font.render("Time played: " + str(time), 1,(255,0,0))
   
    screen.blit(projectname_text,(0,0))
    screen.blit(displaytime_text,(30,10))
"""