# The map function is used to take an iterable and output a new iterable where each element has been modified
#  according to some function.
def starts_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'John', 'Jack', 'Jill', 'Randy']
starts_with_r = filter(starts_with_r, friends) # arg 1: function that returns True/False

friends_lower = map(lambda f: f.lower(), friends)  # This produces a generator
#These are the same as the map
friends_lower1 = [friend.lower() for friend in friends]
friends_lower2 = (friend.lower() for friend in friends_lower) # It's better to use the generator comprehension.
print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    {'username': 'Rolf', 'password': '123'},
    {'username': 'John', 'password': 'apassword'},
]

users = [User.from_dict(user) for user in users]
#using a map instead of a list could be more readable
users = map(User.from_dict, users)

