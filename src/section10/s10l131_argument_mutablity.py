friends_last_seen = {
    'Rolf': 31,
    'John': 21,
    'Jack': 2
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0

#global scope
print(id(friends_last_seen))
see_friend(friends_last_seen, 'Rolf')
# Prints the same id as one above
print(id(friends_last_seen))

see_friend(friends_last_seen, 'John')
print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))