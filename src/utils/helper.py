import random
from ..models.property import Player
from ..models.property import Property

def dice():
    ''' Dice Roll Method '''

    return random.randrange(1,6)


def player_queue(players):
    ''' Randomizing Player Queue Method'''

    while players is not []:
        queue = []

        chosen = random.choice(players)

        queue.append(chosen)
        players.remove(chosen)    


def create_players():
    ''' Creating Players Method '''

    list_players = []

    for x in range(0,3):
        list_players.append(Player('Player'+x, x))

    return list_players


def create_board():
    ''' Creating Board Method '''

    list_properties = []

    for x in range(0,20):
        if x == 0:
            list_properties.append(Property(0,0,100))
        else:
            list_properties.append(Property(10+x,10+x))

    return list_properties


def max_rounds_rule():
    ''' Rule of Rounds Method '''

    max_rounds = 1000

    return max_rounds
