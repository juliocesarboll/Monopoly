import random
from utils.helper import dice
from utils.helper import player_queue
from utils.helper import player_queue
from utils.helper import create_board
from utils.helper import create_players
from utils.helper import max_rounds_rule


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

            else:
                player.position = final_position

            # Create Buy logic
            if properties_list[player.position].player_hold is None:
                
                # Always buy
                if player.behavior == 'Impulsivo':  
                    player.money -= properties_list[player.position].sell_value
                    properties_list[player.position].player_hold = player
                
                # Rent value need be higher $50
                elif player.behavior == 'Exigente':
                    if properties_list[player.position].rent_value > 50:
                        player.money -= properties_list[player.position].sell_value
                        properties_list[player.position].player_hold = player

                # Player money need be at least 80 after buying
                elif player.behavior == 'Cauteloso':
                    after_buy = player.money - properties_list[player.position].sell_value

                    if after_buy >= 80:
                        player.money = after_buy
                        properties_list[player.position].player_hold = player

                # Player randomly buy or not
                else:
                    dice_throw = random.randrange(0,1)
                    
                    if dice_throw == 1:
                        player.money -= properties_list[player.position].sell_value
                        properties_list[player.position].player_hold = player

            # Create Rent logic
            else:
                after_rent = player.money - properties_list[player.position].rent_value
 
                if after_rent < 0:

                    # Paying as much as possible
                    player_holder = properties_list[player.position].player_holder
                    player_holder.money += player.money

                    # Setting Bankrupt to further logic
                    player.money = -1

            # Create Bankrupt logic
            if player.money < 0:

                # Removing all properties from the Player
                for property in properties_list:
                    if property.player_hold == player:
                        property.player_hold = None

                # Removing Player from the Player List
                players_list.remove(player)

    #TODO: Pytest for final results


if __name__ == "__main__":
    ''' Main Course Project '''

    game()