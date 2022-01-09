from .utils.helper import dice
from .utils.helper import player_queue
from .utils.helper import create_board
from .utils.helper import create_players
from .utils.helper import max_rounds_rule


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

            # Create Movement logic
            dice_roll = dice()
            final_position = player.position + dice_roll

            if final_position == 21:
                player.position = 0
                
                # Bonus Money logic
                player.money += properties_list[0].bonus_value

            elif final_position > 21:
                relative_position = final_position - 21
                player.position = relative_position

                # Bonus Money logic
                player.money += properties_list[0].bonus_value

                #TODO: Create Buy logic
                #TODO: Create Rent logic
            else:
                player.position = final_position

                #TODO: Create Buy logic
                #TODO: Create Rent logic

            # Create Bankrupt logic
            if player.money < 0:
                players_list.remove(player)


        

    #TODO: Pytest for final results


if __name__ == "__main__":
    ''' Main Course Project '''

    game()