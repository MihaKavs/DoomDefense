import time
from SpriteManager import SpriteManager
from DamageManager import DamageManager

class RoundManager:
    def __init__(self):
        self.sprite_manager = SpriteManager()  
        self.track_path = [(380, -40), (380, 550), (750, 550), (750, -40)]
        self.current_round = 0 
        self.active_enemies = []  
        self.round_in_progress = False
        self.last_spawn_time = 0
        self.did_exit = False
        self.upgrade_shown = False
        self.tierSpeed = {
            0: 2,
            1: 3,
            2: 3,
            3: 6,
            4: 5,
            5: 4
        }
        self.health_dict = {
            0: 1,
            1: 4,
            2: 8,
            3: 8,
            4: 6,
            5: 20
        }
        self.sprite_manager.initiateBasic()
        self.damage_manager = DamageManager()
        
    #spawns all enemies of the reound outside of range and screen
    def start_rounds(self, round_number):
        self.current_round = round_number
        self.sprite_manager.spawn_rounds(round_number)  # Populate sprite_queue
        self.round_in_progress = True
        enemy, tier, spacing = self.sprite_manager.sprite_queue[0]
        self.sprite_manager.sprite_queue.pop(0)  
        start_position = self.track_path[0]
        self.sprite_manager.sprite.change_location(enemy, *start_position)
        self.active_enemies.append((enemy, tier))  
        self.last_spawn_time = time.time() * 1000 

    # spawns enemy at the start of the track when the time has ellapsed
    def spawn_next_enemy(self):
        if self.sprite_manager.sprite_queue:
            current_time = time.time() * 1000  
            enemy, tier, spacing = self.sprite_manager.sprite_queue[0] 
            if current_time - self.last_spawn_time >= spacing:
                self.sprite_manager.sprite_queue.pop(0)  
                start_position = self.track_path[0]
                self.sprite_manager.sprite.change_location(enemy, *start_position)
                self.active_enemies.append((enemy, tier))  
                self.last_spawn_time = current_time  
            
    def endRound(self):
        self.round_in_progress = False


    #moves enemies through the track based on tier
    def update_enemy_positions(self):
        for enemy in self.active_enemies:
            speed = self.tierSpeed.get(enemy[1])
            if not hasattr(enemy[0], 'path_index'): #initializes enemy at the start
                enemy[0].path_index = 0
                enemy[0].xspeed = speed
                enemy[0].yspeed = 0
                enemy[0].trajectory = 2 #wich way its moving 0=up, 1=right, 2=down, 3=left
                enemy[0].speed = speed
                enemy[0].health = self.health_dict.get(enemy[1])
                pass 
            if enemy[0].health <= 0:
                self.active_enemies.remove(enemy)
                self.sprite_manager.sprite.remove_sprite(enemy)  # Remove sprite if dead
                continue
            trackPoint = self.track_path[enemy[0].path_index]
            changedTrajectory = False
            #trajectory change
            match enemy[0].trajectory:
                case 0:
                    if trackPoint[1] >= enemy[0].rect.centery - enemy[0].yspeed:
                        enemy[0].path_index += 1
                        changedTrajectory = True
                case 1:
                    if trackPoint[0] <= enemy[0].rect.centerx + enemy[0].xspeed:
                        enemy[0].path_index += 1
                        changedTrajectory = True
                case 2:
                    if trackPoint[1] <= enemy[0].rect.centery + enemy[0].yspeed:
                        enemy[0].path_index += 1
                        changedTrajectory = True
                case 3:
                    if trackPoint[0] >= enemy[0].rect.centerx - enemy[0].xspeed:
                        enemy[0].path_index += 1
                        changedTrajectory = True
                        
            #actualy changes trajectory
            if changedTrajectory:
                if enemy[0].path_index > len(self.track_path) - 1:
                    self.active_enemies.remove(enemy)
                    self.damage_manager.druct_hp(enemy[1])
                    self.sprite_manager.sprite.remove_sprite(enemy[0])
                    self.did_exit = True
                    if len(self.active_enemies) == 0:
                        self.endRound()
                elif trackPoint[0] != self.track_path[enemy[0].path_index][0]:
                    if trackPoint[0] > self.track_path[enemy[0].path_index][0]:
                        enemy[0].xspeed = -enemy[0].speed
                        enemy[0].yspeed = 0
                        enemy[0].trajectory = 3
                    else:
                        enemy[0].xspeed = enemy[0].speed
                        enemy[0].yspeed = 0
                        enemy[0].trajectory = 1
                else:
                    if trackPoint[1] > self.track_path[enemy[0].path_index][1]:
                        enemy[0].xspeed = 0
                        enemy[0].yspeed = -enemy[0].speed
                        enemy[0].trajectory = 0
                    else:
                        enemy[0].xspeed = 0
                        enemy[0].yspeed = enemy[0].speed
                        enemy[0].trajectory = 2
                        
            #changes position
            new_position = [enemy[0].rect.x + enemy[0].xspeed, enemy[0].rect.y + enemy[0].yspeed]
            self.sprite_manager.sprite.change_location(enemy[0], *new_position)

    #call every frame and update enemies
    def update(self):
        if self.round_in_progress:
            self.did_exit = False
            self.spawn_next_enemy()
            self.update_enemy_positions()
            # End the round if no enemies are left
            if not self.active_enemies and len(self.sprite_manager.sprite_queue) == 0:
                self.round_in_progress = False

    #start next round
    def next_round(self):
        self.current_round += 1
        self.start_rounds(self.current_round)

    def manage_upgrade(self):
        if self.upgrade_shown:
            self.sprite_manager.sprite.change_location(self.sprite_manager.upgrade, 0, -2000)
            self.upgrade_shown != self.upgrade_shown
        else:
            self.sprite_manager.sprite.change_location(self.sprite_manager.upgrade, 0, 200)
            self.upgrade_shown != self.upgrade_shown
        


