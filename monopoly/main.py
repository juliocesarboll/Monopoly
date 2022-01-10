import random
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

    # Initializing the Players
    players_list = create_players()
    players_list = player_queue(players_list)

    # Initialize Properties
    properties_list = create_board()

    # Create Loop with Rounds and Win Rule
    for round in range(1, max_rounds_rule()):

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
                buy(player, property_stopped)

            # Call Rent action
            else:
                rent(player, property_stopped)

            # Call Bankrupt action
            if bankrupt(player, properties_list):

                # Removing Player from the Player List
                players_list.remove(player)


if __name__ == "__main__":
    ''' Main Course Project '''

    #TODO: Pytest for final results
    # game()