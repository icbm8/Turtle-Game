import pygame
from text_loading import *

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

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
                self.color = BLUE if self.active else GRAY
            if event.type == pygame.KEYDOWN and self.active:
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
                self.txt_surface = FONT.render(self.text, True, BLACK)

        def draw(self, screen):
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            pygame.draw.rect(screen, self.color, self.rect, 2)