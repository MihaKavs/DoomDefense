from Sprite import Sprite
import csv, os
import pygame

#manages sprites and makes a queue for circles
class SpriteManager():
    def __init__(self):
        base_path = os.path.dirname(__file__)
        csv_path = os.path.join(base_path, ".." ,"assets", "rounds.csv") 
        self.rounds = {}
        self.sprite = Sprite()
        self.sprite_queue = []
        self.menue = []
        
        with open(csv_path, newline='')as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                round_key = row['round']
                if round_key in self.rounds:
                    self.rounds[round_key].append(row)
                else:
                    self.rounds[round_key] = [row]
        print(len(self.rounds))

    # spawns the round based on rounds.csv
    def spawn_rounds(self, round):
        round_values = self.rounds.get(str(round))
        for line in round_values:
            amount = int(line.get('amount'))
            spacing = int(line.get('spacing'))
            tier = int(line.get('tier'))
            type = self.get_tier(tier)
            for i in range(amount):
                self.sprite_queue.append([(self.sprite.add_sprite(type, (-1100, -200), (80,80))), tier, spacing])

    #returns tier
    def get_tier(self, tier):
        tier_list = list(self.sprite.circle_dict.keys())
        return tier_list[tier]

    # draws the basic ui elements
    def initiateBasic(self):
        windowSize = pygame.display.get_window_size()
        self.sprite.add_sprite("dollar", (windowSize[0]-150,20), (40,40))
        self.sprite.add_sprite("heart", (windowSize[0]-150, 60), (40,40))
        self.bg = self.sprite.get_bg()
        self.play = self.sprite.get_play()
        self.upgrade = self.sprite.create_indipendent((0, -2000), (150, 300))
        
        self.menue.append(self.sprite.add_sprite("square", (windowSize[0]-110, 150),(100,100)))
        self.menue.append(self.sprite.add_sprite("pentagon", (windowSize[0]-110, 255),(100,100)))
        self.menue.append(self.sprite.add_sprite("hexagon", (windowSize[0]-110, 360),(100,100)))
        self.sprite.create_inizible((390, 0), (50, 590))
        self.sprite.create_inizible((390, 510), (400, 50))
        
    # if needed to add sprite
    def add_sprite(self, name, position):
        sprite = Sprite()
        sprite.add_sprite(name, position)
        self.sprite_queue.append(sprite)
