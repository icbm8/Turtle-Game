import pygame
from text_loading import *

#initialization
pygame.init()

#variables
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Input Box Example")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)


#class for the input box
class InputBox:
        
        #initialization
        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = GRAY
            self.text = text
            self.txt_surface = question_font.render(text, True, BLACK)
            self.active = False

        #drawing the box
        def draw(self, screen, question_text, answer):
            self.active = True
            while self.active:
                #loading the background image
                from image_loading import background_image
                background_image = pygame.transform.smoothscale(background_image,(1500,975)) 
                screen.blit(background_image,(0,0))

                #loading the font
                question = question_font.render(str(question_text), True, (0,0,0))
                screen.blit(question, (5,130))

                #drawing the rect
                pygame.draw.rect(screen, self.color, self.rect, 2)
                self.txt_surface = question_font.render(self.text, True, BLACK)
                screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

                #drawing submit_text

                screen.blit(submit_text, (5, 250))

                pygame.display.flip()

                #keyboard events
                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            if self.text == str(answer):
                                print(self.text)
                                print("correct")
                                self.text = ''
                                self.active = False
                                return True
                            else:
                                print("incorrect")
                                self.active = False
                                return False
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            print("work")
                            self.text = self.text[:-1]
                        elif event.key == pygame.K_DELETE:
                            print("workaodu")

                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                
            
                        

