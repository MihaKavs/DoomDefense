import pygame

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.resume_button = pygame.Rect(540, 250, 200, 50)
        self.quit_button = pygame.Rect(540, 350, 200, 50)

    def draw(self):
        # Fill the background with a color to indicate pause
        self.screen.fill((0, 0, 0, 150))  # Semi-transparent black background

        # Display title
        title_text = self.font.render("Game Paused", True, (255, 255, 255))
        self.screen.blit(title_text, (520, 100))

        # Draw the buttons
        pygame.draw.rect(self.screen, (0, 255, 0), self.resume_button)  # Resume button
        pygame.draw.rect(self.screen, (255, 0, 0), self.quit_button)    # Quit button

        # Add button texts
        resume_text = self.font.render("Resume", True, (255, 255, 255))
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        
        self.screen.blit(resume_text, (self.resume_button.x + 30, self.resume_button.y + 10))
        self.screen.blit(quit_text, (self.quit_button.x + 55, self.quit_button.y + 10))

    def handle_click(self, pos):
        if self.resume_button.collidepoint(pos):
            return "resume"
        elif self.quit_button.collidepoint(pos):
            return "quit"
        return None