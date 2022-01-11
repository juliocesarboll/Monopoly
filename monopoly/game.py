from utils.helper import dice
from utils.helper import player_queue
from utils.helper import player_queue
from utils.helper import create_board
from utils.helper import create_players
from utils.helper import max_rounds_rule
from utils.player_actions import buy
from utils.player_actions import rent
from utils.player_actions import bankrupt
from utils.player_actions import movement


def game():
    ''' Game Properly Method'''

    # Initializing return Object
    ret = {'player_behavior': None, 'rounds': 0, 'timeout': False}

    # Initializing the Players
    players_list = create_players()
    players_list = player_queue(players_list)

    # Initialize Properties
    properties_list = create_board()

    # Create Loop with Rounds and Win Rule
    for round in range(1, max_rounds_rule()+1):
        # Create Win condition
        if len(players_list) == 1:
            break

        # Player Action
        for player in players_list:

            # Call the movement action
            dice_roll = dice()
            movement(player, dice_roll, properties_list)

            property_stopped = properties_list[player.position]

            # Call Buy action
            if property_stopped.player_hold is None:
                if property_stopped.sell_value is not None:
                    buy(player, property_stopped)

            # Call Rent action
            else:
                if property_stopped.rent_value is not None:
                    rent(player, property_stopped)

            # Call Bankrupt action
            if bankrupt(player, properties_list):

                # Removing Player from the Player List
                players_list.remove(player)

    # Return values of the Game
    ret_list = []
    for player in players_list:
        match player.behavior:
            case 'Impulsivo':
                ret['player_behavior'] = 0           
            case 'Exigente':
                ret['player_behavior'] = 1
            case 'Cauteloso':
                ret['player_behavior'] = 2
            case 'Aleatorio':
                ret['player_behavior'] = 3

        ret['rounds'] = round
        if round >= max_rounds_rule(): 
            ret['timeout'] = True

        ret_list.append(ret)

    return ret_list
