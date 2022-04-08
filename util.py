from random import randint

def prompt_user():
    while True:
        play_game_input = input("Would you like to play Rock, Paper, Scissors? (Y | N)\n")
        if play_game_input.lower() == 'n':
            quit()
        elif play_game_input.lower() != 'y':
            print("\nPlease enter y or n")
        else:
            break

def get_answers(player_input):
    options = ["Rock", "Paper", "Scissors"]
    random_num = randint(0, 2)
    return (options[player_input], options[random_num])

def evaluate_game(player_answer, opponent_answer):
    if player_answer == opponent_answer:
        return 'draw'
    elif player_answer == 'Rock' and opponent_answer == 'Scissors':
        return 'win'
    elif player_answer == 'Scissors' and opponent_answer == 'Paper':
        return 'win'
    else:
        return 'loss'