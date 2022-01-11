from game import game as MonopolyGame

# Auxiliar method to do Percentage
def percentage(upper, behavior):
    quotient = upper / 300

    return {'behavior': behavior, 'number': quotient * 100}
     

if __name__ == "__main__":
    ''' Main Course Project '''
    # Results variables
    the_winner = None
    result_list = []
    behaviors_list = []
    sum_rounds = 0
    average_rounds = 0
    timeout_counter = 0
    random_behavior = 0
    cautious_behavior = 0
    demanding_behavior = 0
    impulsive_behavior = 0
    
    # Simulation
    for x in range(0, 300):
        game = MonopolyGame()
        result_list.append(game)

    # Interacting over Simulation
    for result in result_list:
        for obj in result:

            # Counting Behavior Winner
            match obj['player_behavior']:
                case 0:
                    impulsive_behavior += 1
                case 1:
                    demanding_behavior += 1
                case 2:
                    cautious_behavior += 1
                case 3:
                    random_behavior += 1

            # Sum of Rounds
            sum_rounds += obj['rounds']
            
            # Counting Timeouts
            if obj['timeout']:
                timeout_counter += 1
    
    #Calculating Average Rounds WITH ROUND
    average_rounds = sum_rounds / 300

    # Calculating percentage of Behaviors
    behaviors_list.append(percentage(impulsive_behavior, 'Impulsivo'))
    behaviors_list.append(percentage(demanding_behavior, 'Exigente'))
    behaviors_list.append(percentage(cautious_behavior, 'Cauteloso'))
    behaviors_list.append(percentage(random_behavior, 'Aleatorio'))

    # Choosing the better Behavior
    choosen = max(behaviors_list[0]['number'], behaviors_list[1]['number'], behaviors_list[2]['number'], behaviors_list[3]['number'])
    for behavior in behaviors_list:
        if behavior['number'] == choosen:
            the_winner = behavior['behavior']
                

    # OUTPUT
    print("[SIMULATION OUTPUT]")
    print(f"-> Quantas partidas terminam por time out (1000 rodadas): %s" % (timeout_counter))
    print(f"-> Quantos turnos em média demora uma partida: Com Arredondamento - %s | Sem Arredondamento %s" % (round(average_rounds), average_rounds))
    print(f"-> Qual a porcentagem de vitórias por comportamento dos jogadores: Impulsivo - %s | Exigente - %s | Cauteloso - %s | Aleatório - %s" % 
        (behaviors_list[0]['number'], behaviors_list[1]['number'], behaviors_list[2]['number'], behaviors_list[3]['number']))
    print("-> Qual o comportamento que mais vence: %s" % (the_winner))
