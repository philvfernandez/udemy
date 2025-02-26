lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        "name": "Tawnee",
        "numbers": {13, 21, 42, 15, 7},
    },
    {
        "name": "Phil",
        "numbers": {13, 21, 22, 51, 8},
    }
]


winning_lotter_numbers = lottery_numbers.intersection(players[0]['numbers'])
num_right = len(winning_lotter_numbers)
print(f"Player",players[0]['name'],"got",num_right,"numbers right.")
winning_lotter_numbers = lottery_numbers.intersection(players[1]['numbers'])
num_right = len(winning_lotter_numbers)
print(f"Player",players[1]['name'],"fgot",num_right,"numbers right.")