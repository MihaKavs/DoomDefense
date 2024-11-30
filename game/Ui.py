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

    def print_upgrades(self, dict):
        if(dict):
            damage, damageU = dict.get("damage")
            pierce, pierceU = dict.get("pierce")
            attack, attackU = dict.get("attack")
            self.screen.blit(self.my_font.render("Damage", False, (0,0,0)), (10, 210))
            self.screen.blit(self.my_font.render("Pierce", False, (0,0,0)), (10, 310))
            self.screen.blit(self.my_font.render("AttSpeed", False, (0,0,0)), (10, 410))
            self.screen.blit(self.my_font.render(str(damageU * 50 + 50), False, (0,0,0)), (10, 250))
            self.screen.blit(self.my_font.render(str(pierceU * 50 + 50), False, (0,0,0)), (10, 350))
            self.screen.blit(self.my_font.render(str(attackU * 50 + 50), False, (0,0,0)), (10, 450))

    def get_upgrade(self, pos):
        if pos[1] < 300:
            return 1
        elif pos[1] > 400:
            return 3
        else:
            return 2
        



        

