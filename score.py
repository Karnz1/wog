import Utils
import os

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    score_to_add = 0
    if os.path.isfile("Scores.txt"):
        if os.path.getsize('Scores.txt') > 0:
            with open('Scores.txt', 'r') as f:
                score_to_add += int(f.readline())
                score_to_add += points_of_winning
    else:
        score_to_add += points_of_winning
    with open('Scores.txt', 'w') as f:
        print(score_to_add)
        f.write(str(score_to_add))


add_score(1)
