#!/usr/bin/env python3
from util import get_answers, evaluate_game

def run_game():
    player_score = 0
    opponent_score = 0
    num_of_rounds = 0
    
    print("\nFirst to win 3 games wins!\n")

    while num_of_rounds < 3:
        player_input = int(input("Choose Rock[0], Paper[1], or Scissors[2]\n"))

        if player_input < 0 or player_input > 2:
            continue
        
        player_answer, opponent_answer = get_answers(player_input)
        
        result = evaluate_game(player_answer, opponent_answer)
        
        print()
        
        if result == 'win':
            print('You won!')
            player_score += 1
        elif result == 'loss':
            print('You lost :(')
            opponent_score += 1
        else:
            print('Match was a draw')
        
        print(f"You chose {player_answer} and your opponent chose {opponent_answer}\n")
        
        num_of_rounds += 1

    if player_score > opponent_score:
        print("You won the game!")
    elif player_score < opponent_score:
        print("You lost the game :(")
    else:
        print("Nobody won...")




