import pygame

# tower placement and atacking 
class Tower:
    def __init__(self, name, x, y, damage=0, attack_speed=0, pierce=0, radius=0, screen=None):
        self.name = name
        self.position = (x, y)
        self.activated = True
        self.damage = damage
        self.attack_speed = attack_speed
        self.pierce = pierce
        self.radius = radius
        self.upgrade = 0
        self.last_attack_time = 0
        self.popped = 0
        self.screen = screen
        self.lines = []


    def place_tower(self, x, y):
        # Update sprite position through SpriteManager
        self.sprite_manager.change_location(self.name, x, y)

    def set_tower(self, x, y):
        self.place_tower(x, y)
        self.activated = True

    def can_attack(self, active_enemy_list):
        enemies = []
        for enemy in active_enemy_list:
            e = enemy[0]
            enemy_pos = e.rect.center
            tower_pos = (self.position[0] + 50, self.position[1] + 50)
            distance = ((enemy_pos[0] - tower_pos[0]) ** 2 + (enemy_pos[1] - tower_pos[1]) ** 2) ** 0.5
            if distance - 40 <= self.radius:
                enemies.append(e)
        self.attack(enemies)

    def attack(self, active_enemy_list):
        current_time = pygame.time.get_ticks() / 1000  # Get time in seconds
        self.popped = 0    
        if current_time - self.last_attack_time >= self.attack_speed: 
               
            pierce = self.pierce  
            for enemy in active_enemy_list:
                if pierce > 0: 
                    self.popped += min(enemy.health, self.damage)
                    enemy.health -= self.damage
                    self.lines.append({
                        "tower_pos": self.position,
                        "enemy_pos": enemy.rect.center,
                        "duration": 0.3 + current_time
                    })
                    pierce -= 1  
                else:
                    break  

            self.last_attack_time = current_time

    def get_radius(self):
        return self.radius, self.position
    
    def draw_lines(self):
        current_time = pygame.time.get_ticks() / 1000  # Get time in seconds
        for line in self.lines[:]:
            if current_time > line["duration"]:
                self.lines.remove(line)
            else:
                pygame.draw.line(self.screen, "black", line["tower_pos"], line["enemy_pos"])

            