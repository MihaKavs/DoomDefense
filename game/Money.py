class Money:
    def __init__(self, tower_manager, round_manager):
        self.tower_manager = tower_manager
        self.round_manager = round_manager
        self.money = 600  # Initial amount of money

    def earn_money(self, amount):
        """Add money when an enemy is popped."""
        self.money += amount

    def spend_money(self, amount):
        """Spend money on towers if enough funds are available."""
        if self.money >= amount:
            self.money -= amount
            return True
        return False
    
    def can_cpend_money(self, amount):
        if self.money >= amount:
            return True
        return False
