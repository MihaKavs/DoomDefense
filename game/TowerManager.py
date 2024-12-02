from Sprite import Sprite
from TowerTypes import Rectangle
from TowerTypes import Pentagon
from TowerTypes import Hexagon
import pygame

#manages tower behaviour
class TowerManager:
    def __init__(self, screen):
        self.sprite = Sprite()
        self.tower_list = []
        self.poppedAmount = 0
        self.screen = screen

    # creating a new Tower
    def add_tower(self, name, x, y):
        if name == "square":
            tower = Rectangle(x, y, self.screen)
        elif name == "pentagon":
                tower = Pentagon(x, y, self.screen)
        elif name == "hexagon":
                tower = Hexagon(x, y, self.screen)
        else:
                raise ValueError("Unknown tower type: " + name)
            
        tower.sprite = self.sprite.add_sprite(name, (x, y), (100, 100))
        self.tower_list.append(tower)

    # gets lase in list
    def getLastTower(self):
        tower = self.tower_list[-1] 
        return tower.sprite

    # returns the sprite
    def get_tower_sprite(self, name):
        return self.sprite.add_sprite(name, (-1000, -1000), (100, 100)).image
    
    # manages towers attack
    def attack_enemies(self, active_enemies):
        self.poppedAmount = 0
        for tower in self.tower_list:
            if active_enemies: 
                tower.can_attack(active_enemies)
                self.poppedAmount += tower.popped
                
    def draw_lines(self):
        for tower in self.tower_list:
            tower.draw_lines()

    def draw_radiuses(self, screen):
        for tower in self.tower_list:
            screen.blit(tower.sprite.image, tower.sprite.rect.topleft)
            pygame.draw.rect(screen, "red", tower.sprite.rect, 3)

            # Draw the tower's attack radius
            radius, position = tower.get_radius()
            pygame.draw.circle(
                screen, 
                (0, 255, 0),  # Green color
                (int(position[0] + 50), int(position[1] + 50)),  # Center of the tower
                radius,  # Radius size
                1  # Thickness of the circle
            )

    def update_towers(self, active_enemies, screen):
        self.attack_enemies(active_enemies)
        self.draw_radiuses(screen)
        self.sprite.draw(screen)
        self.draw_lines()



       