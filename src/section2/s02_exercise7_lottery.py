import random

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

lottery_numbers = set(random.sample(range(22), 6))
# print(lottery_numbers);


#Top matching player is the first one
top_player = players[0]

# Go over each player
for player in players:
    # Calculate how many numbers they matched
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):
        # if they matched more than the current top player...
        top_player = player

    # Calculate their winnings using the formula
    winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
    print(f"{top_player['name']} won {winnings}.")