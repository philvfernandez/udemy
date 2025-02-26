## Notes:
#Defference between dictionaries and sets: Dictionaries keeps order where sets do not
#You can't have duplicate keys in a dictionary.

## key/value
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
print(friend_ages)

friend_ages["Rolf"] = 25
print(friend_ages)

# Tuple with three elements inside it
friends = (
    {"name": "Rolf Smtih", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
)
print(friends[0]["name"])
print(friends[0]["age"])
print(friends[1]["name"])
print(friends[1]["age"])
print(friends[2]["name"])
print(friends[2]["age"])

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
# Turn tuple into dictionary
friend_ages = dict(friends)
print(friend_ages)

my_friends = {
    'Jose': {'last_seen': 6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}
print(my_friends['Jose']['last_seen'])