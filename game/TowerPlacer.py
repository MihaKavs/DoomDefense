import pygame
class TowerPlacementManager:
    def __init__(self, money_manager, tower_manager, round_manager):
        self.money_manager = money_manager
        self.tower_manager = tower_manager
        self.round_manager = round_manager
        self.tower_costs = {
            "square": 100,
            "pentagon": 200,
            "hexagon": 300,
        }

    def handle_placement(self, name, pos):
        if pos[0] > 1100 or pos[0] < 150:
            return False

        # Define the tower's placement rectangle
        tower_rect = pygame.Rect(pos[0] - 50, pos[1] - 50, 100, 100)

        # Check for collisions with existing sprites or towers
        collision_detected = any(
            tower_rect.colliderect(sprite.rect)
            for sprite in self.round_manager.sprite_manager.sprite.group
        ) or any(
            tower_rect.colliderect(tower.sprite.rect)
            for tower in self.tower_manager.tower_list
        )

        if collision_detected:
            return False  # Placement failed due to collision

        # Check cost and attempt placement
        tower_cost = self.tower_costs.get(name)  # Default to 250 if name is invalid
        if self.money_manager.can_cpend_money(tower_cost):
            self.tower_manager.add_tower(name, pos[0] - 50, pos[1] - 50)
            self.money_manager.spend_money(tower_cost)
            return True  # Placement succeeded

        return False