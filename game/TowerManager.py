from Sprite import Sprite
from TowerTypes import Rectangle
from TowerTypes import Pentagon
from TowerTypes import Hexagon

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

       