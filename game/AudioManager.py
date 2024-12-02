import pygame
import os

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        base_path = os.path.dirname(__file__)
        pop = os.path.join(base_path, ".." ,"assets", "pop.mp3") 
        self.pop_effect = pygame.mixer.Sound(pop)
        hypnosis = os.path.join(base_path, ".." ,"assets", "hypnosis.mp3") 
        chokehold = os.path.join(base_path, ".." ,"assets", "chokehold.mp3") 
        self.music_playlist = [hypnosis, chokehold]
        self.current_music_index = 0
        self.volume = 0.1
        self.set_volume(self.volume)

    #plays pop
    def play_pop(self):
        self.pop_effect.play()

    # play current music and loop through all tracks
    def play_music(self):
        # Load the current track
        current_track = self.music_playlist[self.current_music_index]
        pygame.mixer.music.load(current_track)
        pygame.mixer.music.play(-1)  # Loop the track indefinitely
        print(f"Playing music: {current_track}")

    # next track in the playlist
    def next_track(self):
        pygame.mixer.music.stop()  # Stop current music
        self.current_music_index = (self.current_music_index + 1) % len(self.music_playlist)
        self.play_music()

    # stop background music
    def stop_music(self):
        pygame.mixer.music.stop()

    # when track stops play next
    def update_music_loop(self, pops):
        if not pygame.mixer.music.get_busy():  # Check if the current track has stopped
            self.next_track()
        if pops > 0:
            self.play_pop()

    # sets volume    
    def set_volume(self, volume):
        self.volume = max(0, min(volume, 1))  
        pygame.mixer.music.set_volume(self.volume)  
        self.pop_effect.set_volume(self.volume) 