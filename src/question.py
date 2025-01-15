import pygame
from text_loading import *
from text_loading import question_generator

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Input Box Example")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)
FONT = pygame.font.Font(None, 36)

class InputBox:
        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = GRAY
            self.text = text
            self.txt_surface = FONT.render(text, True, BLACK)
            self.active = False

        def draw(self, screen):
            

            self.active = True
            while self.active:
                #print("input box is active")
                
                
                pygame.draw.rect(screen, self.color, self.rect, 2)
                self.txt_surface = FONT.render(self.text, True, BLACK)
                screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

                submit_text = FONT.render("Press Enter to Submit", True, BLACK)
                screen.blit(submit_text, (5, 250))

                pygame.display.flip()


                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            if self.text == str(question_answer):
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
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                        

