import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        user_number_pick = int(input(f'choose a number between 1 and {difficulty}: '))
        if 1 <= user_number_pick <= difficulty:
            return user_number_pick


def compare_results(secret_number, user_number_choice):
    if secret_number == user_number_choice:
        print("You guessed correctly")
        return True
    else:
        print('You picked the wrong number')
        return False


def play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))

