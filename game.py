#!/usr/bin/env python3
from util import valid_rps_input, get_opponent_answer, evaluate_game, get_full_answers

def main():
    while True:
        play_game_input = input("Would you like to play Rock, Paper, Scissors? (Y | N)\n")
        if play_game_input.lower() == 'n':
            quit()
        elif play_game_input.lower() != 'y':
            print("\nPlease enter y or n")
        else:
            break

    print("\nFirst to win 3 games wins!\n")

    player_score = 0
    opponent_score = 0
    num_of_rounds = 0

    while num_of_rounds < 3:
        player_answer = input("Choose Rock, Paper, or Scissors (R | P | S)\n").lower()

        if not valid_rps_input(player_answer):
            print("\nPlease enter R, P, or S")
            continue
        
        opponent_answer = get_opponent_answer()
        
        result = evaluate_game(player_answer, opponent_answer)
        print()
        
        if result == 'win':
            print('You won')
            player_score += 1
        elif result == 'loss':
            print('You lost')
            opponent_score += 1
        else:
            print('Draw!')
            
        full_player_answer, full_opponent_answer = get_full_answers(player_answer, opponent_answer)
        
        print(f"You chose {full_player_answer} and your opponent chose {full_opponent_answer}\n")

        num_of_rounds += 1
        
    if player_score > opponent_score:
        print("You won the game!")
    elif player_score < opponent_score:
        print("You lost the game :(")
    else:
        print("Nobody won...")
        
if __name__ == '__main__':
    main()



