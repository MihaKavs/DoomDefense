import pygame
from RoundManager import RoundManager
from TowerManager import TowerManager
from Ui import Ui
from Money import Money
from AudioManager import AudioManager
from TowerPlacer import TowerPlacementManager
from KeyHandler import KeyHandler
from StartupMenu import StartupMenu
from PauseMenu import PauseMenu
from Leaderboard import Leaderboard

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

start_menu = StartupMenu(screen)

game_started = False
running = False
while not game_started:
    menu_result = start_menu.handle_menu()
    if menu_result == "start":
        game_started = True
        running = True
    elif menu_result == "exit":
        game_started = False
        break
    else:
        game_started = False
    


roundNumber = 1
round_manager = RoundManager()
round_manager.start_rounds(roundNumber)
roundNumber += 1
pygame.time.delay(100)
temp_immage = pygame.transform.scale(round_manager.sprite_manager.play, (80,80))

tower_manager = TowerManager(screen)
isDragging = False

name = ""
dragging_sprite = None 
selected_tower = None
upgrades = {}
money_manager = Money(tower_manager, round_manager)

Ui_manager = Ui(round_manager, money_manager, screen)

audio_manager = AudioManager()
audio_manager.play_music()

tower_placement_manager = TowerPlacementManager(money_manager, tower_manager, round_manager)

key_handler = KeyHandler(tower_manager)

pause_menu = PauseMenu(screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:   
            pos = pygame.mouse.get_pos()
            if key_handler.is_dragging:
                if tower_placement_manager.handle_placement(key_handler.selected_tower_name, pos):
                    key_handler.reset_dragging()
                else:
                    key_handler.reset_dragging()

            if pos[0] > 1200 and pos[1] > 620 and round_manager.round_in_progress == False:
                if len(round_manager.sprite_manager.rounds) < roundNumber:
                    # TODO save the score and print it
                    running = False
                    break
                round_manager.start_rounds(roundNumber)
                roundNumber += 1
            elif pos[0] < 150 and pos[1] > 200 and pos[1] < 500:
                u = Ui_manager.get_upgrade(pos)
                if money_manager.can_upgrade(selected_tower.get_upgrades(), u):
                    selected_tower.upgrade_tower(u)
                    money_manager.spend_money(money_manager.upgrade_cost)

            elif key_handler.paused:
                clicked = pause_menu.handle_click(pos)
                if clicked == None:
                    break
                elif clicked == "quit":
                    running = False
                else:
                    key_handler.paused = False
            else:
                mouse_rect = pygame.Rect(pos[0], pos[1], 1, 1)
                for tower in tower_manager.tower_list:
                    if mouse_rect.colliderect(tower.sprite.rect):
                        upgrades = tower.get_upgrades()
                        round_manager.manage_upgrade()
                        selected_tower = tower


        elif event.type == pygame.KEYDOWN:
            key_handler.handle_keydown(event.key)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(round_manager.sprite_manager.bg, (0, 0))
    if upgrades: 
        upgrades = selected_tower.get_upgrades()
    # Update and draw game elements
    if not key_handler.paused:
        round_manager.update()
        tower_manager.update_towers(round_manager.active_enemies, screen)
        Ui_manager.update_values()
        round_manager.sprite_manager.sprite.draw(screen)
        Ui_manager.print_shit()
        Ui_manager.print_upgrades(upgrades)
        
        money_manager.earn_money(tower_manager.poppedAmount)
    else:
        pause_menu.draw()

    audio_manager.update_music_loop(tower_manager.poppedAmount)

    # Display the dragging sprite following the mouse
    if key_handler.is_dragging and key_handler.dragging_sprite and not key_handler.paused:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(key_handler.dragging_sprite, (mouse_pos[0] - 50, mouse_pos[1] - 50))

    # Display the start button if no round is in progress
    if not round_manager.round_in_progress:
        screen.blit(temp_immage, (1200, 620))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

leaderboard = Leaderboard(screen)
running = True
while running:
    leaderboard.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            click = leaderboard.handle_click(pos)
            if click is not None:
                if click == "exit":
                    running = False
                elif click == "restart":
                    pass

pygame.quit()



