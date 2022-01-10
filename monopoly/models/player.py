class Player:
    ''' Player Class '''

    name = None
    money = None
    behavior = None
    position = None


    def __init__(self, name, behavior):
        ''' Initializing Player Class '''

        self.name = name
        self.money = 300
        if behavior == 0:
            self.behavior = 'Compulsivo'
        elif behavior == 1:
            self.behavior = 'Exigente'
        elif behavior == 2:
            self.behavior = 'Cauteloso'
        elif behavior == 3:
            self.behavior = 'Aleatorio'
        self.position = 0
