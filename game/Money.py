class Money:
    def __init__(self, tower_manager, round_manager):
        self.tower_manager = tower_manager
        self.round_manager = round_manager
        self.money = 600  # Initial amount of money
        self.upgrade_cost = 0
        self.total_spent = 0

    # add money amount of poops
    def earn_money(self, amount):
        self.money += amount

    # sepend money by the amount 
    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            self.total_spent += amount
            return True
        return False
    
    # checks if enouhg money
    def can_cpend_money(self, amount):
        if self.money >= amount:
            return True
        return False

    def can_upgrade(self, dict, u):
        if(dict):
            damage, damageU = dict.get("damage")
            pierce, pierceU = dict.get("pierce")
            attack, attackU = dict.get("attack")
        if u == 1:
            self.upgrade_cost = damageU * 50 + 50
            return self.can_cpend_money(damageU * 50 + 50)
        elif u == 2:
            self.upgrade_cost = pierceU * 50 + 50
            return self.can_cpend_money(pierceU * 50 + 50)
        else:
            self.upgrade_cost = attackU * 50 + 50
            return self.can_cpend_money(attackU * 50 + 50)
