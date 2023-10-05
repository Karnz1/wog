import time
import random

import Utils
from Utils import screen_cleaner

def generate_sequence(difficulty):
    arr = []
    for i in range(difficulty):
        arr.append(random.randint(1, 101))
    return arr


def get_list_from_user(difficulty, generated_numbers):
    # display numbers to user
    for j in range(difficulty):
        print(generated_numbers[j], end=" ")
    time.sleep(0.7)
    # clear screen
    Utils.screen_cleaner()
    # get user's guess
    arr = []
    for i in range(difficulty):
        guess_is_not_a_number = True
        while guess_is_not_a_number:
            num = input("guess a number: ")
            if num.isdigit():
                arr.append(int(num))
                guess_is_not_a_number = False
    return arr


def is_list_equal(list1, list2):
    lists_match = True
    for item in list1:
        if item not in list2:
            lists_match = False
            break
    return lists_match


def play(difficulty):
    generated_nums = generate_sequence(difficulty)
    return is_list_equal(generated_nums, get_list_from_user(difficulty, generated_nums))

