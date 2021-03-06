import json
class Player:
    ''' Player Class '''

    name = None
    money = None
    behavior = None
    position = None


    def __init__(self, name, money, behavior):
        ''' Initializing Player Class '''

        self.name = name
        self.money = money
        match behavior:
            case 0:
                self.behavior = 'Impulsivo'
            case 1:
                self.behavior = 'Exigente'
            case 2:
                self.behavior = 'Cauteloso'
            case 3:
                self.behavior = 'Aleatorio'
        self.position = 0

    def __repr__(self):
        return json.dumps({'Name': self.name, 'Money': self.money, 'Behavior': self.behavior, 'Position': self.position})
