import pygame
import json

class Leaderboard:
    def __init__(self, screen, file_name="leaderboard.json"):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.file_name = file_name
        self.scores = []
        self.load_scores()
        self.restart_button = pygame.Rect(900, 200, 200, 50)
        self.exit_button = pygame.Rect(900, 300, 200, 50)

    # loads scores from fole or make an empty list
    def load_scores(self):
        try:
            with open(self.file_name, "r") as f:
                self.scores = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.scores = []

    # saves to file
    def save_scores(self):
        with open(self.file_name, "w") as f:
            json.dump(self.scores, f)

    # adds the score and keeps it sorted
    def add_score(self, name, round_reached, money_spent):
        self.scores.append({"name": name, "round": round_reached, "money_spent": money_spent})
        
        # Sort by round (higher is better), then by money_spent (lower is better)
        self.scores = sorted(self.scores, key=lambda x: (-x["round"], x["money_spent"]))
        
        # only 10 scores
        self.scores = self.scores[:10]
        self.save_scores()

    # draws on screen
    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill with black background
        title_text = self.font.render("Leaderboard", True, (255, 255, 255))
        self.screen.blit(title_text, (100, 50))
        pygame.draw.rect(self.screen, (0, 255, 0), self.restart_button)
        restart_text = self.font.render("Restart", True, (255,255,255))
        self.screen.blit(restart_text,(self.restart_button.x + 30, self.restart_button.y + 10))
        pygame.draw.rect(self.screen, (0, 255, 0), self.exit_button)
        exit_text = self.font.render("Exit", True, (255,255,255))
        self.screen.blit(exit_text,(self.exit_button.x + 30, self.exit_button.y + 10))

        y_offset = 150
        for entry in self.scores:
            score_text = self.font.render(f"{entry['name']} - Round: {entry['round']} | Money Spent: {entry['money_spent']}", True, (255, 255, 255))
            self.screen.blit(score_text, (100, y_offset))
            y_offset += 60  # Space out the scores
        pygame.display.flip()

    def handle_click(self, pos):
        """Handle any clicks (e.g., for returning to the main menu)."""
        if self.exit_button.collidepoint(pos):
            return "exit"
        elif self.restart_button.collidepoint(pos):
            return "restart"
        else:
            return None