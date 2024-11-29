from Tower import Tower

class Rectangle(Tower):
    def __init__(self, x, y, screen):
        super().__init__(
            name="Rectangle", 
            x=x, 
            y=y, 
            damage=1, 
            attack_speed=1.0, 
            pierce=2, 
            radius=100,
            screen = screen
        ) 

class Pentagon(Tower):
    def __init__(self, x, y, screen):
        super().__init__(
            name="Rectangle", 
            x=x, 
            y=y, 
            damage=1, 
            attack_speed=1.5, 
            pierce=1, 
            radius=300,
            screen = screen
        )

class Hexagon(Tower):
    def __init__(self, x, y, screen):
        super().__init__(
            name="Hexagon",  
            x=x, 
            y=y, 
            damage=5, 
            attack_speed=1.0, 
            pierce=2, 
            radius=200,
            screen = screen
        ) 

        