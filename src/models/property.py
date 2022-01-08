class Property:
    sell_value = None
    rent_value = None
    bonus_value = None
    player_hold = None


    def __init__(self, sell, rent, bonus=None, hold=None):
        self.sell_value = sell
        self.rent_value = rent
        self.bonus_value = bonus
        self.player_hold = hold