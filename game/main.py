import pygame
from RoundManager import RoundManager
from TowerManager import TowerManager
from Ui import Ui
from Money import Money

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()



roundNumber = 1
round_manager = RoundManager()
round_manager.start_rounds(roundNumber)
roundNumber += 1
pygame.time.delay(100)
temp_immage = pygame.transform.scale(round_manager.sprite_manager.play, (80,80))

tower_manager = TowerManager(screen)
isDragging = False
running = True
name = ""
dragging_sprite = None 

money_manager = Money(tower_manager, round_manager)

Ui_manager = Ui(round_manager, money_manager, screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if isDragging:
                if pos[0] > 1100:
                    pass
                else:
                    tower_rect = pygame.Rect(pos[0] - 50, pos[1] - 50, 100, 100)
                    collision_detected = False
                    for sprite in round_manager.sprite_manager.sprite.group:
                        if tower_rect.colliderect(sprite.rect):
                            collision_detected = True
                            break
                    for tower in tower_manager.tower_list:
                        if tower_rect.colliderect(tower.sprite.rect):
                            collision_detected = True
                            break
                    tower_cost = 0
                    if name == "square":
                        tower_cost = 100
                    elif name == "hexagon":
                        tower_cost = 400
                    else:
                        tower_cost = 250
                    if money_manager.can_cpend_money(tower_cost) and collision_detected == False:
                        tower_manager.add_tower(name, pos[0] - 50, pos[1] - 50)
                        money_manager.spend_money(tower_cost)
                isDragging = False
                dragging_sprite = None  

            if pos[0] > 1200 and pos[1] > 620 and round_manager.round_in_progress == False:
                round_manager.start_rounds(roundNumber)
                roundNumber += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                isDragging = True
                name = "square"
                dragging_sprite = tower_manager.get_tower_sprite(name)  # Get sprite for selected tower
            elif event.key == pygame.K_2:
                isDragging = True
                name = "pentagon"
                dragging_sprite = tower_manager.get_tower_sprite(name)
            elif event.key == pygame.K_3:
                isDragging = True
                name = "hexagon"
                dragging_sprite = tower_manager.get_tower_sprite(name)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(round_manager.sprite_manager.bg, (0, 0))

    # Update and draw game elements
    round_manager.update()
    tower_manager.attack_enemies(round_manager.active_enemies)
    Ui_manager.update_values()
    round_manager.sprite_manager.sprite.draw(screen)
    tower_manager.sprite.draw(screen)
    money_manager.earn_money(tower_manager.poppedAmount)
    tower_manager.draw_lines()
    Ui_manager.print_shit()


    # Draw towers with borders around their rects
    for tower in tower_manager.tower_list:
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

    # Display the dragging sprite following the mouse
    if isDragging and dragging_sprite:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(dragging_sprite, (mouse_pos[0] - 50, mouse_pos[1] - 50))

    # Display the start button if no round is in progress
    if not round_manager.round_in_progress:
        screen.blit(temp_immage, (1200, 620))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
