import random
from models.player import Player
from models.property import Property

def dice():
    ''' Dice Roll Method '''

    return random.randrange(1,6)


def player_queue(players):
    ''' Randomizing Player Queue Method'''

    queue = []
    while len(players):

        chosen = random.choice(players)
        queue.append(chosen)
        players.remove(chosen)

    return queue


def create_players():
    ''' Creating Players Method '''

    list_players = []

    for x in range(0,4):
        name = f'Player {x}'
        list_players.append(Player(name, 300, x))

    return list_players


def create_board():
    ''' Creating Board Method '''

    list_properties = []

    for x in range(0,21):
        if x == 0:
            list_properties.append(Property(None,None,100))
        else:
            list_properties.append(Property(150+(2 * x),50 + x))

    return list_properties


def max_rounds_rule():
    ''' Rule of Rounds Method '''

    max_rounds = 1000

    return max_rounds
