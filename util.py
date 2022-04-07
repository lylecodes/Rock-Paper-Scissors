from random import randint

def valid_rps_input(player_input):
    player_input = player_input.lower()
    if player_input == 'r':
        return True
    if player_input == 'p':
        return True
    if player_input == 's':
        return True
    return False

def get_opponent_answer():
    random_num = randint(1, 3)
    if random_num == 1:
        return 'r'
    elif random_num == 2:
        return 'p'
    else:
        return 's'
    
def evaluate_game(player_answer, opponent_answer):
    if player_answer == opponent_answer:
        return 'draw'
    elif player_answer == 'r' and opponent_answer == 's':
        return 'win'
    elif player_answer == 's' and opponent_answer == 'p':
        return 'win'
    else:
        return 'loss'
    
def get_full_answers(answer_1, answer_2):
    full_answers = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
    full_answer_1 = full_answers[answer_1]
    full_answer_2 = full_answers[answer_2]
    return [full_answer_1, full_answer_2]