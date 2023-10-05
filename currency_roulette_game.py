from forex_python.converter import CurrencyRates
import random


def get_money_interval():
    c = CurrencyRates()
    amount = random.randint(1, 100)
    return c.convert('ILS', 'USD', amount), amount


def get_guess_from_user(generated_num):
    guess_is_not_a_number = True
    while guess_is_not_a_number:
        user_guess = input(f'How much is {round(generated_num, 2)} dollars in ILS? ')
        if user_guess.isdigit():
            return int(user_guess)
        print('Guess in not valid, try again')


def is_list_equal(generated_num, user_guess, difficulty):
    if (generated_num - user_guess) == 5 - difficulty or (generated_num - user_guess) == (5 - difficulty) * (-1):
        return True
    return False


def play(difficulty):
    generated_currency = get_money_interval()
    return is_list_equal(generated_currency[1], get_guess_from_user(generated_currency[0]), difficulty)






