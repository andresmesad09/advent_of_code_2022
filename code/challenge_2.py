"""Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
A for Rock, B for Paper, and C for Scissors.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
from pathlib import Path
POINTS = {
    # Rock
    'X': 1,
    # Paper
    'Y': 2,
    # Scissors
    'Z': 3,
}

POINTS_NEW = {
    # Rock
    'A': 1,
    # Paper
    'B': 2,
    # Scissors
    'C': 3,
}

"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you
"""
STRATEGIES_POSITION = {
    'A': 0,
    'B': 1,
    'C': 2,
}

STRATEGIES = [
    # Rock
    {
        # Lose
        'X': "C",
        # Draw
        'Y': "A",
        # Win
        'Z': "B",
    },
    # Paper
    {
        # Lose
        'X': "A",
        # Draw
        'Y': "B",
        # Win
        'Z': "C",
    },
    # Scissors
    {
        # Lose
        'X': "B",
        # Draw
        'Y': "C",
        # Win
        'Z': "A",
    },

]


# A for Rock, B for Paper, and C for Scissors.
def get_score(opponent, response):
    # lost scenarios
    if (opponent == 'A' and response == 'Z') or (opponent == 'B' and response == 'X') or (opponent == 'C' and response == 'Y'):
        score = POINTS[response]
    # draw scenarios
    elif (opponent == 'A' and response == 'X') or (opponent == 'B' and response == 'Y') or (opponent == 'C' and response == 'Z'):
        score = POINTS[response] + 3
        # win scenarios
    elif (opponent == 'A' and response == 'Y') or (opponent == 'B' and response == 'Z') or (opponent == 'C' and response == 'X'):
        score = POINTS[response] + 6
    return score


# A for Rock, B for Paper, and C for Scissors.
def get_score_new(opponent, response):
    # lost scenarios
    if (opponent == 'A' and response == 'C') or (opponent == 'C' and response == 'B') or (opponent == 'B' and response == 'A'):
        score = POINTS_NEW[response]
    # draw scenarios
    elif opponent == response:
        score = POINTS_NEW[response] + 3
        # win scenarios
    elif (response == 'A' and opponent == 'C') or (response == 'C' and opponent == 'B') or (response == 'B' and opponent == 'A'):
        score = POINTS_NEW[response] + 6
    return score


def first_part():
    input_path = Path().cwd() / "data" / "input_2_small.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()
        plays = [play.replace('\n', '') for play in file_content]

    score = 0
    for p in plays:
        opponent = p.split(' ')[0]
        strategy = p.split(' ')[1]
        score += get_score(opponent=opponent, response=strategy)

    return score


def second_part():
    input_path = Path().cwd() / "data" / "input_2.csv"
    with input_path.open(mode='r', encoding='utf-8') as file:
        file_content = file.readlines()
        plays = [play.replace('\n', '') for play in file_content]

    score = 0
    for p in plays:
        opponent = p.split(' ')[0]
        strategy = p.split(' ')[1]
        strategy_position = STRATEGIES_POSITION[opponent]
        my_play = STRATEGIES[strategy_position][strategy]
        score += get_score_new(opponent=opponent, response=my_play)

    return score


if __name__ == '__main__':
    print(f"Final score: {first_part()}")
    print(f"Second score: {second_part()}")
    # print(POINTS)
