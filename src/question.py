import pygame
from text_loading import *

#variables
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
        def draw(self, screen, question_text, answer, question_mc, subject):
            self.active = True
            while self.active:
                #loading the background image
                from image_loading import background_image
                background_image = pygame.transform.smoothscale(background_image,(1500,975)) 
                screen.blit(background_image,(0,0))

                #loading the font
                question = question_font.render(str(question_text), True, (0,0,0))
                screen.blit(question, (10,80))
                screen.blit(challenge_question_text, (10,10))
                
                question_mc_text = question_font2.render(str(question_mc), True, (0,0,0))
                screen.blit(question_mc_text, (10,120))

                #drawing the rect
                pygame.draw.rect(screen, self.color, self.rect, 2)
                self.txt_surface = question_font.render(self.text, True, BLACK)
                screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

                #drawing submit_text
                if subject == "Marine Science":
                    screen.blit(submit_text, (10, 210))
                else:
                    screen.blit(submit_text, (10, 170))     

                pygame.display.flip()

                #keyboard events
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if self.text == str(answer):
                                self.text = ''
                                self.active = False
                                return True
                            else:
                                self.active = False
                                return False
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        elif event.key == pygame.K_DELETE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                
            
                        

