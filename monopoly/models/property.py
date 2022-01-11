import json
class Property:
    ''' Property Class '''

    sell_value = None
    rent_value = None
    bonus_value = None
    player_hold = None


    def __init__(self, sell, rent, bonus=None, hold=None):
        ''' Initializing Property Class '''

        self.sell_value = sell
        self.rent_value = rent
        self.bonus_value = bonus
        self.player_hold = hold

    def __repr__(self):
        return json.dumps({'Sell Value': self.sell_value, 'Rent Value': self.rent_value, 'Bonus Value': self.bonus_value, 'Player Hold': self.player_hold})
