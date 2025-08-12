accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.00, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.00, 'checking'),
    (600.50, 'savings'),
]

for t in transactions:
    # add_balance(t[0], t[1])
    # we can also do the following
    add_balance(*t) #--> argument unpacking... will pass each element of t as a separate argument.
    # A third way is to:
    # add_balance(amount=t[0], name=t[1])


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# imagine these users are coming from a database
users = [
    {'username': 'rolf', 'password':'1234' },
    {'username': 'john', 'password':'youaretoo' }
]

user_objects = [User(data['username'], data['password']) for data in users]
## Or you can do this using named arguments....
# user_objects = [User(username=data['username'], password=data['password']) for data in users]
## A third way is to use a dictionary unpacking as named arguments to a function...
## Note, this keeps the dictionary order as of python 3.7
# user_objects = [User(**data) for data in users]

#usingn a tuple
"""
users = [
    ('rolf', '1234'),
    ('john', 'youaretoo')
]

user_objects2 = [User(*data) for data in users]
"""