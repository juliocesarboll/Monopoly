class Player:
    name = None
    money = None
    behavior = None
    list_property = None


    def __init__(self, name, behavior):
        self.name = name
        self.money = 300
        self.behavior = behavior
        self.list_property = []
