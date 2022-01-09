from .utils.helper import dice
from .utils.helper import player_queue
from .utils.helper import create_board
from .utils.helper import create_players
from .utils.helper import max_rounds_rule


def game():
    ''' Game Properly Method'''

    # Initializing the Game
    players_list = create_players()
    players_list = player_queue(players_list)

    #TODO: Initialize Properties
    #TODO: Create Loop with Rounds Rule
    #TODO: Create Buy logic
    #TODO: Create Rent logic
    #TODO: Create Movement logic
    #TODO: Create Bankrupt logic
    #TODO: Create Win condition
    #TODO: Bonus $100 logic
    #TODO: Pytest for final results


if __name__ == "__main__":
    ''' Main Course Project '''

    game()