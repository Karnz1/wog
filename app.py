import memory_game, currency_roulette_game, guess_game


def welcome():
    name = input("Enter your name: ")
    print(f'Hi {name} and welcome to the World of Games: The Epic Journey')


def match_game(game, difficulty_level):
    if game == 1:
        return memory_game.play(difficulty_level)
    elif game == 2:
        return guess_game.play(difficulty_level)
    elif game == 3:
        return currency_roulette_game.play(difficulty_level)


def start_play():
    game_options = [1, 2, 3]
    difficulty_options = [1, 2, 3, 4, 5]
    game_to_play = 0
    difficulty_level = 0
    game_result = 0
    while True:
        game = input("""Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
                2. Guess Game - guess a number and see if you chose like the computer.
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
                """)
        if game.isdigit() and int(game) in game_options:
            print(game)
            game_to_play = int(game)
            break
        print("try again")

    while True:
        difficulty = input("Select a difficulty level between 1 and 5: ")
        if difficulty.isdigit() and int(difficulty) in difficulty_options:
            print(difficulty)
            difficulty_level = int(difficulty)
            break
        print("try again")

    game_result = match_game(game_to_play, difficulty_level)

    while True:
        replay_game = input("would you like to replay the game? yes/no")
        if replay_game.upper() == 'YES':
            game_result = match_game(game_to_play, difficulty_level)
        else:
            return game_result



