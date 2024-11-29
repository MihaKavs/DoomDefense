import os
import pygame

#creates a sprite
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        base_path = os.path.dirname(__file__)
        sprite_path = os.path.join(base_path, ".." ,"assets", "sprites.png") 
        self.sprites = pygame.image.load(sprite_path)
        self.group = pygame.sprite.Group()
        self.bgPath = os.path.join(base_path, ".." ,"assets", "bg20.png")
        self.bg = pygame.image.load(self.bgPath)
        self.index = 0
        circle_path = os.path.join(base_path, ".." ,"assets", "bra.png")
        self.circles = pygame.image.load(circle_path)
        play_path = os.path.join(base_path, ".." ,"assets", "play.png")
        self.play = pygame.image.load(play_path)
        self.sprite_dict = {
            "pentagon": (15, 0, 87, 80),
            "hexagon": (123, 10, 95, 95),
            "square": (5, 129, 80, 80),
            "heart": (230, 0, 117, 115),
            "dollar": (210, 130, 80, 125),
        }
        self.circle_dict = {
            "blue-circle": (0, 0, 150, 150),
            "green-circle": (160, 0, 160, 150),
            "red-circle": (327, 0, 170, 150),
            "purple-circle": (0 , 160, 150,150),
            "black-circle": (160 , 158, 150, 150),
            "yellow-circle": (330, 158, 166, 150),
        }

    #actualy creates the sprite acording to values
    def create_sprite(self, x, y, width, height, atlas, pos=(0,0), scale=None, color=None):
        if atlas == 0:
            self.sprites.set_clip(pygame.Rect(x, y, width, height))
            image = self.sprites.subsurface(self.sprites.get_clip())
        else:
            self.circles.set_clip(pygame.Rect(x, y, width, height))
            image = self.circles.subsurface(self.circles.get_clip())
        if scale and color:
            image = pygame.transform.scale(image, scale)
            image.fill(color + (0,), None, pygame.BLEND_RGBA_ADD)
        elif scale:
            image = pygame.transform.scale(image, scale)
        elif color:
            image.fill(color + (0,), None, pygame.BLEND_RGBA_ADD)
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = image.get_rect(topleft=pos)
        sprite.index = self.index
        self.index += 1
        sprite.distance = 0
        sprite.radius = pos[0]
        return sprite
    
    #create sprite just adds the sprite to the group
    def add_sprite(self, name, pos, scale=None, color=None):
        atlas= 0
        if name in self.sprite_dict:
            (x, y, w, h) = self.sprite_dict.get(name)
        else:
            (x, y, w, h) = self.circle_dict.get(name)
            atlas = 1
        if scale and color:
            sprite = self.create_sprite(x, y, w, h, atlas, pos, scale, color)
        elif scale:
            sprite = self.create_sprite(x, y, w, h, atlas, pos, scale)
        elif color:
            sprite = self.create_sprite(x, y, w, h, atlas, pos, color)
        else:
            sprite = self.create_sprite(x, y, w, h, atlas, pos)
        sprite.name = name
        self.group.add(sprite)
        return sprite

    # removes from group
    def remove_sprite(self, sprite):
        self.group.remove(sprite)

    # draws everything in group
    def draw(self, screen):
        self.group.draw(screen)

    #draws only one (not used)
    def drawOne(self, screen, name, x, y ,scale=None):
        sprite = self.sprite_dict.get(name)

        if scale:
            scaled_immage = pygame.transform.scale(sprite.image, scale)
            screen.blit(scaled_immage, (x, y))
        else:
            screen.blit(sprite.image, (x, y))

    #returns sprites index
    def get_sprite_by_index(self, index):
        if index < 0 or index >= len(self.group):
            return None
        return list(self.group)[index]
    
    # for background drawing
    def get_bg(self):
        return self.bg
    
    #  for play button
    def get_play(self):
        return self.play
    
    # changes location of sprite
    def change_location(self, sprite, x, y):
        sprite.rect.topleft = (x, y)

    # invizible sprites to prevent tower placement on track   
    def create_inizible(self, pos, size):
        image = pygame.Surface(size, pygame.SRCALPHA)  
        image.fill((0, 0, 0, 0))
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = image.get_rect(topleft=pos)
        sprite.index = self.index
        self.index += 1
        sprite.distance = 0  
        self.group.add(sprite)

        

