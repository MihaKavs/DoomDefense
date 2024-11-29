import pygame

# prints the texts 
class Ui():
    def __init__(self, round_manager, money_manager, screen):
        pygame.font.init()
        self.round_manager = round_manager
        self.money_manager = money_manager
        self.screen = screen
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render(str(self.round_manager.damage_manager.hp), False, (0, 10, 0))

    def get_hpText(self):
        return self.text_surface
    
    def update_values(self):
        self.text_surface = self.my_font.render(str(self.round_manager.damage_manager.hp), False, (0, 0, 0))

    def get_moneyText(self):
        return self.my_font.render(str(self.money_manager.money), False, (0, 0, 0))
    
    def print_shit(self):
        self.screen.blit(self.my_font.render("100", False, (0,0,0)), (1210, 140))
        self.screen.blit(self.my_font.render("200", False, (0,0,0)), (1210, 250))
        self.screen.blit(self.my_font.render("300", False, (0,0,0)), (1210, 350))
        self.screen.blit(self.my_font.render(str(self.money_manager.money), False, (0,0,0)), (1200, 12))
        self.screen.blit(self.my_font.render(str(self.round_manager.damage_manager.hp), False, (0,0,0)), (1200, 50))

        

