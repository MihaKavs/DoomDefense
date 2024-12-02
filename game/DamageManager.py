

class DamageManager:
    def __init__(self):
        self.hp = 100
        self.hp_deduction = {
            0: 1,
            1: 2,
            2: 3,
            3: 3,
            4: 5,
            5: 15
        }
        pass
    
    def druct_hp(self, tier):
        self.hp -= self.hp_deduction.get(tier)
        if(self.hp <= 0):
            return 0
        else:
            return self.hp
        # TODO when all lives lost end game and save score
        
        