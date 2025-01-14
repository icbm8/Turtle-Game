import pygame
import sys

class QuestionDialog:

    def __init__(self, screen):
        self.screen = screen
        self.running = False
        self.input_text = ''
        self.question = ''
        self.correct_answer = ''

    def show_dialog(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.input_text = ''
        self.running = True
        result = self.run_dialog()
        return result

    def run_dialog(self):
        # Set up fonts
        font = pygame.font.Font(None, 40)
        input_font = pygame.font.Font(None, 30)

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        while self.running:
            self.screen.fill(WHITE)
            
            # Display the question
            question_surface = font.render(self.question, True, BLACK)
            self.screen.blit(question_surface, (50, 50))
            
            # Display the input box
            input_surface = input_font.render(self.input_text, True, BLACK)
            pygame.draw.rect(self.screen, BLACK, (50, 150, 500, 40), 2)
            self.screen.blit(input_surface, (55, 155))

            # Display "Submit" text
            submit_text = font.render("Press Enter to Submit", True, BLACK)
            self.screen.blit(submit_text, (50, 250))
            
            pygame.display.flip()
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Check if the input matches the correct answer
                        if self.input_text.strip().lower() == self.correct_answer.strip().lower():
                            self.running = False
                            print(self.input_text.strip().lower())
                            print("Correct answer!")
                            return True
                        else:
                            self.running = False
                            print("Incorrect answer.")
                            return False
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove last character from the input
                        self.input_text = self.input_text[:-1]
                    else:
                        # Add character to the input text
                        self.input_text += event.unicode

