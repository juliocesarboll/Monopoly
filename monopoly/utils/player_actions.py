import random

def movement(player, dice_roll, properties_list):
    ''' Movement Action of the Player on Board '''

    final_position = player.position + dice_roll

    if final_position == 21:
        player.position = 0
        
        # Bonus Money logic
        player.money = bonus_money(player, properties_list)

    elif final_position > 21:
        relative_position = final_position - 21
        player.position = relative_position

        # Bonus Money logic
        player.money = bonus_money(player, properties_list)

    else:
        player.position = final_position


def buy(player, property):
    ''' Buy Action '''

    match player.behavior:
        
        # Always buy
        case 'Compulsivo':
            player.money -= property.sell_value
            property.player_hold = player

        # Rent value need be higher $50
        case 'Exigente':
            if property.rent_value > 50:
                player.money -= property.sell_value
                property.player_hold = player
    
        # Player money need be at least 80 after buying
        case 'Cauteloso':
            after_buy = player.money - property.sell_value

            if after_buy >= 80:
                player.money = after_buy
                property.player_hold = player

        # Player randomly buy or not
        case 'Aleatorio':
            dice_throw = random.randrange(0,1)
            
            if dice_throw == 1:
                player.money -= property.sell_value
                property.player_hold = player


def rent(player, property):
    ''' Rent Action '''

    after_rent = player.money - property.rent_value
 
    if after_rent < 0:

        # Paying as much as possible
        player_holder = property.player_holder
        player_holder.money += player.money

        # Setting Bankrupt to further logic
        player.money = -1
    else:

        # Pay full price
        player_holder = property.player_hold
        player_holder.money += property.rent_value

        player.money -= property.rent_value


def bankrupt(player, properties_list):
    ''' Bankrupt Action '''

    is_bankrupt = False

    if player.money < 0:

        # Removing all properties from the Player
        for property in properties_list:
            if property.player_hold == player:
                property.player_hold = None

        is_bankrupt = True

    return is_bankrupt


def bonus_money(player, properties_list):
    ''' Add Bonus Money to the Player '''

    player.money += properties_list[0].bonus_value
