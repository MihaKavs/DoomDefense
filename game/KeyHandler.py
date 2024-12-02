import pygame
class KeyHandler:
    def __init__(self, tower_manager):
        self.tower_manager = tower_manager
        self.is_dragging = False
        self.dragging_sprite = None
        self.selected_tower_name = None

    # handles wich key is pressed
    def handle_keydown(self, key):
        if key == pygame.K_1:
            self.start_dragging("square")
        elif key == pygame.K_2:
            self.start_dragging("pentagon")
        elif key == pygame.K_3:
            self.start_dragging("hexagon")

    # starts dragging handling
    def start_dragging(self, name):
        self.is_dragging = True
        self.selected_tower_name = name
        self.dragging_sprite = self.tower_manager.get_tower_sprite(name)  # Get sprite for the selected tower

    # ends dragging handling
    def reset_dragging(self):
        self.is_dragging = False
        self.dragging_sprite = None
        self.selected_tower_name = None