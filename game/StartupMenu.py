import pygame

class StartupMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.start_button = pygame.Rect(540, 250, 200, 50)
        self.exit_button = pygame.Rect(540, 350, 200, 50)
        self.name = ""
        self.input = pygame.Rect(940, 350, 200, 50)
        self.active = False

    def draw(self):
        # Fill the background with a color
        self.screen.fill((200, 200, 200))  # Light gray background
        
        # Display title
        title_text = self.font.render("Tower Defense", True, (255, 255, 255))
        self.screen.blit(title_text, (500, 100))  # Center title
        
        # Draw the buttons
        if self.active:
            pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)  # Green start button
        else:
            pygame.draw.rect(self.screen, (70, 70, 70), self.start_button) 
        pygame.draw.rect(self.screen, (255, 0, 0), self.exit_button)   # Red exit button
        pygame.draw.rect(self.screen, (50, 50, 50), self.input) 
        # Add button texts
        start_text = self.font.render("Start Game", True, (255, 255, 255))
        exit_text = self.font.render("Exit", True, (255, 255, 255))
        input_text = self.font.render("Input your name", True, (255, 255, 255))
        user_text = self.font.render(self.name, True, (255, 255, 255))
        # Center the text in the buttons
        self.screen.blit(start_text, (self.start_button.centerx - start_text.get_width() // 2, self.start_button.centery - start_text.get_height() // 2))
        self.screen.blit(exit_text, (self.exit_button.centerx - exit_text.get_width() // 2, self.exit_button.centery - exit_text.get_height() // 2))
        self.screen.blit(input_text, (self.input.centerx - 100 , self.input.centery- 100))
        self.screen.blit(user_text, (self.input.centerx - user_text.get_width() // 2, self.input.centery - user_text.get_height() // 2))

    def handle_click(self, pos):
        if self.start_button.collidepoint(pos):
            return "start"
        elif self.exit_button.collidepoint(pos):
            return "exit"
        return None

    def handle_menu(self):
        # Continuously draw the menu
        self.draw()  # Draw the menu elements
        pygame.display.flip()  # Update the display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                menu_selection = self.handle_click(pos)
                if menu_selection == "start" and self.active:
                    return "start"
                elif menu_selection == "exit":
                    return "exit"
            if event.type == pygame.KEYDOWN: # input your name
                if event.key == pygame.K_BACKSPACE: 
                    self.name = self.name[:-1]
                    if len(self.name) == 0:
                        self.active = False
                else: 
                    if len(self.name) <= 10:
                        self.name += event.unicode
                    self.active = True
        return None